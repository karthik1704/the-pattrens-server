from tkinter import image_names
from unicodedata import category
from django.db import models

from django_extensions.db.fields import AutoSlugField

from django.conf import settings

USER = settings.AUTH_USER_MODEL 

def my_slugify_function(self, content):
        return content.replace('_', '-').replace(' ', '-').lower()

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=20)
    slug = AutoSlugField(populate_from=['catergory_name'] ,slugify_function=my_slugify_function)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 

    def __str__(self) -> str:
        return self.category_name

class Platform(models.Model):
    platform_name = models.CharField(max_length=20)
    slug = AutoSlugField(populate_from=['platform_name'] ,slugify_function=my_slugify_function)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 

    def __str__(self) -> str:
        return self.platform_name
 

class Project(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    platform = models.ManyToManyField(Platform)

    project_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    copy_right = models.CharField(max_length=100)
    url = models.URLField()
    image = models.ImageField(upload_to='projects/')    
    
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 

    def __str__(self)->str:
        return  self.project_name

# Project Image Model

class ProjectVersion(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    verion = models.CharField()



# Project Like Model
class Like(models.Model):
    user = models.ForignKey(USER, on_delete=models.DO_NOTHING)
    project = models.ForignKey(Project, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    
    def __str__(self)->str:
        return f'{self.project.name} -{self.count}'
        