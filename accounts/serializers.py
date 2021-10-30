from rest_framework import serializers

from accounts.models import User


class UserDetailSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(source='profile.avatar', read_only=True)
    class Meta:
        model = User
        fields = ('pk','email', 'first_name', 'last_name', 'avatar')
        read_only_fields = ('email',)



class UserRegisterSerializer(serializers.ModelSerializer):
    first_name=serializers.CharField()
    last_name=serializers.CharField()
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = User
        fields = [ 'email', 'first_name','last_name',
        'password', 'password2',]
        extra_kwargs = {
            'password': {
                'style':{'input_type':'password'},
                'write_only':True
            }
        }    

    def save(self, request):
        
        user = User(
            email = self.validated_data['email'] or None,
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
        )

        password1 = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password1 != password2:
            raise serializers.ValidationError({'password': 'Password Must Match.'})

        user.set_password(password1)
        user.save()
        return user