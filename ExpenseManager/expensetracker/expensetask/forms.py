from django import forms

from expensetask.models import User,Expense

from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):

    class Meta:

        model=User

        fields=["username","email","password1","password2","phone"]


class SignInForm(forms.Form):
    username=forms.CharField(max_length=200)
    password=forms.CharField(max_length=200) 

class ExpenseForm(forms.ModelForm):
    class Meta:
        model=Expense
        fields="__all__"

class UpdateForm(forms.ModelForm):
    class Meta:
        model=Expense
        fields=["title","category","payment","amount","owner"]       
                   


    
          