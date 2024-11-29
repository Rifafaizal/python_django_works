from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone=models.CharField(max_length=20,unique=True)


class Expense(models.Model):


    category_options=(

                        # (None,"select")
        
                        ("food","food"),

                        ("travel","travel"),

                        ("entertainment","entertainment"),

                        ("ride","ride"),

                        ("health","health"),
    
            )


    payment_options=(
                        # (None,"select"),

                        ("card","card"),
                        ("cash","cash"),
                        ("UPI","UPI"),

    ) 



                        


    title=models.CharField(max_length=100)  
 

    
    category=models.CharField(max_length=200,choices=category_options,default="food") 

    amount=models.PositiveIntegerField()

    payment=models.CharField(max_length=10,choices=payment_options,default="card")

    create_at=models.DateTimeField(auto_now_add=True)

    updated_at=models.DateTimeField(auto_now=True)

    owner=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title




