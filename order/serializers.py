from rest_framework import serializers
from .models import Order, OrderItem
from product.models import Product

class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    product_name = serializers.CharField(source='product.productName', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['product', 'product_name', 'quantity', 'price']
        read_only_fields = ['price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    phone_number = serializers.CharField(max_length=15, allow_blank=True)
    delivery_address = serializers.CharField(allow_blank=True)
    city = serializers.CharField(max_length=100, allow_blank=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'created_at', 'status', 'total_amount', 'items', 'phone_number', 'delivery_address', 'city']
        read_only_fields = ['id', 'created_at', 'user'] 

    def create(self, validated_data):
        order_items_data = validated_data.pop('items')
        total_amount = validated_data.pop('total_amount')     
        order = Order.objects.create(total_amount=total_amount, **validated_data)       
        for item_data in order_items_data:
            product = item_data['product']
            quantity = item_data['quantity']
            price = product.price  
            OrderItem.objects.create(order=order, product=product, quantity=quantity, price=price)
        return order
