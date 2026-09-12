from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.liste_producteurs,
        name='liste_producteurs'
    ),

    path(
        'ajouter/',
        views.ajouter_producteur,
        name='ajouter_producteur'
    ),

    path(
    'modifier/<int:id>/',
    views.modifier_producteur,
    name='modifier_producteur'
),

path(
    'statut/<int:id>/',
    views.changer_statut_producteur,
    name='changer_statut_producteur'
),
]