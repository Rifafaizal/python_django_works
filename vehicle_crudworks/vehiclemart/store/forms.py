from django import forms
from store.models import Vehicle

# fields:name,model,description,fuel_type,running_km,color,price,brand,owner_type


class VehicleForm(forms.Form):
    
    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-5"}))
    
    varient=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-5"}))
    
    description=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-5"}))
    
    fuel_type=forms.ChoiceField(choices=Vehicle.fuel_options,widget=forms.Select(attrs={"class":"form-control form-select mb-5"}))
    
    running_km=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-5"}))
    
    color=forms.CharField(widget=forms.TextInput(attrs={"class":"text-control mb-5"}))
    
    price=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"text-control mb-5"}))
    
    brand=forms.CharField(widget=forms.TextInput(attrs={"class":"text-control mb-5"}))
    
    owner_type=forms.ChoiceField(choices=Vehicle.owner_options,widget=forms.Select(attrs={"class":"text-control text-select mb-5"}))
    
    picture=forms.ImageField()


class VehicleUpdateForm(forms.ModelForm):
    class Meta:
        model=Vehicle
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "varient":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control","rows":5}),
            "fuel_type":forms.Select(attrs={"class":"form-control form-select"}),
            "running_km":forms.TextInput(attrs={"class":"form-control"}),
            "color":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "brand":forms.NumberInput(attrs={"class":"form-control"}),
            "owner_type":forms.Select(attrs={"class":"form-control form-select"}),
            "picture":forms.FileInput(attrs={"class":"form-control"}) 
            
            
             }

