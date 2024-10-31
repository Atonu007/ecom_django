from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User,Subscribe

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'phone_number', 'password', 'address', 'city', 'country', 'agreed_to_policy']
        extra_kwargs = {'password': {'write_only': True}}  

    def create(self, validated_data):
       return User.objects.create_user(**validated_data)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already in use.")
        return value

    def validate(self, attrs):
        if not attrs.get('agreed_to_policy'):
            raise serializers.ValidationError("You must agree to the policy.")
        return attrs





class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            if not user:
                raise serializers.ValidationError('Invalid email or password')
        else:
            raise serializers.ValidationError('Both fields are required')
        attrs['user'] = user 
        return attrs
    


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = ['email']  

    def validate_email(self, value):
        if Subscribe.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already subscribed.")
        return value
