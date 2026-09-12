from django.contrib import admin
from .models import Produit, Stock


@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):

    list_display = (
        'nom',
        'unite',
        'actif',
        'date_creation',
    )

    list_filter = (
        'actif',
    )

    search_fields = (
        'nom',
    )


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):

    list_display = (
        'produit',
        'producteur',
        'quantite',
        'prix_unitaire',
        'prix_supermarche',
        'prix_particulier',
        'actif',
        'date_ajout',
    )

    list_filter = (
        'actif',
        'produit',
    )

    search_fields = (
        'produit__nom',
    )