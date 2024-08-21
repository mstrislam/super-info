
from django.db import models

class Hashtags(models.Model):
   title = models.CharField(max_length=255)

class Category(models.Model):
   title = models.CharField(max_length=255)

class Publications(models.Model):

   category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='publication', null=True)
   hashtags = models.ManyToManyField(Hashtags, related_name='publication')
   title = models.CharField(max_length=255)
   short_description = models.TextField(null=True)
   description = models.TextField()
   img = models.ImageField(null=True)
   datetime = models.DateField()
   is_active = models.BooleanField(default=True)



class Contacts(models.Model):


   name = models.CharField(max_length=255)
   email = models.EmailField()
   subject = models.TextField()
   message = models.TextField()