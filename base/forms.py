from django import forms
from django.forms import ModelForm

from .models import *

class CardsForm(forms.ModelForm):
    cards = Cards.objects.all()
    
    class Meta:
        model = Cards
        fields = '__all__'
