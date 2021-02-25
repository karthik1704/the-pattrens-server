from check.models import Check
from django.shortcuts import render

# Create your views here.
from rest_framework import serializers, viewsets, permissions

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        return obj.user == request.user

class CheckSerializer(serializers.ModelSerializer):

    class Meta:
        model = Check
        fields = '__all__'


class CheckViewSet(viewsets.ModelViewSet):
    queryset = Check.objects.none()
    serializer_class = CheckSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        queryset = Check.objects.filter(user=self.request.user)
        return queryset