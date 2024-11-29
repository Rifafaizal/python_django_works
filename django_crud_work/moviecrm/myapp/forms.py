from django import forms
from myapp.models import Movie
from django.contrib.auth.models import User


# class MovieForm(forms.Form):
#     title=forms.CharField()
#     genre=forms.CharField()
#     runtime=forms.IntegerField()
#     language=forms.CharField()
#     year=forms.CharField()
#     director=forms.CharField()
#     actor=forms.CharField()
#     picture=forms.ImageField()


class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields="__all__"


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
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))        

      