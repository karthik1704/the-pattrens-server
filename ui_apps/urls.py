from ui_apps.views import UiAppsViewSet
from django.urls import include, path

from rest_framework import routers

router = routers.DefaultRouter()
router.register('apps', UiAppsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]