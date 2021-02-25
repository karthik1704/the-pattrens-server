from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models.fields import BooleanField, CharField, DateField, DateTimeField, EmailField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import OneToOneField

from .manager import UserManager
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    
    username = CharField(max_length=25, blank=True, null=True, unique=True, db_index=True)
    email = EmailField(unique=True, db_index=True)
    is_superuser = BooleanField(default=False)
    is_staff = BooleanField(default=False)
    is_active = BooleanField(default=True) 
    
    created = DateTimeField(auto_now_add=True)
    last_login = DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self) -> str:
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_superuser

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return self.is_superuser







class Profile(models.Model):
    user = OneToOneField(User,on_delete=models.CASCADE)
    avatar = ImageField(upload_to="avatar/", blank=True, null=True)
    first_name = CharField(max_length=100,blank=True, null=True)
    last_name = CharField(max_length=100,blank=True, null=True)
    birth_date = DateField(blank=True, null=True)
