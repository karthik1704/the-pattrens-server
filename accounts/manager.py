from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, username=None, password=None, *agrs, **kwargs):

        if not email:
            raise ValueError('Email Required')

        user = self.model(
            username = username,
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,  username=None, password=None, *args, **kwargs):

        user = self.create_user(
            username=username,
            email=email,
            password=password
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)
        return user
    


    
