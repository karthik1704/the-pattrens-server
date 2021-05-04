from django.urls import  path


from myboards.views import myboard_detail, myboards


urlpatterns = [
    path('', myboards, name='myboards' ),
    path('<int:pk>/', myboard_detail, name='myboards_detail' )
]