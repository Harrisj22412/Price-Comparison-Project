from django.db import models
#Created Backend Model Class
# Create your models here.

from django.contrib.auth.models import User

# Create your views here.

class Category(models.Model):
    name = models.CharField(max_length = 225)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.TextField()
    date_created = models.DateTimeField(auto_now_add= True)
    date_updated = models.DateTimeField(auto_now_add= True)
    likes = models.ManyToManyField(User, related_name='blog_post')
    dislikes = models.ManyToManyField(User, related_name='blog_post')

    def __str__(self):
        return self.title