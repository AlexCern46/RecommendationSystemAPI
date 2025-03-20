from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UpdateMovieStatusView, MoviesByStatusView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('movies/<int:movie_id>/status/', UpdateMovieStatusView.as_view(), name='update_movie_status'),
    path('status/', MoviesByStatusView.as_view(), name='movies_by_status'),
]