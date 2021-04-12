from rest_framework import viewsets, generics

from .models import UiApps
from .serializers import UiAppsSerializer, UiAppsListSerializer

from django.shortcuts import  render

# Create your views here.

def index(request):
    return render(request, 'ui_apps/apps.html', {'range': range(10)})

class UiAppsListView(generics.ListAPIView):

    queryset = UiApps.objects.all()
    serializer_class = UiAppsListSerializer

class UiAppsViewSet(viewsets.ModelViewSet):
    queryset = UiApps.objects.all()
    serializer_class = UiAppsSerializer
    