from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BookViewSet, BookDetailView, BookRatingsView

router = DefaultRouter()
router.register(r'', BookViewSet, basename='book')

urlpatterns = [
    path('<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('<int:book_id>/ratings/', BookRatingsView.as_view(), name='book-ratings'),
    path('', include(router.urls)),
]
