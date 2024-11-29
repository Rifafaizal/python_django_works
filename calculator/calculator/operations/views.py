from django.shortcuts import render
from django.views.generic import View,TemplateView
from operations.forms import BmiForm
from operations.forms import EmiForm
from operations.forms import BmrForm,weightManagementForm,MilageForm,percentageForm,LeapYearForm,FahrenheitForm,SignUpForm,RegistrationForm

# Create your views here.


#localhost:8000/add/
# method:get
class AdditionView(View):
    template_name="addition.html"

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)
        
        
    def post(self,request,*args,**kwargs):

        n1=request.POST.get("num1") 
        n2=request.POST.get("num2")
        result=int(n1)+int(n2)
        print(result)
        return render(request,self.template_name)  


#sub
class SubtractionView(View):
    template_name="sub.html" 
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)


    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)-int(n2)
        print(result)
        return render(request,self.template_name)



# multiplication
class MultiplicationView(View):
    template_name="multiplication.html"
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)

    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)*int(n2)
        print(result)
        return render(request,self.template_name,{"result":result})



# division
class DivisionView(View):
    template_name="division.html"
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)

    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)/int(n2)
        print(result)
        return render(request,self.template_name,{"result":result})




# cube
class CubeView(View):
    template_name="cube.html"
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        result=int(n1)**3
        print(result)
        return render(request,self.template_name,{"result":result})










#factorial
class FactorialView(View):
    template_name="factorial.html"
    def get(self,request,*args,**kwargs):
        return render( request,self.template_name)

    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        result=int(n1)


#DJANGO FORM
# BMI FORM
# url:localhost:8000/bmi/
# method:GET,POST

class BmiView(View):
    template_name="bmi.html"
    def get(self,request,*args,**kwargs):
        form_instance=BmiForm()

        return render(request,self.template_name,{"form":form_instance})

    def post(self,request,*args,**kwargs):
        # step1-extract form_data
        form_data=request.POST

        # step2-initialioze form with form_data
        form_instance=BmiForm(form_data)

        #step3-check form is valid
        if form_instance.is_valid():
            # print(form_instance.cleaned_data)  #form_instance.cleaned_data={"height":4,"weight":6}
            height=form_instance.cleaned_data.get("height")
            weight=form_instance.cleaned_data.get("weight")
            bmi=int(weight)/(int(height)/100)**2  


        #     print("form is valid")
        # else:
        #     print("form is invalid")    
           

        # bmi=int(weight)/(int(height)/100)**2
        
        return render(request,self.template_name,{"form":form_instance,"result":bmi})







       
#EMI
class EmiView(View):
    template_name="emi.html"
    def get(self,request,*args,**kwargs):
        form_instance=EmiForm()
        return render(request,self.template_name,{"form":form_instance})

    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=EmiForm(form_data)
        if form_instance.is_valid():
            loan_amount=form_instance.cleaned_data.get("loan_amount")
            tenure=form_instance.cleaned_data.get("tenure")
            interest=form_instance.cleaned_data.get("interest")
            r=int(interest)/100/12
            n=int(tenure)*12  
            one_plus_r=(1+r)**n
            emi=(int(loan_amount)*r*one_plus_r)/(one_plus_r-1)

        


      
        # form_instance=EmiForm()
        return render(request,self.template_name,{"form":form_instance,"result":emi})


#BMR
#function define cheyyan
def calculate_bmr(height,weight,age,gender):
    if gender=="male":
        bmr=10*weight+6.25*height-5*age+5
    else:
        bmr=10*weight+6.25*height-5*age-161
    return bmr

def daily_calorie_intake(bmr,activity):
    return float(activity)*bmr

           


class BmrView(View):
    template_name="bmr.html"
    def get(self,request,*args,**kwargs):
        form_instance=BmrForm()
        return render(request,self.template_name,{"form":form_instance}) 
    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=BmrForm(form_data)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            print(form_instance.cleaned_data)
            height=data.get("height")
            weight=data.get("weight")
            age=data.get("age")
            gender=data.get("gender")
            activity=data.get("activity")
            print(height,weight,age,gender,activity)

            bmr=calculate_bmr(height,weight,age,gender)
            calorie=daily_calorie_intake(bmr,activity)
            print(calorie)

        return render(request,self.template_name,{"form":form_instance,"calorie":bmr})







