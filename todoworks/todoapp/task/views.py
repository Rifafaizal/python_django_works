from django.shortcuts import render,redirect

# Create your views here.

from django.views.generic import View

from task.forms import SignUpForm,SignInForm,TodoForm

from django.contrib.auth import authenticate,login,logout

from task.models import Todo

from django.utils.decorators import method_decorator

from task.decorators import signin_required

from django.views.decorators.cache import never_cache


decs=[signin_required,never_cache]



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
        
            print("account created")
        
            return redirect("signin")

            print("failed")

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
            
                print("session started")

                return redirect("index")

        
        print("invalid credential")
        
        return render(request,self.template_name,{"form":form_instance})  



class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")        



@method_decorator(decs,name="dispatch")
class IndexView(View):

    template_name="index.html"

    form_class=TodoForm

    def get(self,request,*args,**kwargs):
        
        qs=Todo.objects.filter(owner=request.user)
        
        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance,"data":qs})

   
    def post(self,request,*args,**kwargs):
   
        form_data=request.POST
   
        form_instance=self.form_class(form_data)
   
        if form_instance.is_valid():
           
            form_instance.instance.owner=request.user

            form_instance.save()
         
        
            return redirect("index")
        
        return render(request,self.template_name,{"form":form_instance})  

@method_decorator(decs,name="dispatch")
class TodoDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Todo.objects.get(id=id).delete()
        return redirect("index")





@method_decorator(decs,name="dispatch")
class TodoUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk") 
        Todo.objects.filter(id=id).update(status=True)  
        return redirect("index")     








