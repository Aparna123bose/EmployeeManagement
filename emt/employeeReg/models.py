from django.db import models

# Create your models here.
class Position(models.Model):
    Title = models.CharField(max_length=50)

    def __str__(self):
        return  self.Title

class Employee(models.Model):
    Full_Name = models.CharField(max_length=100)
    Emp_Code = models.CharField(max_length=50)
    Moblie = models.CharField(max_length=50)
    Position = models.ForeignKey(Position,on_delete=models.CASCADE)