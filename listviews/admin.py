from django.contrib import admin
from listviews.models import Category, Book


# Register your models here.bookview

class Categoryadmin(admin.ModelAdmin):
    list_display = ['name', 'shelf_no']

class Bookadmin(admin.ModelAdmin):
    list_display = ['b_name', 'author', 'category']

admin.site.register(Category, Categoryadmin)
admin.site.register(Book, Bookadmin)
