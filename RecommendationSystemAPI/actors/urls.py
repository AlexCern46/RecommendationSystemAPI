from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ActorViewSet, ActorDetailView, ActorMovieView

router = DefaultRouter()
router.register(r'', ActorViewSet, basename='actor')

urlpatterns = [
    path('<int:pk>/', ActorDetailView.as_view()),
    path('<int:pk>/movies/', ActorMovieView.as_view(), name='actor-movies'),
    path('', include(router.urls))
]
