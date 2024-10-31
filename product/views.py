from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product,SubCategory,Category
from .serializers import CategorySerializer, SubCategorySerializer,ProductSerializer,CategoryList
from django.db.models import Q



class CategoryCreateView(APIView):
   
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CategoryListView(APIView):
 
    def get(self, request):
        categories = Category.objects.all()  
        serializer = CategoryList(categories, many=True)  
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class CategoryDetailUpdateView(APIView):

    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk) 
            serializer = CategorySerializer(category) 
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({"error": "Category not found."}, status=status.HTTP_404_NOT_FOUND)

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

    def delete(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)  
            category.delete() 
            return Response(status=status.HTTP_204_NO_CONTENT)  
        except Category.DoesNotExist:
            return Response({"error": "Category not found."}, status=status.HTTP_404_NOT_FOUND)


class SubCategoryCreateView(APIView):

    def post(self, request):
        serializer = SubCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SubCategoryListView(APIView):

    def get(self, request):
        subcategories = SubCategory.objects.all()  
        serializer = SubCategorySerializer(subcategories, many=True)  
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class SubCategoryDetailUpdateView(APIView):

    def get(self, request, pk):
        try:
            subcategory = SubCategory.objects.get(pk=pk) 
            serializer = SubCategorySerializer(subcategory)  
            return Response(serializer.data, status=status.HTTP_200_OK)
        except SubCategory.DoesNotExist:
            return Response({"error": "Subcategory not found."}, status=status.HTTP_404_NOT_FOUND)

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

    def delete(self, request, pk):
        try:
            subcategory = SubCategory.objects.get(pk=pk)  
            subcategory.delete()  
            return Response(status=status.HTTP_204_NO_CONTENT)  
        except SubCategory.DoesNotExist:
            return Response({"error": "Subcategory not found."}, status=status.HTTP_404_NOT_FOUND)


class ProductCreateView(APIView):

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class ProductListView(APIView):

    def get(self, request):
        products = Product.objects.all() 
        serializer = ProductSerializer(products, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)



class ProductDetailUpdateView(APIView):
 
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)  
            serializer = ProductSerializer(product) 
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)

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
        

    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)  
            product.delete() 
            return Response(status=status.HTTP_204_NO_CONTENT)  
        except Product.DoesNotExist:
            return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
        


class SearchProducts(APIView):
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
    def get(self, request, category_name):
        try:
            products = Product.objects.filter(subcategory__category__name=category_name)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)