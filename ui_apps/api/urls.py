from django.urls import include, path

from rest_framework import routers

from ui_apps.views import UiAppsViewSet,UiAppsListView

router = routers.DefaultRouter()
router.register('apps', UiAppsViewSet)

urlpatterns = [
    #path('', include(router.urls)),
    path('apps/list/', UiAppsListView.as_view()),

]