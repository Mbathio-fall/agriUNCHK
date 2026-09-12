from django import forms
from .models import Produit


class ProduitForm(forms.ModelForm):

    class Meta:
        model = Produit

        fields = [
            'nom',
            'unite',
            'description',
        ]

        labels = {
            'nom': 'Nom du produit',
            'unite': 'Unité',
            'description': 'Description',
        }

        widgets = {

            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Exemple : Oignon'
            }),

            'unite': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Exemple : kg'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Description du produit'
            }),

        }

        from django import forms
from .models import Produit, Stock


class ProduitForm(forms.ModelForm):

    class Meta:
        model = Produit

        fields = [
            'nom',
            'unite',
            'description',
        ]

        labels = {
            'nom': 'Nom du produit',
            'unite': 'Unité',
            'description': 'Description',
        }

        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Exemple : Oignon'
            }),

            'unite': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Exemple : kg'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),
        }


class StockForm(forms.ModelForm):

    class Meta:
        model = Stock

        fields = [
            'producteur',
            'produit',
            'quantite',
            'prix_unitaire',
            'prix_supermarche',
            'prix_particulier',
        ]

        labels = {
            'producteur': 'Producteur',
            'produit': 'Produit',
            'quantite': 'Quantité disponible',
            'prix_unitaire': "Prix d'achat",
            'prix_supermarche': 'Prix supermarché',
            'prix_particulier': 'Prix particulier',
        }

        widgets = {
            'producteur': forms.Select(attrs={
                'class': 'form-select'
            }),

            'produit': forms.Select(attrs={
                'class': 'form-select'
            }),

            'quantite': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0'
            }),

            'prix_unitaire': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0'
            }),

            'prix_supermarche': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0'
            }),

            'prix_particulier': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0'
            }),
        }