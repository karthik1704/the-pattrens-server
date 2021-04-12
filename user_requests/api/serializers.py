from rest_framework import serializers
from user_requests.models import UserRequest

class UserRequestsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserRequest
        fields = '__all__'

