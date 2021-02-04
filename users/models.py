from django.db import models
from PIL import Image
from index import models as index_models


# Create your models here.
class Profile(models.Model):
     fighter = models.OneToOneField(index_models.Fighter, on_delete=models.CASCADE)
     image = models.ImageField(default='default.jpg',upload_to='profile_pics')

     def __str__(self):
          return f'{self.fighter.name} Profile'
     
     def save(self, *args, **kwargs):
          super(Profile, self).save(*args, **kwargs)

          img = Image.open(self.image.path)

          if img.height > 400 or img.width > 400:
               output_size = (400, 400)
               img.thumbnail(output_size)
               img.save(self.image.path)