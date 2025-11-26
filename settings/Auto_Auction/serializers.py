from tokenize import TokenError
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
import secrets

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'role',
            'data_registered',
            'token'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'token': {'read_only': True}
        }

    def create(self, validated_data):
        validated_data['token'] = secrets.token_hex(16)
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])
        if not user:
            raise ValidationError('Invalid credentials')
        return {'user': user}

class LogoutSerializer(serializers.Serializer):
    token = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs['token']
        return attrs

    def save(self, **kwargs):
        try:
            token = RefreshToken()
            token.blacklist()

        except TokenError:
            raise AuthenticationFailed('Invalid token')

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = '__all__'

class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'