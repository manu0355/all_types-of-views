from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, help_text='Action,friction,drama, romance,etc.,')
    shelf_no = models.BigIntegerField()

    def __str__(self):
        return self.name

class Book(models.Model):
    b_name = models.CharField(max_length = 200)
    author = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null=True)

    def __str__(self):
        return self.b_name


