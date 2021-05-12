from store.models.customer import customer
from django.shortcuts import render,HttpResponse
from .models.product import Product
from .models.category import category
from .models.customer import customer


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
    if request.method=="GET":
        return render(request,"signup.html")
    else:
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        print(first_name, last_name , phone, email , password)

        customer = customer(first_name=first_name ,
                            last_name=last_name ,
                            phone=phone,
                            email=email ,
                            password=password)   

        customer.register()

        return HttpResponse("signup success")
