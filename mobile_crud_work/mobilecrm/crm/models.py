from django.db import models

# Create your models here.

class Mobile(models.Model):

    name=models.CharField(max_length=200)

    brand=models.CharField(max_length=100)

    storage=models.PositiveIntegerField()

    buyer_email=models.EmailField(max_length=30)

    colour=models.CharField(max_length=100)

    description=models.TextField()

    buyer_gender_options=[
        ("male","male"),
        ("female","female")
    ]

    buyer_gender=models.CharField(max_length=30,choices=buyer_gender_options,default="male")

    price=models.PositiveIntegerField()

    buy_date=models.DateField()

    picture=models.ImageField(upload_to="mobile-images",null=True)


   


