from django.shortcuts import render,redirect

# Create your views here.

from django.views.generic import View

from django.contrib.auth import authenticate,login,logout

from expensetask.forms import SignInForm,SignUpForm,ExpenseForm,UpdateForm

from expensetask.models import Expense


class SignUpView(View):
    template_name="signup.html"
    form_class=SignUpForm
    def get(self,request,*args,**kwargs):
        form_instance=self.form_class()
        return render(request,self.template_name,{"form":form_instance})

    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=self.form_class(form_data)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("signin")
        return render(request,self.template_name,{"form":form_instance})  


class SignInView(View):
    template_name="signin.html"
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
                return redirect("create")
                return render(request,self.template_name,{"form":form_instance})


class CreateView(View):
    template_name="create.html"
    form_class=ExpenseForm
    def get(self,request,*args,**kwargs):
        form_instance=self.form_class()
        qs=Expense.objects.filter(owner=request.user)
        return render(request,self.template_name,{"form":form_instance,"data":qs})
    def post(self,request,*args,**kwargs):
        form_class=ExpenseForm
        form_data=request.POST
        qs=Expense.objects.filter(owner=request.user)  
        form_instance=self.form_class(form_data)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("create")  
            return render(request,self.template_name,{"form":form_instance,"data":qs})

class ListView(View):
    template_name="list.html"
  
    def get(self,request,*args,**kwargs):
        qs=Expense.objects.all()
     
        return render(request,self.template_name,{"data":qs})  

class DetailView(View):
    template_name="detail.html"   
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Expense.objects.get(id=id)
        return render(request,self.template_name,{"data":qs})  


class DeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Expense.objects.filter(id=id).delete()  
        return redirect("list") 


class UpdateView(View):
    template_name="update.html"
    form_class=UpdateForm
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        user_object=Expense.objects.get(id=id)
        form_instance=self.form_class(instance=user_object)
        return render(request,self.template_name,{"form":form_instance})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")  
        user_object=Expense.objects.get(id=id) 
        form_data=request.POST
        
        form_instance=self.form_class(form_data,instance=user_object)
        if form_instance.is_valid():
            form_instance.save()
            
            return redirect("list")
            return render(request,self.template_name,{"form":form_instance})

                      










