from django.shortcuts import render,redirect,get_object_or_404
from crm.forms import  MobileForm,SignUpForm,SignInForm
from django.views.generic import View
from crm.models import Mobile 
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from django.utils.decorators import method_decorator
from crm.decorators import signin_required
from django.views.decorators.cache import never_cache

# Create your views here.


# localhost:8000/employee/create/
# get,post
# static
#css,images,js
decs=[signin_required,never_cache]
@method_decorator(decs,name="dispatch")
class MobileCreateView(View):
    template_name="create.html"
    form_class=MobileForm

    def get(self,request,*args,**kwargs):
        form_instance=self.form_class()
        return render(request,self.template_name,{"form":form_instance})

    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=self.form_class(form_data,files=request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            messages.success(request,"mobile item is successfully added")
            return redirect("mobile-add")

            messages.error(request,"adding is failed")

        return render(request,self.template_name,{"form":form_instance})


@method_decorator(decs,name="dispatch")
class MobileListView(View):
    template_name="moblist.html"  
  
    def get(self,request,*args,**kwargs):
        qs=Mobile.objects.all()
        return render(request,self.template_name,{"data":qs})


@method_decorator(decs,name="dispatch")
class MobileDetailView(View):
    template_name="detail.html"  
    def get(self,request,*args,**kwargs):
       id=kwargs.get("pk")
       qs=Mobile.objects.get(id=id)
       
       return render(request,self.template_name,{"data":qs})

@method_decorator(decs,name="dispatch")
class MobileDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Mobile.objects.get(id=id).delete()
        messages.success(request,"successfully deleted")
        return redirect("mobile-list")       


@method_decorator(decs,name="dispatch")
class MobileUpdateView(View):
    template_name="update.html"
    form_class=MobileForm
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Mobile_objects=get_object_or_404(Mobile,id=id)
        form_instance=self.form_class(instance=Mobile_objects)
        return render(request,self.template_name,{"form":form_instance})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Mobile_objects=get_object_or_404(Mobile,id=id)

        form_data=request.POST 
        form_instance=self.form_class(form_data,files=request.FILES,instance=Mobile_objects) 
        if form_instance.is_valid():
            form_instance.save()
            messages.success(request,"successfully mobile item updated")
            return redirect("mobile-list")
            messages.error(request,"update is failed")
        return render(request,self.template_name,{"form":form_instance})

       
class SignUpView(View):
    template_name="register.html"
    form_class=SignUpForm
    def get(self,request,*args,**kwargs):
        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})

    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=self.form_class(form_data)
        if form_instance.is_valid():
            # form_instance.save()
            data=form_instance.cleaned_data

            #plaintest=>encrypt
                #create_user-password hide aytt kanikan venmdi
                #sequred hash algorithm
            User.objects.create_user(**data)
            return redirect("signin")
        return render(request,self.template_name,{"form":form_instance})



# login
# localhost:8000/signin
# get ,

class SignInView(View):
    template_name="login.html"
    form_class=SignInForm
    def get(self,request,*args,**kwargs):
        form_instance=self.form_class()
        return render(request,self.template_name,{"form":form_instance})  

    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=self.form_class(form_data)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            uname=data.get("username")
            pwd=data.get("password")
            user_object=authenticate(request,username=uname,password=pwd)
            if user_object:
                login(request,user_object)
                return redirect("mobile-list")
        return render(request,self.template_name,{"form":form_instance}) 

@method_decorator(decs,name="dispatch")
class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")               




 





