from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.category.name} - {self.name}"

class Product(models.Model):
    img = models.ImageField(upload_to='product_images/') 
    productName = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=100)
    badge = models.BooleanField(default=False) 
    des = models.TextField()  
    brand = models.CharField(max_length=100)
    subcategory = models.ForeignKey(SubCategory, related_name='products', on_delete=models.CASCADE, null=True)
    stock = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.productName

