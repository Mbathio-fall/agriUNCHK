from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Stock
from orders.models import Commande, LigneCommande

from .models import Produit
from .form import ProduitForm, StockForm


@login_required
def catalogue(request):

    stocks = Stock.objects.filter(
        actif=True,
        produit__actif=True,
        quantite__gt=0
    ).select_related(
        'produit',
        'producteur'
    )

    return render(
        request,
        'products/catalogue.html',
        {
            'stocks': stocks
        }
    )






@login_required
def commander(request, stock_id):

    if request.user.role not in ['PARTICULIER', 'SUPERMARCHE']:
        return redirect('dashboard')

    stock = get_object_or_404(
        Stock,
        id=stock_id,
        actif=True,
        produit__actif=True
    )

    if request.method == 'POST':

        quantite = request.POST.get('quantite')
        adresse_livraison = request.POST.get('adresse_livraison')

        if not adresse_livraison:
          return render(request,'products/commander.html',
        {
            'stock': stock,
            'erreur': 'Veuillez indiquer une adresse de livraison.'
        }
    )

        if not quantite:
            return render(
                request,
                'products/commander.html',
                {
                    'stock': stock,
                    'erreur': 'Veuillez indiquer une quantité.'
                }
            )

        try:
            quantite = float(quantite)
        except ValueError:
            return render(
                request,
                'products/commander.html',
                {
                    'stock': stock,
                    'erreur': 'La quantité doit être un nombre.'
                }
            )

        if quantite <= 0:
            return render(
                request,
                'products/commander.html',
                {
                    'stock': stock,
                    'erreur': 'La quantité doit être supérieure à zéro.'
                }
            )

        if quantite > float(stock.quantite):
            return render(
                request,
                'products/commander.html',
                {
                    'stock': stock,
                    'erreur': 'La quantité demandée dépasse le stock disponible.'
                }
            )

        if request.user.role == 'SUPERMARCHE':
            prix = stock.prix_supermarche

        else:
            prix = stock.prix_particulier

        if prix is None:
            return render(
                request,
                'products/commander.html',
                {
                    'stock': stock,
                    'erreur': 'Le prix de ce produit n’est pas encore disponible.'
                }
            )

        sous_total = quantite * float(prix)

        commande = Commande.objects.create(
         client=request.user,
         adresse_livraison=adresse_livraison,
         total=sous_total
        )

        LigneCommande.objects.create(
            commande=commande,
            stock=stock,
            quantite=quantite,
            prix_unitaire=prix,
            sous_total=sous_total
        )
        stock.quantite = quantite
        stock.save()
        
        return redirect(
            'commande_detail',
            commande_id=commande.id
        )

    return render(
        request,
        'products/commander.html',
        {
            'stock': stock
        }
    )

@login_required
def commande_detail(request, commande_id):

    commande = get_object_or_404(
        Commande,
        id=commande_id,
        client=request.user
    )

    return render(
        request,
        'products/commande_detail.html',
        {
            'commande': commande
        }
    )










@login_required
def mes_commandes(request):

    if request.user.role not in ['PARTICULIER', 'SUPERMARCHE']:
        return redirect('dashboard')

    commandes = Commande.objects.filter(
        client=request.user
    ).prefetch_related(
        'lignes__stock__produit'
    ).order_by('-date_commande')

    return render(
        request,
        'products/mes_commandes.html',
        {
            'commandes': commandes
        }
    )





@login_required
@login_required
def liste_produits(request):

    if request.user.role == 'PRODUCTEUR':
        produits = Produit.objects.filter(
            stocks__producteur=request.user.producteur
        ).distinct().order_by('-date_creation')

    else:
        produits = Produit.objects.all().order_by('-date_creation')

    return render(
        request,
        'products/liste.html',
        {
            'produits': produits
        }
    )


@login_required
def ajouter_produit(request):

    if request.method == 'POST':

        form = ProduitForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('liste_produits')

    else:

        form = ProduitForm()

    return render(
        request,
        'products/ajouter.html',
        {
            'form': form
        }
    )

#=========================
# STOCKS
# =========================

@login_required
@login_required
def liste_stocks(request):

    if request.user.role == 'PRODUCTEUR':
        stocks = Stock.objects.filter(
            producteur=request.user.producteur
        ).select_related(
            'producteur',
            'produit'
        ).order_by('-date_ajout')

    else:
        stocks = Stock.objects.select_related(
            'producteur',
            'produit'
        ).order_by('-date_ajout')

    return render(
        request,
        'products/stocks.html',
        {
            'stocks': stocks
        }
    )


@login_required
def ajouter_stock(request):

    if request.method == 'POST':

        form = StockForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('liste_stocks')

    else:
        form = StockForm()

    return render(
        request,
        'products/ajouter_stock.html',
        {
            'form': form
        }
    )


@login_required
def modifier_stock(request, id):

    stock = get_object_or_404(Stock, id=id)

    if request.method == 'POST':

        form = StockForm(
            request.POST,
            instance=stock
        )

        if form.is_valid():
            form.save()
            return redirect('liste_stocks')

    else:

        form = StockForm(
            instance=stock
        )

    return render(
        request,
        'products/modifier_stock.html',
        {
            'form': form,
            'stock': stock
        }
    )


@login_required
def changer_statut_stock(request, id):

    stock = get_object_or_404(Stock, id=id)

    stock.actif = not stock.actif
    stock.save()

    return redirect('liste_stocks')

@login_required
def supprimer_stock(request, id):

    stock = get_object_or_404(Stock, id=id)

    if request.method == 'POST':
        stock.delete()
        return redirect('liste_stocks')

    return render(
        request,
        'products/confirmer_suppression_stock.html',
        {
            'stock': stock
        }
    )


@login_required
def catalogue_particulier(request):

    stocks = Stock.objects.filter(
        actif=True,
        produit__actif=True,
        quantite__gt=0,
        prix_particulier__isnull=False
    ).select_related(
        'produit',
        'producteur'
    )

    return render(
        request,
        'products/catalogue_particulier.html',
        {
            'stocks': stocks
        }
    )


@login_required
def catalogue_supermarche(request):

    stocks = Stock.objects.filter(
        actif=True,
        produit__actif=True,
        quantite__gt=0,
        prix_supermarche__isnull=False
    ).select_related(
        'produit',
        'producteur'
    )

    return render(
        request,
        'products/catalogue_supermarche.html',
        {
            'stocks': stocks
        }
    )