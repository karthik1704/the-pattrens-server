from django.db import models


# Create your models here.

class Platform(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)



class UiApps(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 
    image = models.ImageField(upload_to='apps/')

    class Meta:
        verbose_name = 'User Interface Apps'
        verbose_name_plural = 'User Interface Apps'


    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name



class UiImages(models.Model):
    uiapp = models.ForeignKey(UiApps, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='apps/')

