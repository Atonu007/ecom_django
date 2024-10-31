from django.db import models
from django.conf import settings
from product.models import Product

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2) 
    status = models.CharField(max_length=20, default='Pending', choices=[
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Canceled', 'Canceled')
    ])
    phone_number = models.CharField(max_length=15) 
    delivery_address = models.TextField()  
    city = models.CharField(max_length=100)  

    def __str__(self):
        return f'Order {self.id} by {self.user.username}'
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)  

    def __str__(self):
        return f'OrderItem {self.id} for Order {self.order.id}'
