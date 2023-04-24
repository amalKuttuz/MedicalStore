from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model =Profile
        fields = ("username","phone_no","houseno","city","pincode")
