from django.shortcuts import render, get_object_or_404
from .forms import FighterForm, FightForm, RoundForm
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
                    return redirect('round')
               else:
                    enemy=Zombie.objects.all()
                    fighter.cur_health-=random.randint(10,25)
                    if fighter.cur_health <= 0:
                         return redirect('info')

                    else:          
                         print(fighter.cur_health)
                         fighter.save()
                         messages.success(request, 'Three credits remain in your account.')
                         return redirect('fighter',pk=pk)
     else:
          form = FightForm()
     return render(request,'index/fighter.html',{'fighter':fighter,'form':form})
def round(request):
     fighter = Fighter.objects.get(pk=1)
     y = Zombie.objects.get(pk=1)
     if request.method == "POST":
          form = RoundForm(request.POST)
          if form.is_valid():
               k = form.cleaned_data['action']
               y.cur_health-=random.randint(10,35)
               fighter.cur_health-=random.randint(5,30)
               fighter.save()
               y.save()
               if fighter.cur_health <= 0:
                    messages.info(request, 'ooppppsss')
                    return redirect('lost')
               if y.cur_health <= 0:
                    messages.info(request, 'Whoohoo you beated a monster!')
                    fighter.wins +=1
                    fighter.save()
                    y.cur_health = y.health
                    y.save()
                    messages.info(request, 'Ohh no there one more on you way!')

                    return redirect('round')
               elif k == '1':
                    messages.success(request, 'Nice high kick')
               elif k == '2':
                    messages.success(request, 'Wow! What a low kick')

     else:
          form = RoundForm()
     return render(request,'index/round.html',{'fighter':fighter,'form':form,'y':y})
def info(request):
     x = Fighter.objects.all()
     for i in x:
          if i.cur_health < i.health:
               i.cur_health = i.health
               i.save()
     
     return render(request,'index/info.html',{'x':x})

def lost(request):
     fighter = Fighter.objects.get(pk=1)
     return render(request,'index/lost.html',{'fighter':fighter})


     
