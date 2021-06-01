from rest_framework import serializers

from ui_apps.models import (
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

class VersionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Version
        fields = '__all__'

class UiImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = UiImages
        fields = '__all__'

class UiAppsListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tag = TagSerializer(many=True)
    uiimage = UiImagesSerializer(many=True)
    version = VersionSerializer(many=True)
    class Meta:
        model = UiApps
        fields = (
            'id',
            'name',
            'slug',
            'copyright',
            'url',
            'image',
            'category',
            'tag',
            'created_at',
            'modified_at',
            'version',
            'uiimage',

        )


class UiAppsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UiApps
        fields = '__all__'