from Webapp import models
from django import forms

class Categoryform(forms.ModelForm):
    
    class Meta:
        model = models.CategoryList
        fields = ['categories']
