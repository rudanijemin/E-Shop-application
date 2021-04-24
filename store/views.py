from django.shortcuts import render,HttpResponse
from .models.product import Product


# Create your views here.
def index(request):
    Prds=Product.get_all_products();
    
    return render(request,"index.html",{"products":Prds})
