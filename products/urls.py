from django.urls import path
from . import views


urlpatterns = [
    path('catalogue/', views.catalogue, name='catalogue'),

    path('commander/<int:stock_id>/',views.commander,name='commander'),
    path('commande/<int:commande_id>/',views.commande_detail,name='commande_detail'),
    path(
    'mes-commandes/',
    views.mes_commandes,
    name='mes_commandes'
),


path(
        '',
        views.liste_produits,
        name='liste_produits'
    ),

    path(
        'ajouter/',
        views.ajouter_produit,
        name='ajouter_produit'
    ),


    # Stocks

    path(
        'stocks/',
        views.liste_stocks,
        name='liste_stocks'
    ),

    path(
        'stocks/ajouter/',
        views.ajouter_stock,
        name='ajouter_stock'
    ),

    path(
        'stocks/modifier/<int:id>/',
        views.modifier_stock,
        name='modifier_stock'
    ),

    path(
        'stocks/statut/<int:id>/',
        views.changer_statut_stock,
        name='changer_statut_stock'
    ),

    path(
    'catalogue/particulier/',
    views.catalogue_particulier,
    name='catalogue_particulier'
),


path(
    'catalogue/supermarche/',
    views.catalogue_supermarche,
    name='catalogue_supermarche'
),


path(
    'stocks/supprimer/<int:id>/',
    views.supprimer_stock,
    name='supprimer_stock'
),
]