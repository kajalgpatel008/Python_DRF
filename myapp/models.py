from django.db import models

# Create your models here.
class Speaker(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    description=models.CharField(max_length=100,blank=True,null=True)
    photo=models.ImageField(upload_to='pics',blank=True,null=True)
    
    def __str__(self):
        return self.name

class Event(models.Model):
    title=models.CharField(max_length=100,blank=True,null=True)
    desc=models.CharField(max_length=100,blank=True,null=True)
    event_date=models.DateTimeField(blank=True,null=True)
    
    def __str__(self):
        return self.title

