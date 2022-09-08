from importlib.resources import contents
from django.db import models
from django.urls import  reverse
from django.contrib.auth.models import User

# Create your models here.


class ExampleModel(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    # img = models.ImageField(upload_to='post/')


    


    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
    
    def get_del_url(self):
        return reverse('delete', kwargs={'pk': self.pk})