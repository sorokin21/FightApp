from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProfileUpdateForm
from index import models as index_models
from django.contrib.auth.forms import UserCreationForm

def profile(request):
     fighter = index_models.Fighter.objects.get(pk=1)

     context = {
          'fighter' : fighter,
     }
     return render (request, 'users/profile.html', context)

def register(request):
     if request.method == 'POST':
          form = UserCreationForm(request.POST)
          if form.is_valid():
               form.save()
               username = form.cleaned_data.get('username')
               messages.success(request, f'Your account has been created! You are now able to log in!')
               return redirect('login')
     else:
          form = UserCreationForm()
     return render (request,'users/register.html',{'form':form})