class weightManagementView(View):
    template_name="weight_management.html"
    form_class=weightManagementForm
    def get(self,request,*args,**kwargs):
        form_instance=self.form_class()    #enth change vannalm kodkkndiye avshym lla .auto aytt
        return render(request,self.template_name,{"form":form_instance})

    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=weightManagementForm(form_data)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            # print(form_instance.cleaned_data)
            height=data.get("height")
            weight=data.get("weight")
            age=data.get("age")
            gender=data.get("gender")
            activity=data.get("activity")
            mode=data.get("mode")
            duration=data.get("duration")
            target_weight=data.get("target_weight")
            print(height,weight,age,gender,activity,mode,duration,target_weight)

            bmr=calculate_bmr(height,weight,age,gender)
            # print(bmr)
            calorie=daily_calorie_intake(bmr,activity)
            # print(calorie)
            target_calorie=target_weight*7700
            days=duration*7
            daily_target_calorie=target_calorie/days

            total_calorie=0
            if mode=="gain":
                total_calorie=calorie+daily_target_calorie
            else:
                total_calorie=calorie-daily_target_calorie

            result=f"Total calorie to maintain current weight {round(calorie)}"
            result2=f"Total calorie to intake to {mode} in {days} days ={round(total_calorie)}"




        print("calorie to maintain current weight",calorie)
        print(f"total daily calorie to {mode} {target_weight} kg in {days}={total_calorie}")


        return render(request,self.template_name,{"form":form_instance,"result":result,"result2":result2})



#milage
# distance_travel
# fuel_consumed
# milage=distance_traveld/fuel_consumed



class MilageView(View):
    template_name="milage.html"
    form_class=MilageForm
    def get(self,request,*args,**kwargs):
        form_instance=self.form_class()
        return render(request,self.template_name,{"form":form_instance})
    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=self.form_class(form_data)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            distance_travel=data.get("distance_travel")
            fuel_consumed=data.get("fuel_consumed")
            milage=distance_travel/fuel_consumed
            return render(request,self.template_name,{"form":form_instance,"result":milage})

#percentage
#amount

class percentageView(View):
    template_name="percentage.html"
    form_class=percentageForm
    def get(self,request,*args,**kwargs):
        form_instance=self.form_class()
        return render(request,self.template_name,{"form":form_instance})
    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=self.form_class(form_data)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            amount=data.get("amount")
            percentage=data.get("percentage")
            percent=amount*percentage/100
            return render(request,self.template_name,{"form":form_instance,"result":percent})




class LeapYearView(View):
    template_name="leapyear.html"
    form_class=LeapYearForm
    def get(self,request,*args,**kwargs):
        form_instance=self.form_class()
        return render(request,self.template_name,{"form":form_instance})
    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=self.form_class(form_data)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            year=data.get("year")
            result=(year%100==0 and year%400==0) or (year%100!=0 and year%4==0)
           
            return render(request,self.template_name,{"form":form_instance,"result":result}) 




           

# temp_in_fh=(temp_in_deg*(9/5)) + 32
class FahrenheitView(View):
    template_name="Fahrenheit.html"
    form_class=FahrenheitForm
    def get(self,request,*args,**kwargs):
        form_instance=self.form_class()
        return render(request,self.template_name,{"form":form_instance})
    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=self.form_class(form_data)   
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            temperature_in_degree=data.get("temperature_in_degree")
            fh=(temperature_in_degree*(9/5)) + 32
            return render(request,self.template_name,{"form":form_instance,"result":fh})



class SignUpView(View):
    template_name="signup.html"
    form_class=SignUpForm
    def get(self,request,*args,**kwargs):
        form_instance=self.form_class()
        return render(request,self.template_name,{"form":form_instance})


class RegistrationView(View):
    template_name="reg.html"
    form_class=RegistrationForm
    def get(self,request,*args,**Kwargs):
        form_instance=self.form_class()
        return render(request,self.template_name,{"form":form_instance})                    


class IndexView(TemplateView):   #html page render cheyyndiyerm use cheynnath(render a template)
    template_name="index.html"
    # def get(self,request,*args,**kwargs):
    #     return render(request,self.template_name)
   



          





