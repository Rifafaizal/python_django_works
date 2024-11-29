from django.db import models

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=200)
    # genre_options=(
    #     ("action","action"),
    #     ("romantic","romantic"),
    #     ("horror","horror")
    # )
    # genre_type=models.CharField(max_length=100,choices=genre_options,default="action")
    genre=models.CharField(max_length=200)
    runtime=models.PositiveIntegerField()
    language=models.CharField(max_length=100)
    year=models.PositiveIntegerField()
    director=models.CharField(max_length=100)
    actor=models.CharField(max_length=100)
    picture=models.ImageField(upload_to="movie_images",null=True)

    def __str__(self):
        return self.title



    

