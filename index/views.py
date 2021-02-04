from django.shortcuts import render, get_object_or_404
from .forms import FighterForm, FightForm, RoundForm
from django.shortcuts import redirect
from .models import Fighter, Zombie, Weapon
from django.contrib import messages
import random

# Create your views here.

def loot(request):
     weapon = Weapon.objects.all()
     fighter = Fighter.objects.get(pk=1)
     y = fighter.weapon.get(pk=4)
     print (y.damage)

     #for i in y:
          #print(i.pk)


     content ={
          'fighter':fighter,
          'weapon':weapon,
     }
     return render(request,'index/loot.html',content)



def index(request):
     x = Fighter.objects.get(pk=1)
     if request.method == "POST":
          form = FightForm(request.POST)

          if form.is_valid():
               pk = form.cleaned_data['action']
               print (pk)
               if x.skills != 0:
                    x.skills -= 1
                    if pk == '1':
                         x.health += 5
                         x.save()
                         return redirect('index_home')
                    else:
                         x.damage +=2
                         x.save()
                         return redirect('index_home')
               else:
                    return redirect('fighter',1)
               
     else:
          form = FightForm()


          return render(request,'index/home.html',{'form':form,'x':x})

def fighter(request, pk):
     fighter = get_object_or_404(Fighter, pk=pk)
     if request.method == "POST":
          return redirect('round')

     return render(request,'index/fighter.html',{'fighter':fighter})
def round(request):
     fighter = Fighter.objects.get(pk=1)
     y = Zombie.objects.get(pk=1)
     num = random.randint(1,3)
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
                    if num == 2:
                         fighter.w_bool = True
                         messages.info(request, 'DeadWalker lost a knife')
                         messages.info(request, 'Ohh no there one more on you way!')
                         fighter.save()

                         return redirect('round')
               elif k == '1':
                    messages.success(request, 'Nice high kick')
               elif k == '2':
                    messages.success(request, 'Wow! What a low kick')

     else:
          form = RoundForm()
     return render(request,'index/round.html',{'fighter':fighter,'form':form,'y':y})
def info(request):
     weapon = Weapon.objects.all()
     fighter = Fighter.objects.get(pk=1)
     y=0
     for i in weapon:
          y=i
     
     fighter.cur_health=fighter.health
     fighter.save()
     content ={
          'fighter':fighter,
          'weapon':weapon,
          'y':y
     }
     
     return render(request,'index/info.html',content)

def lost(request):
     fighter = Fighter.objects.get(pk=1)
     fighter.w_bool = False
     fighter.skills += 1
     fighter.save()
     messages.info(request, 'You lost a knife')
     return render(request,'index/lost.html',{'fighter':fighter})


     
