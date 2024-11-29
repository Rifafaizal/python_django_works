"""
URL configuration for calculator project.

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
from operations.views import AdditionView,SubtractionView,MultiplicationView,DivisionView,CubeView,FactorialView,BmiView,EmiView,BmrView,weightManagementView,MilageView,percentageView,LeapYearView,FahrenheitView,SignUpView,RegistrationView,IndexView

#


urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',AdditionView.as_view(),name="addition"),
    path('sub/',SubtractionView.as_view(),name='subtraction'),
    path('mul/',MultiplicationView.as_view(),name='multiplication'),
    path('division/',DivisionView.as_view()),
    path('cube/',CubeView.as_view(),name='cube'),
    path('factorial/',FactorialView.as_view()),

    path('bmi/',BmiView.as_view(),name="bmi"),
    path('emi/',EmiView.as_view()),
    path('bmr/',BmrView.as_view()),
    path('wm/',weightManagementView.as_view()),
    path('milage/',MilageView.as_view()),
    path('percent/',percentageView.as_view()),
    path('leapyear/',LeapYearView.as_view()),
    path('fahrenheit/',FahrenheitView.as_view()),
    path('signup/',SignUpView.as_view()),
    path('reg/',RegistrationView.as_view()),
    path('',IndexView.as_view())

    
]
