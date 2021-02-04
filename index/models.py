from django.db import models
from PIL import Image
# Create your models here.

class Weapon(models.Model):
     name = models.CharField(max_length=200, help_text='Enter a name (e.g. Club)')
     damage=models.IntegerField(default=1,null=True)
     def __str__(self):
          return self.name

class Fighter(models.Model):
     name=models.CharField(max_length=200)
     health=models.IntegerField()
     cur_health=models.IntegerField()
     damage=models.IntegerField(null=True)
     wins = models.IntegerField(null=True)
     skills = models.IntegerField(default=0,null=True)
     weapon = models.ManyToManyField(Weapon, help_text='Select a weapon for this fighter.')
     w_bool = models.BooleanField(default=False)

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