from django.db import models

# Create your models here.

class Branch(models.Model):
    name=models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Result(models.Model):
    roll_number=models.CharField(max_length=20)
    name=models.CharField(max_length=50)
    branch=models.ForeignKey(Branch,on_delete=models.DO_NOTHING)
    year=models.CharField(max_length=20)
    big_data=models.IntegerField(default=0)
    ml=models.IntegerField(default=0)
    dppm=models.IntegerField(default=0)
    stm=models.IntegerField(default=0)
    atcd=models.IntegerField(default=0)
    percentage=models.DecimalField(max_digits=5, decimal_places=2)
    final_result=models.CharField(max_length=4)