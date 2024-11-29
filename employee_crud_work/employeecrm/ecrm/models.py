from django.db import models

# Create your models here.
class Employee(models.Model):

    name= models.CharField(max_length=30)

    email= models.EmailField(max_length=30)

    address=models.TextField(max_length=100)

    department=models.CharField(max_length=100)

    salary=models.IntegerField()

    date_of_join=models.DateField()

    gender_option=[
        ("male","male"),
        ("female","female")
    ]

    gender=models.CharField(max_length=30,choices=gender_option,default="male")

    picture=models.ImageField(upload_to="employee_image",null=True)
