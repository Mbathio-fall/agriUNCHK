from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views 


urlpatterns = [
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.ConnexionView.as_view(), name='login'),
    path('deconnexion/',LogoutView.as_view(),name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('particulier/dashboard/',views.dashboard,name='particulier_dashboard'),
    path('supermarche/dashboard/',views.dashboard,name='supermarche_dashboard'),
    path('producteur/dashboard/',views.dashboard,name='producteur_dashboard'),

path(
    'utilisateurs/',
    views.liste_utilisateurs,
    name='liste_utilisateurs'
),

path(
    'utilisateurs/<int:user_id>/statut/',
    views.changer_statut_utilisateur,
    name='changer_statut_utilisateur'
),

path(
    'supermarches/',
    views.liste_supermarches,
    name='liste_supermarches'
),

path(
    'particuliers/',
    views.liste_particuliers,
    name='liste_particuliers'
),

path(
    'profil/',
    views.profil,
    name='profil'
),
]