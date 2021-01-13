from django.db import models
from django.db.models.fields import CharField, DateTimeField, SlugField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Platform(models.Model):
    name = CharField(max_length=50)
    slug = SlugField(unique=True)


class UiApps(models.Model):
    name = CharField(max_length=100)
    created_at = DateTimeField(auto_now_add=True)
    modified_at = DateTimeField(auto_now=True) 
    image = ImageField(upload_to='apps/')

    class Meta:
        verbose_name = 'User Interface Apps'
        verbose_name_plural = 'User Interface Apps'


    def __str__(self) -> str:
        return self.name

class UiImages(models.Model):
    uiapp = ForeignKey(UiApps, on_delete=models.CASCADE)
    platform = ForeignKey(Platform, on_delete=models.DO_NOTHING)
    image = ImageField(upload_to='apps/')

