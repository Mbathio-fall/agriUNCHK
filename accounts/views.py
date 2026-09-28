from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from accounts.models import User
from orders.models import Commande
from producers.models import Producteur
from products.models import Produit, Stock

from .forms import InscriptionForm


def inscription(request):

    if request.method == 'POST':

        form = InscriptionForm(request.POST)

        if form.is_valid():

            user = form.save()

            if user.role == 'PRODUCTEUR':
                Producteur.objects.create(
                    utilisateur=user,
                    nom=user.username,
                    telephone='',
                    localisation=''
                )

            return redirect('login')

    else:

        form = InscriptionForm()

    return render(
        request,
        'accounts/inscription.html',
        {'form': form}
    )
@login_required
def dashboard(request):

    # =====================================
    # ADMINISTRATEUR
    # =====================================

    if request.user.is_superuser or request.user.is_staff:

        nombre_commandes = Commande.objects.count()

        nombre_producteurs = Producteur.objects.count()

        nombre_produits = Produit.objects.count()

        nombre_stocks = Stock.objects.count()

        nombre_supermarches = User.objects.filter(
            role='SUPERMARCHE'
        ).count()

        nombre_particuliers = User.objects.filter(
            role='PARTICULIER'
        ).count()

        commandes_en_attente = Commande.objects.filter(
            statut='EN_ATTENTE'
        ).count()

        commandes_en_livraison = Commande.objects.filter(
            statut='EN_LIVRAISON'
        ).count()

        commandes_preparation = Commande.objects.filter(
            statut='EN_PREPARATION'
        ).count()

        commandes_livrees = Commande.objects.filter(
            statut='LIVREE'
        ).count()

        return render(
            request,
            'accounts/dashboard.html',
            {
                'nombre_commandes': nombre_commandes,
                'nombre_producteurs': nombre_producteurs,
                'nombre_produits': nombre_produits,
                'nombre_stocks': nombre_stocks,
                'nombre_supermarches': nombre_supermarches,
                'nombre_particuliers': nombre_particuliers,

                'commandes_en_attente': commandes_en_attente,
                'commandes_en_livraison': commandes_en_livraison,
                'commandes_preparation': commandes_preparation,
                'commandes_livrees': commandes_livrees,
            }
        )

       # =====================================
    # PARTICULIER
    # =====================================

    if request.user.role == 'PARTICULIER':

        nombre_produits = Stock.objects.filter(
            actif=True,
            produit__actif=True,
            quantite__gt=0,
            prix_particulier__isnull=False
        ).count()

        nombre_commandes = Commande.objects.filter(
            client=request.user
        ).count()

        livraisons_en_cours = Commande.objects.filter(
            client=request.user,
            statut='EN_LIVRAISON'
        ).count()

        return render(
            request,
            'accounts/particulier/dashboard.html',
            {
                'nombre_produits': nombre_produits,
                'nombre_commandes': nombre_commandes,
                'livraisons_en_cours': livraisons_en_cours,
            }
        )

    # =====================================
    # SUPERMARCHÉ
    # =====================================

    if request.user.role == 'SUPERMARCHE':

        nombre_produits: int = Stock.objects.filter(
            actif=True,
            produit__actif=True,
            quantite__gt=0,
            prix_supermarche__isnull=False
        ).count()

        nombre_commandes = Commande.objects.filter(
            client=request.user
        ).count()

        livraisons_en_cours = Commande.objects.filter(
            client=request.user,
            statut='EN_LIVRAISON'
        ).count()

        return render(
            request,
            'accounts/supermarche/dashboard.html',
            {
                'nombre_produits': nombre_produits,
                'nombre_commandes': nombre_commandes,
                'livraisons_en_cours': livraisons_en_cours,
            }
        )

    # =====================================
    # PRODUCTEUR
    # =====================================

    if request.user.role == 'PRODUCTEUR':

        return render(
            request,
            'accounts/producteur/dashboard.html'
        )

    # =====================================
    # SI AUCUN RÔLE
    # =====================================

    return redirect('login')

@login_required
def liste_utilisateurs(request):

    # Seul l'administrateur peut accéder à cette page
    if not request.user.is_staff and not request.user.is_superuser:
        return redirect('dashboard')

    utilisateurs = User.objects.all().order_by('-date_joined')

    return render(
        request,
        'accounts/liste_utilisateurs.html',
        {
            'utilisateurs': utilisateurs
        }
    )

@login_required
def liste_supermarches(request):

    if not request.user.is_staff and not request.user.is_superuser:
        return redirect('dashboard')

    supermarches = User.objects.filter(
        role='SUPERMARCHE'
    ).order_by('-date_joined')

    return render(
        request,
        'accounts/liste_supermarches.html',
        {
            'supermarches': supermarches
        }
    )


@login_required
def liste_particuliers(request):

    if not request.user.is_staff and not request.user.is_superuser:
        return redirect('dashboard')

    particuliers = User.objects.filter(
        role='PARTICULIER'
    ).order_by('-date_joined')

    return render(
        request,
        'accounts/liste_particuliers.html',
        {
            'particuliers': particuliers
        }
    )
@login_required
def changer_statut_utilisateur(request, user_id):

    if not request.user.is_staff and not request.user.is_superuser:
        return redirect('dashboard')

    utilisateur = User.objects.get(id=user_id)

    # Empêcher l'administrateur de désactiver son propre compte
    if utilisateur == request.user:
        return redirect('liste_utilisateurs')

    utilisateur.is_active = not utilisateur.is_active
    utilisateur.save()

    return redirect('liste_utilisateurs')

@login_required
def profil(request):

    return render(
        request,
        'accounts/profil.html'
    )