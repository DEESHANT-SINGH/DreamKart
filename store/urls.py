from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    # Display Produts by Category By using this url patterns = http://127.0.0.1:8000/store/shoes/
    path('<slug:category_slug>/', views.store, name='products_by_category'),
    # Display Product Details By using url patterns = http://127.0.0.1:8000/category_slug/product_slug/
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
] 
