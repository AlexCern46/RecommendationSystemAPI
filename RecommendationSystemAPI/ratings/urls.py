from django.urls import path

from .views import MovieRatingCreateView, MovieRatingView, BookRatingCreateView, BookRatingView

urlpatterns = [
    path('movie/', MovieRatingCreateView.as_view()),
    path('movie/<int:pk>/', MovieRatingView.as_view()),
    path('book/', BookRatingCreateView.as_view()),
    path('book/<int:pk>/', BookRatingView.as_view())
]
