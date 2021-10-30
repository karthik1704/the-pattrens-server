from django.db import models
from django.conf import settings

from django_extensions.db.fields import AutoSlugField

from ui_apps.models import UiImages

# Create your models here.
User = settings.AUTH_USER_MODEL

class MyBoard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board_name = models.CharField(max_length=50)
    slug = AutoSlugField(max_length=50,  null=True, populate_from=['board_name'])
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 

    

    def __str__(self) -> str:
        return self.board_name

    def slugify_function(self, content):
        return content.replace('_', '-').replace(' ', '-').lower()

    

class MyBoardItem(models.Model):
    myboard = models.ForeignKey(MyBoard, on_delete=models.CASCADE)
    image = models.ForeignKey(UiImages, on_delete=models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 