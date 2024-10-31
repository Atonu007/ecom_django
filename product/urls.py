from django.urls import path
from .views import (
    ProductsByCategoryView,
    SearchProducts,
    CategoryCreateView,
    SubCategoryCreateView,
    ProductCreateView,
    ProductListView,
    SubCategoryListView,
    CategoryListView,
    ProductDetailUpdateView,
    CategoryDetailUpdateView,
    SubCategoryDetailUpdateView,
)

urlpatterns = [
    path('add-categories/', CategoryCreateView.as_view(), name='create-category'),
    path('categories/list/', CategoryListView.as_view(), name='list-categories'),  
    path('categories/<int:pk>/', CategoryDetailUpdateView.as_view(), name='category-detail-update'), 

    path('add-subcategories/', SubCategoryCreateView.as_view(), name='create-subcategory'),
    path('subcategories/list/', SubCategoryListView.as_view(), name='list-subcategories'),
    path('subcategories/<int:pk>/', SubCategoryDetailUpdateView.as_view(), name='subcategory-detail-update'),

    path('add-product/', ProductCreateView.as_view(), name='create-product'),
    path('products/list/', ProductListView.as_view(), name='list-products'),  
    path('products/<int:pk>/', ProductDetailUpdateView.as_view(), name='product-detail-update'),
   
    path('search_products/', SearchProducts.as_view(), name='search_products'),
    path('products/category/<str:category_name>/', ProductsByCategoryView.as_view(), name='products-by-category'),
]
