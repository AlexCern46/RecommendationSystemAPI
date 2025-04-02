from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RecommendedMovieViewSet, RecommendedBookViewSet

router = DefaultRouter()
router.register(r"recommended-movies", RecommendedMovieViewSet, basename="recommended-movies")
router.register(r"recommended-books", RecommendedBookViewSet, basename="recommended-books")

urlpatterns = [
    path("", include(router.urls)),
]
