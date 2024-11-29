# operations>forms.py
from django import forms

class BmiForm(forms.Form):
    height=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))  #label height ,input type text name height
    weight=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))  #label weight ,input type text name weight




class EmiForm(forms.Form):
    loan_amount=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))
    tenure=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))
    interest=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))

class BmrForm(forms.Form):
    height=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))
    weight=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))
    age=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"})) 
    gender_choices=(
        ("male","male"),
        ("female","female")
    ) 

    gender=forms.ChoiceField(choices=gender_choices,widget=forms.Select(attrs={"class":"form-control form-select mb-3"}))

    activity_choices=(
        (1.2,"sedentary"),
        (1.375,"lightly active"),
        (1.55,"moderately active"),
        (1.725,"very active"),
        (1.9,"extra active")
    )
    activity=forms.ChoiceField(choices=activity_choices,widget=forms.Select(attrs={"class":"form-control form-select"}))

class weightManagementForm(BmrForm):
    mode_choices=(
        ("gain","gain"),
        ("loss","loss")
    )
    mode=forms.ChoiceField(choices=mode_choices,widget=forms.Select(attrs={"class":"form-control form-select"}))
    duration=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    target_weight=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))

class MilageForm(forms.Form):
    distance_travel=forms.IntegerField()
    fuel_consumed=forms.IntegerField() 

class percentageForm(forms.Form):
    amount=forms.IntegerField()    
    percentage=forms.IntegerField()


# degree_celsius to fh conversion view
class FahrenheitForm(forms.Form):
    temperature_in_degree=forms.IntegerField()

class SignUpForm(forms.Form):
    First_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))
    Last_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))
    Email=forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control mb-3"}))
    Password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-3"}))   












# fahrenheit to degree_celsius conversion view














# leap_year view
class LeapYearForm(forms.Form):
    year=forms.IntegerField() 


class RegistrationForm(forms.Form):
    Firstname=forms.CharField(label="fullname",widget=forms.TextInput(attrs={"class":"form-control mb-4"}))
    Lastname=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-4"}))
    Address=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","rows":5}))
    City=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-4"}))
    Pincode=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-4"}))
    Phone=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-4"}))
    Email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control mb-4"}))
    recommentation_choices=(
                                ('socialmedia','socialmedia'),
                                ('friend','friend'),
                                ('onsite','onsite')
    )
    Recommentation=forms.ChoiceField(label="how did you hear about us ",choices=recommentation_choices,widget=forms.Select(attrs={"class":"form-control"}))
    Other=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    Feedback=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
    Suggestion=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","rows":4}))
    rec_choices=(
                    ('yes','yes'),
                    ('no','no'),
                    ('maybe','maybe')
    )
    Recommentation_options=forms.ChoiceField(widget=forms.RadioSelect,choices=rec_choices)
    

                                    

        



