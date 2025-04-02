import pandas as pd
from books.models import Book
from celery import shared_task
from movies.models import Movie
from ratings.models import MovieRating, BookRating
from surprise import Dataset, Reader, SVD

from .models import RecommendedMovie, RecommendedBook

STATUS_WEIGHTS = {
    "watched": 1.0, "watching": 0.7, "plan to watch": 0.3,
    "read": 1.0, "reading": 0.7, "plan to read": 0.3
}


@shared_task
def generate_recommendations():
    movie_ratings = MovieRating.objects.select_related("user", "movie").values(
        "user_id", "movie_id", "rating", "user__usermoviestatus__status"
    )
    book_ratings = BookRating.objects.select_related("user", "book").values(
        "user_id", "book_id", "rating", "user__userbookstatus__status"
    )

    movie_df = pd.DataFrame(list(movie_ratings))
    book_df = pd.DataFrame(list(book_ratings))

    def apply_weight(row, col):
        return row["rating"] * STATUS_WEIGHTS.get(row[col], 0)

    if not movie_df.empty:
        movie_df["weighted_rating"] = movie_df.apply(lambda row: apply_weight(row, "user__usermoviestatus__status"),
                                                     axis=1)
        movie_df = movie_df[movie_df["weighted_rating"] > 0]

    if not book_df.empty:
        book_df["weighted_rating"] = book_df.apply(lambda row: apply_weight(row, "user__userbookstatus__status"),
                                                   axis=1)
        book_df = book_df[book_df["weighted_rating"] > 0]

    def train_model(df, id_column):
        reader = Reader(rating_scale=(1, 10))
        data = Dataset.load_from_df(df[["user_id", id_column, "weighted_rating"]], reader)
        model = SVD()
        model.fit(data.build_full_trainset())
        return model

    if not movie_df.empty:
        movie_model = train_model(movie_df, "movie_id")
        RecommendedMovie.objects.all().delete()
        for user_id in movie_df["user_id"].unique():
            watched = set(movie_df[movie_df["user_id"] == user_id]["movie_id"])
            recommendations = sorted(
                [(m, movie_model.predict(user_id, m).est) for m in
                 set(Movie.objects.values_list("id", flat=True)) - watched],
                key=lambda x: x[1], reverse=True
            )[:5]
            RecommendedMovie.objects.bulk_create([
                RecommendedMovie(user_id=user_id, movie_id=mid, score=score) for mid, score in recommendations
            ])

    if not book_df.empty:
        book_model = train_model(book_df, "book_id")
        RecommendedBook.objects.all().delete()
        for user_id in book_df["user_id"].unique():
            read = set(book_df[book_df["user_id"] == user_id]["book_id"])
            recommendations = sorted(
                [(b, book_model.predict(user_id, b).est) for b in
                 set(Book.objects.values_list("id", flat=True)) - read],
                key=lambda x: x[1], reverse=True
            )[:5]
            RecommendedBook.objects.bulk_create([
                RecommendedBook(user_id=user_id, book_id=bid, score=score) for bid, score in recommendations
            ])
