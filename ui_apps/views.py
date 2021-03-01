from rest_framework import viewsets, generics

from .models import UiApps
from .serializers import UiAppsSerializer, UiAppsListSerializer

# Create your views here.

class UiAppsListView(generics.ListAPIView):

    queryset = UiApps.objects.all()
    serializer_class = UiAppsListSerializer

class UiAppsViewSet(viewsets.ModelViewSet):
    queryset = UiApps.objects.all()
    serializer_class = UiAppsSerializer
    