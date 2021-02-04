from django import forms
from .models import Fighter



class FighterForm(forms.Form):


     Character = forms.ModelChoiceField(queryset=Fighter.objects.all()) 

     def __init__(self, *args, **kwargs):
        super(FighterForm, self).__init__(*args, **kwargs)

class FightForm(forms.Form):

     CHOICES = (
        ('1', 'Increase HP'),
        ('2', 'Increase DMG'),
     )
     action = forms.ChoiceField(choices=CHOICES,widget=forms.Select())

     def __init__(self, *args, **kwargs):
          super(FightForm, self).__init__(*args, **kwargs)

class RoundForm(forms.Form):

     CHOICES = (
        ('1', 'High kick'),
        ('2', 'Low kick'),
     )
     action = forms.ChoiceField(choices=CHOICES,widget=forms.Select())

     def __init__(self, *args, **kwargs):
          super(RoundForm, self).__init__(*args, **kwargs)

