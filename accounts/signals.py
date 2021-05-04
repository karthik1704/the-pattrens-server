# from allauth.account.signals import user_signed_up
from django.db.models.signals  import post_save
from django.dispatch.dispatcher import receiver
from accounts.models import Profile, User
from myboards.models import MyBoard

@receiver(post_save , sender=User)
def create_default_board(sender, instance, created, **kwargs):
    if created:
        MyBoard.objects.create(user=instance, name='Default Board')
        Profile.objects.create(user=instance)
        