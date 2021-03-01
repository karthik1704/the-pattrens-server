from rest_framework import serializers

from .models import (
    Category, 
    Element, 
    Pattern, 
    Platform,
    Tag, 
    UiApps,
    UiImages,
    Version,
)

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class ElementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Element
        fields = '__all__'

class PatternSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pattern
        fields = '__all__'

class PlatformSerializer(serializers.ModelSerializer):

    class Meta:
        model = Platform
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'

class UiImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = UiImages
        fields = '__all__'

class UiAppsListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tag = TagSerializer(many=True)
    uiimage = UiImagesSerializer(many=True)
    class Meta:
        model = UiApps
        fields = (
            'id',
            'name',
            'copyright',
            'url',
            'image',
            'category',
            'tag',
            'created_at',
            'modified_at',
            'uiimage',

        )


class UiAppsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UiApps
        fields = '__all__'