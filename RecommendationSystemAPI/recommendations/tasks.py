from celery import shared_task
from django.contrib.auth import get_user_model

from .models import UserRecommendations
from .recommendation_engine import CollaborativeFiltering, ContentFiltering

User = get_user_model()


def fetch_user_data(user_id):
    # Заглушка для загрузки данных пользователя (например, оценки, статусы)
    pass


@shared_task
def generate_recommendations(user_id):
    user_data = fetch_user_data(user_id)

    if user_data:  # Коллаборативная фильтрация
        cf_model = CollaborativeFiltering()
        recommendations = cf_model.get_recommendations(user_id)
    else:  # Контентная фильтрация при недостатке данных
        cf_model = ContentFiltering()
        recommendations = cf_model.get_recommendations(user_id)

    # Сохранение результатов
    UserRecommendations.objects.update_or_create(
        user_id=user_id,
        defaults={'data': recommendations}
    )
    cache.set(f'recommendations_{user_id}', recommendations, timeout=86400)
