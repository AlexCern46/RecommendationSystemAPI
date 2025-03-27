from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UpdateMovieStatusView, MoviesByStatusView, UpdateBookStatusView, BooksByStatusView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('movies/<int:movie_id>/', UpdateMovieStatusView.as_view(), name='update_movie_status'),
    path('movies/', MoviesByStatusView.as_view(), name='movies_by_status'),
    path('books/<int:book_id>/', UpdateBookStatusView.as_view(), name='update_book_status'),
    path('books', BooksByStatusView.as_view(), name='books_by_status'),
]