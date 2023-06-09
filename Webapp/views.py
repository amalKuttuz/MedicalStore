from django.shortcuts import redirect, render
from .models import *
from django.views import View
from.forms import *
# Create your views here.
def homepage(request):
    context=Productlistfunction(request)
    return render(request,'visitor/home.html',context)

def productpage(request,pk):
    context=productdetailfunction(request,pk)
    return render(request,'visitor/productdetails.html',context)

def aboutpage(request):
    return render(request,'visitor/about.html')

def contactpage(request):
    return render(request,'visitor/contact.html')

def userprofile(request):
        form = ProfileForm(instance=request.user)
        context={'form':form}
        if request.method == "POST":
            form = ProfileForm(request.POST)
            if form.is_valid():
                user = form.save()
        return render(request,'account/profile.html',context)

def cart(request):
    products=Cart.objects.filter(username=request.user)
    return render(request,'account/cart.html')
 
def addtocart(request,pk):
    cart=User.objects.filter(username=request.user)
    prd=Products.objects.filter(id=pk)
    quanity='1'
    Cart.save(cart,prd,quanity)
    return redirect("cart")




    # context={"form":form}
    # if request.method=='GET':
    #     form=ProfileForm(request.user,request.GET)
    #     if form.is_valid():
    #         form.save()
    # else:
    #     form=ProfileForm(request.user)

def categoryfunction(request):
    catelist=CategoryList.objects.all()
    context= {catelist}
    return context


def Productlistfunction(request):
    allprdlist= Products.objects.all()
    catlist=CategoryList.objects.all()
    context={"allprdlist":allprdlist,"catlist":catlist}
    return context

def productdetailfunction(request,pk):
    prddetails=Products.objects.filter(id=pk)
    context={"prddetails":prddetails}    
    return context

# class ProductCategory(View):
#     def get(request,pk):
#         catprd=CategoryList.objects.filter(categories=pk)
#         return render(request,'ProductCategores.html',catprd)

        
