from django.contrib import admin
from .models import Fighter, Zombie, Weapon
# Register your models here.
admin.site.register(Fighter)
admin.site.register(Zombie)
admin.site.register(Weapon)