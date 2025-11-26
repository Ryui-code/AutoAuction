from rest_framework.routers import DefaultRouter
from .views import RegisterGenericAPIView, LoginGenericAPIView, LogoutAPIView, CarViewSet, AuctionViewSet, BidViewSet, FeedbackViewSet, ProfileViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'profile', ProfileViewSet, basename='profile')
router.register(r'car', CarViewSet, basename='car')
router.register(r'auction', AuctionViewSet, basename='auction')
router.register(r'bid', BidViewSet, basename='bid')
router.register(r'feedback', FeedbackViewSet, basename='feedback')

urlpatterns = [
    path('register/', RegisterGenericAPIView.as_view(), name='register'),
    path('login/', LoginGenericAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('', include(router.urls))
]