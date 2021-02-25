from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.
class Check(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
        

# class MyBoard(models.Model):
#     user = ForeignKey(User, on_delete=models.CASCADE)
#     name = CharField(max_length=255)
#     images = ForeignKey(UiImages, on_delete=models.DO_NOTHING, blank=True, null=True)
#     created_at = DateTimeField(auto_now_add=True)
#     modified_at = DateTimeField(auto_now=True) 

#     def __str__(self) -> str:
#         return self.name