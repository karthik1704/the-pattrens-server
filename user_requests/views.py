# from rest_framework import generics
# from rest_framework.permissions import AllowAny

# from .models import UserRequest
# from .serializers import UserRequestsSerializer
# # Create your views here.

# class UserResquestCreateView(generics.CreateAPIView):

#     queryset = UserRequest.objects.all()
#     serializer_class = UserRequestsSerializer
#     permission_classes = [AllowAny]
    
from django.shortcuts  import render

def request_form(request):

    return render(request, 'user_requests/request.html', {})