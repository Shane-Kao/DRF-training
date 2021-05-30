from django.db import models

from user.models import CustomUser
# Create your models here.

class Jwt(models.Model):
    user_id = models.ForeignKey(CustomUser, related="login_user", on_delete=models.CASCADE)
    access = models.TextField()
    refresh = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)