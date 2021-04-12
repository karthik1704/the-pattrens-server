from django.urls import  path

from .views import UserResquestCreateView

urlpatterns = [
    path('requests/create/', UserResquestCreateView.as_view())
]