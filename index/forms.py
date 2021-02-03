from django import forms
from .models import Fighter



class FighterForm(forms.Form):


     Character = forms.ModelChoiceField(queryset=Fighter.objects.all()) 

     def __init__(self, *args, **kwargs):
        super(FighterForm, self).__init__(*args, **kwargs)

class FightForm(forms.Form):

     CHOICES = (
        ('1', 'Start a fight'),
        ('2', 'Run away'),
     )
     action = forms.ChoiceField(choices=CHOICES,widget=forms.Select())

     def __init__(self, *args, **kwargs):
          super(FightForm, self).__init__(*args, **kwargs)


