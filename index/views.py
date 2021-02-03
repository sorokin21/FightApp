from django.shortcuts import render, get_object_or_404
from .forms import FighterForm, FightForm
from django.shortcuts import redirect
from .models import Fighter, Zombie
from django.contrib import messages
import random

# Create your views here.
def index(request):
     x = Fighter.objects.all()
     if request.method == "POST":
          form = FighterForm(request.POST)

          if form.is_valid():
               pk = form.cleaned_data['Character']
               x=pk.pk
               return redirect('fighter',pk=x)
     else:
          form = FighterForm()

          return render(request,'index/home.html',{'form':form,'x':x})

def fighter(request, pk):
     fighter = get_object_or_404(Fighter, pk=pk)
     if request.method == "POST":
          form = FightForm(request.POST)

          if form.is_valid():
               k = form.cleaned_data['action']
               print(k)
               if k == '1':
                    enemy=Zombie.objects.all()
                    fighter.cur_health-=random.randint(10,25)
                    print(fighter.cur_health)
                    fighter.save()
                    messages.success(request, 'Three credits remain in your account.')
                    return redirect('fighter',pk=pk)
     else:
          form = FightForm()
     return render(request,'index/fighter.html',{'fighter':fighter,'form':form})

def info(request):
     x = Fighter.objects.all()
     for i in x:
          if i.cur_health < i.health:
               i.cur_health = i.health
               i.save()
     
     return render(request,'index/info.html',{'x':x})


     
