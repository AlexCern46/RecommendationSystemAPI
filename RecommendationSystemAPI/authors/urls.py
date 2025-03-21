from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AuthorViewSet, AuthorDetailView, AuthorBookView

router = DefaultRouter()
router.register(r'', AuthorViewSet, basename='author')

urlpatterns = [
    path('<int:pk>/', AuthorDetailView.as_view()),
    path('<int:pk>/books/', AuthorBookView.as_view(), name='author-books'),
    path('', include(router.urls))
]
