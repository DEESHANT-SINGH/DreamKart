from category.models import Category
from django.shortcuts import get_object_or_404, render
from .models import Product

# Create your views here.
def store(request, category_slug=None):
    ########## Display Produts by Category By using this url patterns = ############
    ########## http://127.0.0.1:8000/store/shoes/ ##########
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)   # It will bring objects if not there then give error 404
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    #######################################################
    else:    
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()     # will count no. of products

    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)   # All things passed in context will be available for html page


# For Product_detail page
def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug = category_slug, slug = product_slug)  # category_ _slug use to get acces of the slug of that model
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
    }
    return render(request, 'store/product_detail.html', context) 