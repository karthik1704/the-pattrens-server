from django.db import models
from django.conf import settings

from ui_apps.models import UiImages

# Create your models here.
User = settings.AUTH_USER_MODEL

class MyBoard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 

    def __str__(self) -> str:
        return self.name

    

class MyBoardItem(models.Model):
    image = models.ForeignKey(UiImages, on_delete=models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 