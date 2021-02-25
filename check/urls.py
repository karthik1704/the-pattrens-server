from check.views import CheckViewSet
from django.urls import path, include

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('check', CheckViewSet)

urlpatterns = [
    path('', include(router.urls))
]