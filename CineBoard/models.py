from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):  
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):  
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    release_date = models.DateField()
    rating = models.FloatField()
    categories = models.ManyToManyField(Category)

    image = models.ImageField(upload_to='movies/', blank=True, null=True)

    def __str__(self):
        return self.title



class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

