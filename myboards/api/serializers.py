from rest_framework import serializers

from myboards.models import MyBoard, MyBoardItem

class MyBoardItemSerializer(serializers.ModelSerializer):

    class Meta:
        model=MyBoardItem
        fields='__all__'

class MyBoardSerializer(serializers.ModelSerializer):
    board_items=MyBoardItemSerializer(many=True,read_only=True)
    class Meta:
        model = MyBoard
        fields =( 'id','user','board_name','slug','created_at','modified_at', 'board_items' )
        read_only_fields = ('user','slug',)
        lookup_field = 'slug'  
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }