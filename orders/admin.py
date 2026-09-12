from django.contrib import admin
from .models import Commande, LigneCommande


class LigneCommandeInline(admin.TabularInline):
    model = LigneCommande
    extra = 0


@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'client',
        'date_commande',
        'statut',
        'total',
    )

    list_filter = (
        'statut',
        'date_commande',
    )

    search_fields = (
        'client__username',
    )

    inlines = [
        LigneCommandeInline,
    ]


@admin.register(LigneCommande)
class LigneCommandeAdmin(admin.ModelAdmin):

    list_display = (
        'commande',
        'stock',
        'quantite',
        'prix_unitaire',
        'sous_total',
    )