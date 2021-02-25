from django.urls import include, path

from rest_framework import routers

from .views import MyBoardViewSet

router = routers.DefaultRouter()
router.register('myboards', MyBoardViewSet, basename='myboard')

urlpatterns = [
    path('', include(router.urls))
]