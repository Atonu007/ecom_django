from rest_framework import serializers
from .models import Category, SubCategory,Product


class SubCategorySerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category']
    def create(self, validated_data):
        category = validated_data.pop('category')
        name = validated_data.get('name')
        subcategory = SubCategory.objects.create(name=name, category=category)
        return subcategory
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']  
    def create(self, validated_data):
        category = Category.objects.create(**validated_data)
        return category
    

class CategoryList(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True) 
    class Meta:
        model = Category
        fields = ['id', 'name', 'subcategories']



class ProductSerializer(serializers.ModelSerializer):
    subcategory = serializers.PrimaryKeyRelatedField(queryset=SubCategory.objects.all())  
    class Meta:
        model = Product
        fields = ['id', 'img', 'productName', 'price', 'color', 'badge', 'des', 'brand', 'subcategory', 'stock', 'date_added']
    def create(self, validated_data):
        product = Product.objects.create(**validated_data)
        return product
    


