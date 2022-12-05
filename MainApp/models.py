from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# table Topic(entity) with fields text and date_added
class Topic(models.Model):
    
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    #User is an internally maintained table
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    #to return the text eg: chess if text had chess 
    def __str__(self):
        return self.text

class Entry(models.Model):
    #CONNECT , same as foreign key concept , Topic is object not element
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    #since it automatically adds s to the name like Topic --> Topics
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}..."
   


