"""
URL configuration for greetings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp.views import HelloWorldView
from myapp.views import GoodMorningView
from myapp.views import GoodNightView
from myapp.views import SelfIntroView
from myapp.views import FrameWorkView
from myapp.views import CarView
from myapp.views import MobileView
from myapp.views import ChoclateView
from myapp.views import BookView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/',HelloWorldView.as_view()),
    path('goodmorning/',GoodMorningView.as_view()),
    path('goodnight/',GoodNightView.as_view()),
    path('selfintro/',SelfIntroView.as_view()),
    path('framework/',FrameWorkView.as_view()),
    path('carview/',CarView.as_view()),
    path('mobile/',MobileView.as_view()),
    path('choco/',ChoclateView.as_view()),
    path('book/',BookView.as_view()),
  

]


