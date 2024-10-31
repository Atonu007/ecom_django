from django.urls import path
from .views import UserRegistrationView,LoginView,LogoutView, SubscribeAPIView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='api-register'),
    path('login/', LoginView.as_view(), name='login'),  
    path('logout/', LogoutView.as_view(), name='logout'),
    path('subscribe/', SubscribeAPIView.as_view(), name='subscribe'),
]
