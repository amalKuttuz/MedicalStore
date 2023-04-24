from django.shortcuts import render
from .models import *
from django.views import View
from.forms import *
# Create your views here.
def homepage(request):
    context=Productlistfunction(request)
    print(context)
    return render(request,'visitor/home.html',context)

def ProductPage(request,pk):
    context=productdetailfunction(request,pk)
    return render(request,'visitor/productdetails.html',context)

def profile(request):
    if request.method == "GET":
        return render(request, "account/profile.html",{"form": ProfileForm})
    elif request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
    return render(request,'account/profile.html')




    # context={"form":form}
    # if request.method=='GET':
    #     form=ProfileForm(request.user,request.GET)
    #     if form.is_valid():
    #         form.save()
    # else:
    #     form=ProfileForm(request.user)

# def catnavlist(request):
#     catelist=CategoryList.objects.all()
#     return catelist


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

        
