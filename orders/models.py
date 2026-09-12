from django.db import models

from django.db import models
from django.conf import settings
from products.models import Stock


class Commande(models.Model):

    STATUT_CHOICES = (
        ('EN_ATTENTE', 'En attente'),
        ('CONFIRMEE', 'Confirmée'),
        ('EN_PREPARATION', 'En préparation'),
        ('EN_LIVRAISON', 'En livraison'),
        ('LIVREE', 'Livrée'),
        ('ANNULEE', 'Annulée'),
    )

    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='commandes'
    )

    date_commande = models.DateTimeField(
        auto_now_add=True
    )

    statut = models.CharField(
        max_length=30,
        choices=STATUT_CHOICES,
        default='EN_ATTENTE'
    )

    adresse_livraison = models.TextField()

    total = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    

    def __str__(self):
        return f"Commande #{self.id} - {self.client.username}"


class LigneCommande(models.Model):

    commande = models.ForeignKey(
        Commande,
        on_delete=models.CASCADE,
        related_name='lignes'
    )

    stock = models.ForeignKey(
        Stock,
        on_delete=models.PROTECT,
        related_name='lignes_commandes'
    )

    quantite = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    prix_unitaire = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    sous_total = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.stock.produit.nom} - {self.quantite}"