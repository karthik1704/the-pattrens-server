from rest_framework import viewsets

from .models import UiApps
from .serializers import UiAppsSerializer
# Create your views here.

class UiAppsViewSet(viewsets.ModelViewSet):
    queryset = UiApps.objects.all()
    serializer_class = UiAppsSerializer
    