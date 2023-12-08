
from django.shortcuts import render, redirect
from .models import Voiture , VoitureForm
from django.contrib.auth import logout

# Create your views here.
def liste_voitures(request):
        voitures = Voiture.objects.all()
        return render(request, 'liste_voitures.html', {'voitures': voitures})

def ajouter_voiture(request):
    if request.method == 'POST':
        form = VoitureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('liste_voitures')
    else:
        form = VoitureForm()

    context = {
        'form': form,
    }
    return render(request, 'ajouter_voiture.html', context)
