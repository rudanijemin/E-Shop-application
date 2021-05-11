from django.shortcuts import render,HttpResponse
from .models.product import Product
from .models.category import category


# Create your views here.
def index(request):
    Products=None
    categories=category.get_all_categories();
    # return render(request  ,"order/order.html"); 
    categoryid=request.GET.get('category')
    if categoryid:
        Products=Product.get_all_products_by_categoryid(categoryid);
    else:
        Products=Product.get_all_products();

    data = {}
    data["products"]=Products
    data["categories"]=categories
    return render(request,"index.html",data)

def signup(request):
    return render(request,"signup.html")
