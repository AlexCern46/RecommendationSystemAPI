from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import DirectorViewSet, DirectorDetailView, DirectorMovieView

router = DefaultRouter()
router.register(r'', DirectorViewSet, basename='director')

urlpatterns = [
    path('<int:pk>/', DirectorDetailView.as_view()),
    path('<int:pk>/movies/', DirectorMovieView.as_view(), name='director-movies'),
    path('', include(router.urls))
]
