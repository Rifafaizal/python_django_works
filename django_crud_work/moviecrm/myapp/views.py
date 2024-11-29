from django.shortcuts import render,redirect
from django.views.generic import View
from myapp.forms import MovieForm,SignUpForm,SignInForm
from django.db.models import Q

from myapp.models import Movie
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

from django.contrib import messages

from django.utils.decorators import method_decorator
from myapp.decorators import signin_required
from django.views.decorators.cache import never_cache


@method_decorator(signin_required,name="dispatch")
class MovieView(View):
    template_name="movie.html"
    form_class=MovieForm
    def get(self,request,*args,**kwargs):
        form_instance=self.form_class()
        return render(request,self.template_name,{"form":form_instance})
    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=self.form_class(form_data,files=request.FILES)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            print(data)

            Movie.objects.create(**data)
            messages.success(request,"movie successfully added!")


            return redirect("movie-list")
            messages.error(request,"movie added failed")
            return render(request,self.template_name,{"form":form_instance})

               

@method_decorator(signin_required,name="dispatch")
class MovieListView(View):
    template_name="movielist.html"
    def get(self,request,*args,**kwargs):
        search_text=request.GET.get("filter")


        qs=Movie.objects.all()
        all_titles=Movie.objects.values_list("title",flat=True).distinct()
        all_genres=Movie.objects.values_list("genre",flat=True).distinct()
        all_languages=Movie.objects.values_list("language",flat=True).distinct()
        all_directors=Movie.objects.values_list("director",flat=True).distinct()

        all_records=[]
        all_records.extend(all_titles)
        print(all_titles)
        all_records.extend(all_genres)
        all_records.extend(all_languages)
        all_records.extend(all_directors)


        if search_text:
            qs=qs.filter(Q(title__contains=search_text)|Q(genre__contains=search_text)|Q(language__contains=search_text)|Q(director__contains=search_text))

        return render(request,self.template_name,{"data":qs,"records":all_records})

@method_decorator(signin_required,name="dispatch")
class MovieDetailsView(View):
    template_name="moviedetails.html"
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Movie.objects.get(id=id)
        return render(request,self.template_name,{"data":qs})




@method_decorator(signin_required,name="dispatch")
class MovieDeleteView(View):
    def get(self,request,*args,**kwargs):
        # print(kwargs.get('pk'))
        id=kwargs.get("pk")
        Movie.objects.get(id=id).delete()
        messages.success(request,"deleted movie list")
        return redirect("movie-list") 

@method_decorator(signin_required,name="dispatch")
class MovieUpdateView(View):
   
    template_name="mobie_update.html"
   
    form_class=MovieForm
   
    def get(self,request,*args,**kwargs):
   
        id=kwargs.get("pk")
   
        Movie_object=Movie.objects.get(id=id)
        
        form_instance=self.form_class(instance=Movie_object)
   
        return render(request,self.template_name,{"form":form_instance})
   
    def post(self,request,*args,**kwargs):
   
        id=kwargs.get("pk")

        Movie_object=Movie.objects.get(id=id)

   
        form_data=request.POST
   
        form_instance=self.form_class(form_data,files=request.FILES,instance=Movie_object)
   
        if form_instance.is_valid():
   
            form_instance.save()
            messages.success(request,"movie successfully updated")


   
            return redirect("movie-list")
        messages.error(request,"movie update failed")
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

            data=form_instance.cleaned_data
            User.objects.create_user(**data)
            return redirect("login")
        
        return render(request,self.template_name,{"form":form_instance})  


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
            pswd=data.get("password")
            user_object=authenticate(request,username=uname,password=pswd)
            if user_object:

                login(request,user_object)
                return redirect("movie-list")
            return render(request,self.template_name,{"form":form_instance}) 


@method_decorator(signin_required,name="dispatch")
class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")             


        
           







