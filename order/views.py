from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import  OrderSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .utils import get_user_from_token  
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class OrderCreateView(APIView):
    # permission_classes = [IsAuthenticated] 
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'total_amount': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_DECIMAL, description="Total amount of the order"),
                'items': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'product': openapi.Schema(type=openapi.TYPE_INTEGER, description="Product ID"),
                    'quantity': openapi.Schema(type=openapi.TYPE_INTEGER, description="Quantity of the product"),
                }), description="List of order items")
            },
            required=['total_amount', 'items'],
        ),
        responses={
            201: openapi.Response('Order created successfully', OrderSerializer),
            400: 'Bad Request',
            401: 'Unauthorized',
        }
    )
    def post(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]  
        user_info = get_user_from_token(token)      
        if user_info is None:
            return Response({"error": "Invalid token."}, status=status.HTTP_401_UNAUTHORIZED)
        order_data = {
            "total_amount": request.data.get("total_amount"),
            "phone_number": user_info['phone_number'],
            "delivery_address": user_info['address'],  
            "city": user_info['city'],
            "items": request.data.get("items"),  
        }
        serializer = OrderSerializer(data=order_data, context={'request': request})
        if serializer.is_valid():
            order = serializer.save(user=request.user)
            return Response({
                "order_id": order.id,
                "message": "Order created successfully."
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class OrderHistoryView(APIView):
    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={
            200: openapi.Response('Order history retrieved successfully', OrderSerializer(many=True)),
            401: 'Unauthorized',
        }
    )  
    def get(self, request, *args, **kwargs):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        response_data = []
        for order in serializer.data:
            order_data = {
                "id": order["id"],
                "created_at": order["created_at"],
                "status": order["status"],
                "total_amount": order["total_amount"],
                "items": order["items"]
            }
            response_data.append(order_data)
        return Response(response_data, status=status.HTTP_200_OK)


