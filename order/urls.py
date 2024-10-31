from django.urls import path
from .views import OrderCreateView, OrderHistoryView

urlpatterns = [
    path('create-order/', OrderCreateView.as_view(), name='create_order'),
    path('orders/history/', OrderHistoryView.as_view(), name='order-history'),
   
]
