from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Genre(models.Model):
    name = models.TextField()


class Movie(models.Model):      
    title = models.TextField()
    original_title = models.TextField()
    overview = models.TextField()
    # M:N
    genres = models.ManyToManyField(Genre)
    
    poster_path = models.TextField()
    backdrop_path = models.TextField()
    vote_average = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    vote_count = models.IntegerField(validators=[MinValueValidator(0)])
    release_date = models.TextField()
    runtime = models.IntegerField(validators=[MinValueValidator(0)])
    popularity = models.FloatField(validators=[MinValueValidator(0)])
    adult = models.BooleanField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movies", symmetrical=True)
    
class Comment(models.Model):    
    content = models.TextField() 
    
    # 외래키
    user =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    # M:N
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_comments", symmetrical=True)
    # M:N
    movie =  models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="comments")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
       