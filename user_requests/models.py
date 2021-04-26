from django.db import models

# Create your models here.

class UserRequest(models.Model):
    name = models.CharField('Your Name',max_length=150, blank=True, null=True)
    app_name = models.CharField(max_length=150)
    platform = models.CharField(max_length=25)
    app_url = models.URLField('App URL/ Website URL')
    description = models.TextField('Why do you love this app?', blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    promotion = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.app_name

    