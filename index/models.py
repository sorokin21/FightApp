from django.db import models
from PIL import Image
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
     image = models.ImageField(default='default.jpg',upload_to='profile_pics')

     def __str__(self):
          return self.name

     def save(self, *args, **kwargs):
          super(Zombie, self).save(*args, **kwargs)

          img = Image.open(self.image.path)

          if img.height > 400 or img.width > 400:
               output_size = (400, 400)
               img.thumbnail(output_size)
               img.save(self.image.path)