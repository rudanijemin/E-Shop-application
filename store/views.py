from django.shortcuts import render,HttpResponse
from .models.product import Product
from .models.category import category


# Create your views here.
def index(request):
    Products=Product.get_all_products();
    categories=category.get_all_categories();
    # return render(request  ,"order/order.html"); 
    data = {}
    data["products"]=Products
    data["categories"]=categories
    return render(request,"index.html",data)
