from django.shortcuts import render
from .models import *
from django.views import View
# Create your views here.
def homepage(request):
    productdata=Productlistview(request)
    return render(request,'visitor/home.html',productdata)

def ProductPage(request):
    prddetails=productdetailview(request)
    return render(request,'productdetails.html',prddetails)

# def catnavlist(request):
#     catelist=CategoryList.objects.all()
#     return catelist


def Productlistview(request):
    allprdlist= Products.objects.all()
    catlist=CategoryList.objects.all()
    context={"allprdlist":allprdlist,"catlist":catlist}
    return context
def productdetailview(request,pk):
    prddetails=Products.objects.filter(id=pk)
    return prddetails

# class ProductCategory(View):
#     def get(request,pk):
#         catprd=CategoryList.objects.filter(categories=pk)
#         return render(request,'ProductCategores.html',catprd)

        
