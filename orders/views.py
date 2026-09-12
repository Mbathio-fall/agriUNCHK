from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from producers.models import Producteur

from .models import Commande, LigneCommande


@login_required
def liste_commandes(request):

    if not request.user.is_staff:
        return redirect('dashboard')

    commandes = Commande.objects.all().select_related(
        'client'
    ).prefetch_related(
        'lignes__stock__produit'
    ).order_by('-date_commande')

    return render(request,
    'orders/liste_commandes.html',
    {
        'commandes': commandes,
        'statut_choices': Commande.STATUT_CHOICES
    }
)


@login_required
def modifier_statut_commande(request, commande_id):

    if not request.user.is_staff:
        return redirect('dashboard')

    commande = Commande.objects.get(id=commande_id)

    if request.method == 'POST':

        nouveau_statut = request.POST.get('statut')

        if nouveau_statut in dict(Commande.STATUT_CHOICES):
            commande.statut = nouveau_statut
            commande.save()

    return redirect('liste_commandes')

@login_required
def livraisons(request):

    if request.user.role not in ['PARTICULIER', 'SUPERMARCHE']:
        return redirect('dashboard')

    livraisons = Commande.objects.filter(
        client=request.user,
        statut='EN_LIVRAISON'
    ).prefetch_related(
        'lignes__stock__produit'
    ).order_by('-date_commande')

    return render(
        request,
        'orders/livraisons.html',
        {
            'livraisons': livraisons
        }
    )

@login_required
def mes_ventes(request):

    if request.user.role != 'PRODUCTEUR':
        return redirect('dashboard')

    try:
        producteur = request.user.producteur
    except Producteur.DoesNotExist:
        return redirect('dashboard')

    ventes = LigneCommande.objects.filter(
        stock__producteur=producteur
    ).select_related(
        'commande',
        'commande__client',
        'stock',
        'stock__produit'
    ).order_by(
        '-commande__date_commande'
    )

    return render(
        request,
        'orders/mes_ventes.html',
        {
            'ventes': ventes
        }
    )