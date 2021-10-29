from django.db import models

from django.conf import settings

USER = settings.AUTH_USER_MODEL 
# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    copy_right = models.CharField(max_length=100)
    url = models.URLField()
    image = models.ImageField(upload_to='projects/')    
    
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 

    def __str__(self)->str:
        return  self.name
    
class Like(models.Model):
    user = models.ForignKey(USER, on_delete=models.DO_NOTHING)
    project = models.ForignKey(Project, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    
    def __str__(self)->str:
        return f'{self.project.name} -{self.count}'
        