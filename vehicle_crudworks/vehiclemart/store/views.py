from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from store.forms import VehicleForm
from django.db.models import Q
from store.forms import VehicleUpdateForm



from store.models import Vehicle

# Create your views here.


# fields:name,model,description,fuel_type,running_km,color,price,brand,owner_type

class VehicleView(View):
    template_name="vehicle.html"
    form_class=VehicleForm
    def get(self,request,*args,**kwargs):
        form_instance=self.form_class()
        return render(request,self.template_name,{"form":form_instance})

    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=self.form_class(form_data,files=request.FILES)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            # print(data)  #{'name': 'royal enfield', 'varient': '2003', 
                            # 'description': 'good', 'fuel_type': 'petrol', 
                            # 'running_km': '1200', 'color': 'black', 'price': 150000,
                            # 'brand': 'ror', 'owner_type': 'single'}

            #database
            Vehicle.objects.create(
                name=data.get("name"),
                varient=data.get("varient"),
                description=data.get("description"),
                fuel_type=data.get("fuel_type"),
                running_km=data.get("running_km"),
                color=data.get("color"),
                price=data.get("price"),
                brand=data.get("brand"),
                owner_type=data.get("owner_type"),
                picture=data.get("picture")
            )



            # OR Vehicle.objects.create(**data) -ith kodthalm work cheyyum

        return redirect("vehicle-list")

        return render(request,self.template_name,{"form":form_instance})


class VehicleListView(View):
    template_name="vehicle_list.html"
    def get(self,request,*args,**kwargs):
        search_text=request.GET.get("filter")
      
        qs=Vehicle.objects.all()
        all_names=Vehicle.objects.values_list("name",flat=True).distinct()
        all_brands=Vehicle.objects.values_list("brand",flat=True).distinct()
        all_fuel_types=Vehicle.objects.values_list("fuel_type",flat=True).distinct()
        all_owner_types=Vehicle.objects.values_list("owner_type",flat=True).distinct()


        all_records=[]
        all_records.extend(all_names)
        all_records.extend(all_brands)
        # print(all_records)
        all_records.extend(all_fuel_types)
        all_records.extend(all_owner_types)






        if search_text:
            qs=qs.filter(Q(name__contains=search_text)|Q(fuel_type__contains=search_text)|Q(owner_type__contains=search_text))
        return render(request,self.template_name,{"data":qs,"records":all_records})



class VehicleDetailView(View):
    template_name="vehicle_detail.html"
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Vehicle.objects.get(id=id)
        return render(request,self.template_name,{"data":qs})

class VehicleDeleteView(View):
    def get(self,request,*args,**kwargs) :
        id=kwargs.get("pk")
        Vehicle.objects.get(id=id).delete()   
        return redirect("vehicle-list")    



#update


# # class VehicleUpdateView(View):

#     template_name="edit.html"
#     form_class=VehicleForm
#     def get(self,request,*args,**kwargs):
#         id=kwargs.get("pk")
#         Vehicle_object=Vehicle.objects.get(id=id)
#         data={
#             "name":Vehicle_object.name,
#             "varient":Vehicle_object.varient,
#             "description":Vehicle_object.description,
#             "fuel_type":Vehicle_object.fuel_type,
#             "running_km":Vehicle_object.running_km,
#             "color":Vehicle_object.color,
#             "price":Vehicle_object.price,
#             "brand":Vehicle_object.brand,
#             "owner_type":Vehicle_object.owner_type,
#             "picture":Vehicle_object.picture
#         }
#         form_instance=self.form_class(initial=data)
#         return render(request,self.template_name,{"form":form_instance})
#     def post(self,request,*args,**kwargs):
#         id=kwargs.get("pk")
#         form_data=request.POST
#         form_instance=self.form_class(form_data)
#         if form_instance.is_valid():
#             data=form_instance.cleaned_data
#             Vehicle.objects.filter(id=kwargs.get("pk")).update(**data)
#             return redirect("vehicle-list")
#         return render(request,self.template_name,{"form":form_instance})

class VehicleUpdateView(View):
    template_name="edit.html"
    form_class=VehicleUpdateForm
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Vehicle_object=get_object_or_404(Vehicle,id=id)
        form_instance=self.form_class(instance=Vehicle_object)
        return render(request,self.template_name,{"form":form_instance})


    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Vehicle_object=get_object_or_404(Vehicle,id=id)
        form_data=request.POST
        form_instance=self.form_class(form_data,files=request.FILES,instance=Vehicle_object)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("vehicle-list")
        return render(request,self.template_name,{"form":form_instance})


   

