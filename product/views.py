from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product,SubCategory,Category
from .serializers import CategorySerializer, SubCategorySerializer,ProductSerializer,CategoryList
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated



class CategoryCreateView(APIView):
    # permission_classes = [IsAuthenticated] 
    
    @swagger_auto_schema(
        request_body=CategorySerializer,
        responses={201: openapi.Response('Category created successfully'), 400: 'Bad Request'}
    )
   
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CategoryListView(APIView):
    @swagger_auto_schema(
        responses={200: CategoryList(many=True), 404: 'Not Found'}
    )
 
    def get(self, request):
        categories = Category.objects.all()  
        serializer = CategoryList(categories, many=True)  
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class CategoryDetailUpdateView(APIView):
    # permission_classes = [IsAuthenticated] 
    @swagger_auto_schema(
        responses={200: CategorySerializer, 404: 'Category not found'}
    )

    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk) 
            serializer = CategorySerializer(category) 
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({"error": "Category not found."}, status=status.HTTP_404_NOT_FOUND)
        
    @swagger_auto_schema(
        request_body=CategorySerializer,
        responses={200: CategorySerializer, 404: 'Category not found', 400: 'Bad Request'}
    )

    def post(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)  
            serializer = CategorySerializer(category, data=request.data, partial=True)  
            if serializer.is_valid():
                serializer.save()  
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Category.DoesNotExist:
            return Response({"error": "Category not found."}, status=status.HTTP_404_NOT_FOUND)
        
    @swagger_auto_schema(
        responses={204: 'Category deleted successfully', 404: 'Category not found'}
    )

    def delete(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)  
            category.delete() 
            return Response(status=status.HTTP_204_NO_CONTENT)  
        except Category.DoesNotExist:
            return Response({"error": "Category not found."}, status=status.HTTP_404_NOT_FOUND)


class SubCategoryCreateView(APIView):
    # permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        request_body=SubCategorySerializer,
        responses={201: openapi.Response('Subcategory created successfully'), 400: 'Bad Request'}
    ) 

    def post(self, request):
        serializer = SubCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SubCategoryListView(APIView):
    @swagger_auto_schema(
        responses={200: SubCategorySerializer(many=True)}
    )

    def get(self, request):
        subcategories = SubCategory.objects.all()  
        serializer = SubCategorySerializer(subcategories, many=True)  
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class SubCategoryDetailUpdateView(APIView):
    # permission_classes = [IsAuthenticated] 

    @swagger_auto_schema(
        responses={200: SubCategorySerializer, 404: 'Subcategory not found'}
    )

    def get(self, request, pk):
        try:
            subcategory = SubCategory.objects.get(pk=pk) 
            serializer = SubCategorySerializer(subcategory)  
            return Response(serializer.data, status=status.HTTP_200_OK)
        except SubCategory.DoesNotExist:
            return Response({"error": "Subcategory not found."}, status=status.HTTP_404_NOT_FOUND)
    @swagger_auto_schema(
        request_body=SubCategorySerializer,
        responses={200: SubCategorySerializer, 404: 'Subcategory not found', 400: 'Bad Request'}
    )


    def post(self, request, pk):
        
        try:
            subcategory = SubCategory.objects.get(pk=pk) 
            serializer = SubCategorySerializer(subcategory, data=request.data, partial=True)  
            if serializer.is_valid():
                serializer.save()  
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except SubCategory.DoesNotExist:
            return Response({"error": "Subcategory not found."}, status=status.HTTP_404_NOT_FOUND)
        

    @swagger_auto_schema(
        responses={204: 'Subcategory deleted successfully', 404: 'Subcategory not found'}
    )

    def delete(self, request, pk):
        try:
            subcategory = SubCategory.objects.get(pk=pk)  
            subcategory.delete()  
            return Response(status=status.HTTP_204_NO_CONTENT)  
        except SubCategory.DoesNotExist:
            return Response({"error": "Subcategory not found."}, status=status.HTTP_404_NOT_FOUND)


class ProductCreateView(APIView):
    # permission_classes = [IsAuthenticated] 

    @swagger_auto_schema(
        request_body=ProductSerializer,
        responses={201: openapi.Response('Product created successfully'), 400: 'Bad Request'}
    )

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class ProductListView(APIView):
    @swagger_auto_schema(
        responses={200: ProductSerializer(many=True)}
    )

    def get(self, request):
        products = Product.objects.all() 
        serializer = ProductSerializer(products, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)



class ProductDetailUpdateView(APIView):
    # permission_classes = [IsAuthenticated] 

    @swagger_auto_schema(
        responses={200: ProductSerializer, 404: 'Product not found'}
    )
 
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)  
            serializer = ProductSerializer(product) 
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
        

    @swagger_auto_schema(
        request_body=ProductSerializer,
        responses={200: ProductSerializer, 404: 'Product not found', 400: 'Bad Request'}
    )

    def post(self, request, pk):
        try:
            product = Product.objects.get(pk=pk) 
            serializer = ProductSerializer(product, data=request.data, partial=True)  
            if serializer.is_valid():
                serializer.save() 
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
        
    @swagger_auto_schema(
        responses={204: 'Product deleted successfully', 404: 'Product not found'}
    )
    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)  
            product.delete() 
            return Response(status=status.HTTP_204_NO_CONTENT)  
        except Product.DoesNotExist:
            return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
        


class SearchProducts(APIView):
    @swagger_auto_schema(
        responses={200: ProductSerializer(many=True)}
    )
    def get(self, request):
        query = request.GET.get('query', '')
        if query:
            products = Product.objects.filter(
                Q(productName__icontains=query) |
                Q(brand__icontains=query) |
                Q(des__icontains=query)
            )
        else:
            products = Product.objects.none()  
        serialized_products = ProductSerializer(products, many=True).data
        return Response(serialized_products, status=status.HTTP_200_OK)
    

class ProductsByCategoryView(APIView):
    @swagger_auto_schema(
        responses={200: ProductSerializer(many=True), 404: 'Category not found'}
    )
    def get(self, request, category_name):
        try:
            products = Product.objects.filter(subcategory__category__name=category_name)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)