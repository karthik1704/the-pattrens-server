from rest_framework import serializers

from .models import UiApps


class UiAppsSerializer(serializers.ModelSerializer):

    class Meta:
        model =UiApps
        fields = '__all__'