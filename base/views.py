from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *
# Create your views here.
def index(request):
    cards = Cards.objects.all()

    form = CardsForm()

    if request.method == 'POST':
        form = CardsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'cards':cards, 'form':form}
    return render(request, 'base/cards_list.html', context)
def updateCard(request, pk):
    card = Cards.objects.get(cardID=pk)

    form = CardsForm(instance=card)

    if request.method == 'POST':
        form = CardsForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'base/update_card.html', context)

def deleteCard(request, pk):
    item = Cards.objects.get(cardID=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'base/delete.html', context)