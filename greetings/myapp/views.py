
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render


#localhost:8000/helloworld/
class HelloWorldView(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse("helloworld")

 #localhost:8000/goodmorning/       
class GoodMorningView(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse("goodmorning")


#localhost:8000/goodnight/
class GoodNightView(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse("goodnight")


#localhost:8000/goodnight/
# method:get
# response:selfintro.html

class SelfIntroView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"selfintro.html") 

#localhost:8000/framework/
#method:get
#response:framework.html django dlask oodo,,




class FrameWorkView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"framework.html")



#carview > list car details(html)
class CarView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"carview.html")



# mobilesview > list mobile details (html)
class MobileView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"mobileview.html")  

#choclates
class ChoclateView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"choclate.html")


#book
class BookView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"book.html")        







        










