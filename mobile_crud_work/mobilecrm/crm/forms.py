from django import forms
from crm.models import Mobile

from django.contrib.auth.models import User



class MobileForm(forms.ModelForm):
    class Meta:
        model=Mobile
        fields="__all__"

        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "brand":forms.TextInput(attrs={"class":"form-control"}),
            "storage":forms.NumberInput(attrs={"class":"form-control"}),
            "buyer_email":forms.EmailInput(attrs={"class":"form-control"}),
            "colour":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control","rows":5}),
            "buyer_gender":forms.Select(attrs={"class":"form-control form-select"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "buy_date":forms.DateInput(attrs={"class":"form-control","type":"date"}),
            "picture":forms.FileInput(attrs={"class":"form-control"}),

            
        }

class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"] 
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"}),

        }


class SignInForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-3"}))

              