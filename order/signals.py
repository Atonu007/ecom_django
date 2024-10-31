from django.db.models.signals import post_save
from django.dispatch import receiver
from product.models import Product
from .models import OrderItem

@receiver(post_save, sender=OrderItem)
def decrease_product_stock(sender, instance, created, **kwargs):
    if created: 
        if instance.product.stock >= instance.quantity:
            instance.product.stock -= instance.quantity
            instance.product.save()  
        else:
            raise ValueError("Not enough stock for this product.")
