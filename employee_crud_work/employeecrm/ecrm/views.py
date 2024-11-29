from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View

from ecrm.forms import EmployeeForm
from ecrm.models import Employee


# Create your views here.
class EmployeeCreateView(View):
    template_name="create.html"
    form_class=EmployeeForm

    def get(self,request,*args,**kwargs):
        form_instance=self.form_class()
        return render(request,self.template_name,{"form":form_instance})

    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=self.form_class(form_data,files=request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("employee-add")

            return render(request,self.template_name,{"form":form_instance})



class EmployeeListView(View):
    template_name="list.html"  
  
    def get(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        return render(request,self.template_name,{"data":qs})



class EmployeeDetailView(View):
    template_name="detail.html"  
    def get(self,request,*args,**kwargs):
       id=kwargs.get("pk")
       qs=Employee.objects.get(id=id)
       
       return render(request,self.template_name,{"data":qs})


class EmployeeDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employee.objects.get(id=id).delete()
        return redirect("employee-list")       



class EmployeeUpdateView(View):
    template_name="update.html"
    form_class=EmployeeForm
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Employee_objects=get_object_or_404(Employee,id=id)
        form_instance=self.form_class(instance=Employee_objects)
        return render(request,self.template_name,{"form":form_instance})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Employee_objects=get_object_or_404(Employee,id=id)

        form_data=request.POST 
        form_instance=self.form_class(form_data,files=request.FILES,instance=Employee_objects) 
        if form_instance.is_valid():
            form_instance.save()
            return redirect("employee-list")
        return render(request,self.template_name,{"form":form_instance})

        





