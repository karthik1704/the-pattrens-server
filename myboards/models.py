from django.db import models
from django.conf import settings
from django.db.models.fields import CharField, DateTimeField
from django.db.models.fields.related import ForeignKey
# Create your models here.

User = settings.AUTH_USER_MODEL

class MyBoard(models.Model):
    user = ForeignKey(User, on_delete=models.CASCADE)
    name = CharField(max_length=255)
    created_at = DateTimeField(auto_now_add=True)
    modified_at = DateTimeField(auto_now=True) 