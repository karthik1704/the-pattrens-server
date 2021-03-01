from django.db import models

# Create your models here.

class UserRequest(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    app_name = models.CharField(max_length=150)
    platform = models.CharField(max_length=25)
    app_url = models.URLField()
    description = models.TextField( blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    promotion = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.app_name

    