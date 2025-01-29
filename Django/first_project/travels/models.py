from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Destination(models.Model):
    city_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    
    def __str__(self):
        return self.city_name


class Destination_deatils(models.Model):
    areas = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='details')
    area_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    area_desc = RichTextField(null=True, blank=True)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
     
    def __str__(self):
        return self.area_name
    
    
class Comments(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
     destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='comments')
     content = RichTextField()
     created_at = models.DateTimeField(auto_now_add=True)
     
     def __str__(self):
        return self.user.username
    