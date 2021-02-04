from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProfileUpdateForm
from index import models as index_models

def profile(request):
     fighter = index_models.Fighter.objects.get(pk=1)

     context = {
          'fighter' : fighter,
     }
     return render (request, 'users/profile.html', context)