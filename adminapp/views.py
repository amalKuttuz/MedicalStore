from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from Webapp.models import *
from django.contrib.auth.decorators import login_required
from adminapp . forms import *
# Create your views here.
@login_required
def dashboard(request):
    return render(request,'adminapp/dashboard.html')
@login_required
def manageproduct(request):
    product_list=Products.objects.filter(added_by=request.user)
    context={'product_list':product_list}
    return render(request,'adminapp/manageproducts.html',context)

@login_required
def managecategory(request):
    category_list=CategoryList.objects.filter(addedby=request.user)
   
    context={'category_list':category_list}
    return render(request,'adminapp/managecategory.html',context)

@login_required
def customers(request):
    userlist=User.objects.filter(is_staff=0)
    context={'userlist':userlist}
    return render(request,'adminapp/customers.html',context)

def editcategory(request,pk):
    category_list=CategoryList.objects.get(id=pk)
    print(category_list)
    form=Categoryform(instance=category_list)
    context={
        'form':form

            }  
    if request.method=='POST':
        form=Categoryform(request.POST,instance=category_list)
        if form.is_valid():
            form.save()
            context={'category_list':category_list,'form':form}
        return redirect(managecategory)
    return render(request,'adminapp/editdetails.html',context)


    # form=Categoryform()
    # if request=='POST':
    #     form=Categoryform(instance=category_list)
    #     if form.is_valid:
    #         CategoryList.save()
    # else:
    #     print("error")       
    # context={'category_list':category_list,'form':form}
    # return render(request,'adminapp/editdetails.html',context)