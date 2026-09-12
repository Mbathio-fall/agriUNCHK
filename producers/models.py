from django.db import models
from django.conf import settings


class Producteur(models.Model):

    utilisateur = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='producteur'
    )

    nom = models.CharField(max_length=150)

    telephone = models.CharField(max_length=20)

    localisation = models.CharField(max_length=200)

    actif = models.BooleanField(default=True)

    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom