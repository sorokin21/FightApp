from django.db import models

# Create your models here.

class Fighter(models.Model):
     name=models.CharField(max_length=200)
     health=models.IntegerField()
     cur_health=models.IntegerField()
     wins = models.IntegerField(null=True)

     def __str__(self):
          return self.name

class Zombie(models.Model):
     name=models.CharField(max_length=200)
     health=models.IntegerField()
     cur_health=models.IntegerField()

     def __str__(self):
          return self.name
