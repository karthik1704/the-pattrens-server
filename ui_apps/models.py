from django.db import models
from django.db.models.fields import CharField, DateTimeField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class UiApps(models.Model):
    name = CharField(max_length=100)
    created_at = DateTimeField(auto_now_add=True)
    modified_at = DateTimeField(auto_now=True) 
    image = ImageField(upload_to='/apps/')

class UiImages(models.Model):
    uiapp = ForeignKey(UiApps, on_delete=models.CASCADE)
    image = ImageField(upload_to='/apps/')

