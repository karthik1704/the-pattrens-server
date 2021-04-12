from django.urls import  path


from myboards.views import myboards



urlpatterns = [
    path('', myboards, name='myboards' )
]