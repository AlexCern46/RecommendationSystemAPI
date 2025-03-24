import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from movies.models import Movie
from ratings.models import MovieRating


class CollaborativeFiltering:
    def get_recommendations(self, user_id):
        user_ratings = MovieRating.objects.filter(user_id=user_id).values_list('movie_id', 'rating')
        if not user_ratings:
            return []
        ratings_matrix = self.build_ratings_matrix()
        user_vector = np.array([rating for _, rating in user_ratings]).reshape(1, -1)
        similarity_scores = cosine_similarity(user_vector, ratings_matrix)
        recommendations = self.extract_recommendations(similarity_scores)
        return recommendations

    def build_ratings_matrix(self):
        # Заглушка для построения матрицы рейтингов
        pass

    def extract_recommendations(self, similarity_scores):
        # Заглушка для извлечения рекомендаций
        pass


class ContentFiltering:
    def get_recommendations(self, user_id):
        user_movies = MovieRating.objects.filter(user_id=user_id).values_list('movie_id', flat=True)
        if not user_movies:
            return []
        movie_genres = Movie.objects.filter(id__in=user_movies).values_list('genre', flat=True)
        recommended_movies = Movie.objects.filter(genre__in=movie_genres).exclude(id__in=user_movies)
        return list(recommended_movies.values_list('id', flat=True))
