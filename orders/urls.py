from django.urls import path
from . import views


urlpatterns = [

    path(
        'commandes/',
        views.liste_commandes,
        name='liste_commandes'
    ),

    path(
    'commandes/<int:commande_id>/statut/',
    views.modifier_statut_commande,
    name='modifier_statut_commande'
),

path(
    'livraisons/',
    views.livraisons,
    name='livraisons'
),

path('mes-ventes/', views.mes_ventes, name='mes_ventes'),

]