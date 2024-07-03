from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=False)

class App(models.Model):
    name = models.CharField(max_length=30)
    link = models.CharField(max_length=30)
    category= models.CharField(max_length=30)
    subcategory=models.CharField(max_length=30)
    points=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

"""class Image(models.Model):
    image=models.ImageField(upload_to='images/')
    date = models.DateTimeField( auto_now_add=True)

    class Meta:
        ordering=['-date']

    def __str__(self):
        return str(self.date)"""
    
class Task(models.Model):
    name = models.CharField(max_length=30)
    points=models.IntegerField()
  #  app = models.ForeignKey(App, on_delete=models.CASCADE)
    #image=models.ImageField(upload_to='images/', blank=True, null=True, default='default.jpg' )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    is_approved=models.BooleanField(default=False)

class Image(models.Model):
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/',null=True,blank=True)       
# class Task(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     address = models.CharField(max_length=100)
#     photo = models.ManyToManyField(Image, blank=True)

def nameFile(instance, filename):
    return '/'.join(['images', str(instance.name), filename])





    

    