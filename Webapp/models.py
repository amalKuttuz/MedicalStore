from django.db import models
from django.contrib.auth.models import User

# Model of Product Categories
class CategoryList(models.Model):
    categories=models.CharField(max_length=50,default="Tablet")
    #To return the category value
    def __str__(self):
            return self.categories
    
# Model of Products
class Products(models.Model):
    med_name=models.CharField(max_length=50)
    med_price=models.IntegerField()
    med_category=models.ForeignKey(CategoryList, on_delete=models.CASCADE)
    mfg_date=models.DateField(auto_now_add=True)
    expiry_date=models.DateField( auto_now_add=False)
    med_image=models.ImageField(upload_to="productimages", height_field=None, width_field=None, max_length=None)
    added_by=models.ForeignKey(User, on_delete=models.CASCADE)
    stock_available=models.IntegerField()

    def __str__(self):
            return self.med_name
    
class Profile(models.Model):
      username=models.ForeignKey(User, on_delete=models.CASCADE)
      phone_no=models.IntegerField(max_length=9)
      housename=models.TextField()
      city=models.TextField()
      pincode=models.IntegerField( max_length=5)
      