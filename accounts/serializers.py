from rest_framework import serializers

from accounts.models import User


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk','email')
        read_only_fields = ('email',)



# class RegisterSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password1= serializers.CharField(write_only=True, style={'input_type': 'password'})
#     password2= serializers.CharField(write_only=True, style={'input_type': 'password'})

#     def validate(self, data):
#         if data['password1'] != data['password2']:
#             raise serializers.ValidationError(_("The two password fields didn't match."))
#         return data

#     def get_cleaned_data(self):
#         return {
#             'email': self.validated_data.get('email', ''),
#             'password1': self.validated_data.get('password1', ''),
#         }

#     def save(self,request):
#         pass