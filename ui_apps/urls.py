from django.urls import  path

from ui_apps.views import index, project_detail, project_slider


urlpatterns = [
    path('', index, name='home'),
    path('detail/<str:slug>/', project_detail, name='detail'),
    path('slider/', project_slider, name='project-slider'),

]