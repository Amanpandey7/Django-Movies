from django.contrib import admin
from .models import Movie, Review

class MovieAdmin(admin.ModelAdmin):
    ordering = ['id']
    search_fields = ['name', 'description']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)
# Register your models here.
