from django.urls import  path

from user_requests.views import request_form, UserRequestCreateView

urlpatterns = [
    #path('', request_form, name='request')
    path('', UserRequestCreateView.as_view(), name='request')
]