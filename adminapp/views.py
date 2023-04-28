from django.shortcuts import render
from django.contrib.auth.models import User
from Webapp.models import *
# Create your views here.
def dashboard(request):
    return render(request,'adminapp/dashboard.html')

def manageproduct(request):
    product_list=Products.objects.filter(added_by=request.user)
    context={'product_list':product_list}
    return render(request,'adminapp/manageproducts.html',context)

def managecategory(request):
    category_list=CategoryList.objects.filter(addedby=request.user)
    context={'category_list':category_list}
    return render(request,'adminapp/managecategory.html',context)

def customers(request):
    userlist=User.objects.filter(is_staff=0)
    context={'userlist':userlist}
    return render(request,'adminapp/customers.html',context)