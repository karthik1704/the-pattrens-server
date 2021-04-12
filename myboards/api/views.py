from rest_framework import viewsets
from rest_framework.permissions import BasePermission, IsAuthenticated

from myboards.models import MyBoard
from .serializers import MyBoardSerializer
# Create your views here.

class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):

        return obj.user == request.user

class MyBoardViewSet(viewsets.ModelViewSet):
    queryset = MyBoard.objects.none()
    serializer_class = MyBoardSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    def get_queryset(self):
        queryset = MyBoard.objects.filter(user = self.request.user)
        return queryset

    def  perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        return super(MyBoardViewSet, self).perform_create(serializer)

    def perform_update(self, serializer):
        serializer.validated_data['user'] = self.request.user
        return super(MyBoardViewSet, self).perform_update(serializer)