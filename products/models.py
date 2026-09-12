from django.db import models


class Produit(models.Model):
    nom = models.CharField(max_length=150)
    unite = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    actif = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom


class Stock(models.Model):
    producteur = models.ForeignKey(
        'producers.Producteur',
        on_delete=models.CASCADE,
        related_name='stocks'
    )

    produit = models.ForeignKey(
        Produit,
        on_delete=models.CASCADE,
        related_name='stocks'
    )

    quantite = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    # Prix payé au producteur
    prix_unitaire = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    # Prix vendu au supermarché
    prix_supermarche = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    # Prix vendu au particulier
    prix_particulier = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    date_ajout = models.DateTimeField(auto_now_add=True)

    actif = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.produit} - {self.producteur}"