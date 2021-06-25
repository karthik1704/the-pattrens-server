from rest_framework import serializers
import base64

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
    image64 = serializers.SerializerMethodField()

    class Meta:
        model = UiImages
        fields = '__all__'
    
    def get_image64(self, obj):
        #with open(obj.image,'rb') as image_file:
        image_data = base64.b64encode(obj.image.read()).decode('utf-8')   
        file_ext = obj.image.url.split('.')[-1]     
        return f'data:image/{file_ext};base64, {image_data}'

class UiAppsListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tag = TagSerializer(many=True)
    uiimage = UiImagesSerializer(many=True)
    version = VersionSerializer(many=True)
    image64 = serializers.SerializerMethodField()

    class Meta:
        model = UiApps
        fields = (
            'id',
            'name',
            'slug',
            'copyright',
            'url',
            'image',
            'image64',
            'category',
            'tag',
            'created_at',
            'modified_at',
            'version',
            'uiimage',

        )

    def get_image64(self, obj):
        #with open(obj.image,'rb') as image_file:
        print(obj.image.url.split('.')[-1])
        image_data = base64.b64encode(obj.image.read()).decode('utf-8')        
        file_ext = obj.image.url.split('.')[-1]     
        return f'data:image/{file_ext};base64, {image_data}'

class UiAppsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UiApps
        fields = '__all__'

