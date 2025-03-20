from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MovieViewSet, MovieDetailView, MovieRatingsView

router = DefaultRouter()
router.register(r'', MovieViewSet, basename='movie')

urlpatterns = [
    path('<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('<int:movie_id>/ratings/', MovieRatingsView.as_view(), name='movie-ratings'),
    path('', include(router.urls)),
]
