from django.urls import  path

from .views import request_form

urlpatterns = [
    path('', request_form, name='request')
]