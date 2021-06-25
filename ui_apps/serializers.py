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
    image64 = serializers.SerializerMethodField()
    class Meta:
        model = UiApps
        fields = (
            'id',
            'name',
            'copyright',
            'url',
            'image',
            'image64',
            'category',
            'tag',
            'created_at',
            'modified_at',
            'uiimage',

        )
    
    def get_image64(self, obj):
        import base64
        with open(obj.image,'rb') as image_file:
            image_data = base64.b32encode(image_file.read()).decode('utf-8')
            print (image_data)
        
        return f'data:image/jpeg;base64, {image_data}'

    


class UiAppsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UiApps
        fields = '__all__'