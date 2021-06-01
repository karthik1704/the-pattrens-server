from rest_framework import viewsets, generics

from ui_apps.models import UiApps
from .serializers import UiAppsSerializer, UiAppsListSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class UiAppsListView(generics.ListAPIView):

    queryset = UiApps.objects.all()
    serializer_class = UiAppsListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'tag', 'platform' ]
    search_fields = ['$name',]

class UiAppsViewSet(viewsets.ModelViewSet):
    queryset = UiApps.objects.all()
    serializer_class = UiAppsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['platform', 'pattern',  ]