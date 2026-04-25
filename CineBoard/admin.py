from django.contrib import admin
from .models import Movie, Genre, Category, Comment

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(Comment)
# Register your models here.
