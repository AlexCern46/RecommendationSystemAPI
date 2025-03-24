from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class UserRecommendations(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data = models.JSONField()
    updated_at = models.DateTimeField(auto_now=True)
