from django.db import models

# Create your models here.
from django.urls import reverse
class School(models.Model):
    Sname=models.CharField(max_length=100)
    Sprincipal=models.CharField(max_length=100)
    Slocation=models.CharField(max_length=100)

    def __str__(self):
        return self.Sname
    
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

class Student(models.Model):
    Sname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='Students')
    Stname=models.CharField(max_length=100)
    Stage=models.IntegerField()

    def __str__(self):
        return self.Stname