# accounts/urls.py
from django.urls import path
from .views import RegisterAPIView, LoginAPIView, ProtectedAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='api_register'),
    path('login/', LoginAPIView.as_view(), name='api_login'),
    path('protected/', ProtectedAPIView.as_view(), name='api_protected'),
]