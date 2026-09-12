from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Producteur
from .forms import ProducteurForm


@login_required
def liste_producteurs(request):

    producteurs = Producteur.objects.all().order_by('-date_creation')

    return render(
        request,
        'producers/liste.html',
        {
            'producteurs': producteurs
        }
    )


@login_required
def ajouter_producteur(request):

    if request.method == 'POST':

        form = ProducteurForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('liste_producteurs')

    else:

        form = ProducteurForm()

    return render(
        request,
        'producers/ajouter.html',
        {
            'form': form
        }
    )
@login_required
def modifier_producteur(request, id):

    producteur = Producteur.objects.get(id=id)

    if request.method == 'POST':

        form = ProducteurForm(
            request.POST,
            instance=producteur
        )

        if form.is_valid():
            form.save()
            return redirect('liste_producteurs')

    else:

        form = ProducteurForm(
            instance=producteur
        )

    return render(
        request,
        'producers/modifier.html',
        {
            'form': form,
            'producteur': producteur
        }
    )

@login_required
def changer_statut_producteur(request, id):

    producteur = Producteur.objects.get(id=id)
    producteur.actif = not producteur.actif
    producteur.save()

    return redirect('liste_producteurs')