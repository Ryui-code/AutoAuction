from collections import defaultdict

from django.db.models import CharField
from rest_framework import status
from .filter import CarFilterSet
from .permissions import CheckStatus
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class RegisterGenericAPIView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        response = JsonResponse({'detail': 'Successfully registered.'})

        response.set_cookie(
            key='auth_token',
            value=user.token,
            httponly=True,
            secure=False,
            samesite='Lax'
        )
        return response

class LoginGenericAPIView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        response = JsonResponse({'detail': 'Successfully logged in.'})

        response.set_cookie(
            key='auth_token',
            value=user.token,
            httponly=True,
            secure=False,
            samesite='Lax'
        )
        return response

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = JsonResponse({'detail': 'Successfully logged out.'})
        response.delete_cookie('auth_token')
        return response

class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [CheckStatus]

class AuctionViewSet(viewsets.ModelViewSet):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    permission_classes = [CheckStatus]

class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    permission_classes = [CheckStatus]

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [CheckStatus]