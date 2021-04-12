from django.urls import path

from accounts.views import settings

urlpatterns = [
    path('', settings, name='settings' )
]