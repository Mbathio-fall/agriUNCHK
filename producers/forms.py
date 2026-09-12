from django import forms
from .models import Producteur
from accounts.models import User


class ProducteurForm(forms.ModelForm):

    class Meta:
        model = Producteur

        fields = [
            'utilisateur',
            'nom',
            'telephone',
            'localisation',
        ]

        labels = {
            'utilisateur': 'Compte utilisateur',
            'nom': 'Nom du producteur',
            'telephone': 'Téléphone',
            'localisation': 'Localisation',
        }

        widgets = {
            'utilisateur': forms.Select(attrs={
                'class': 'form-select',
            }),

            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Exemple : Mamadou Ndiaye'
            }),

            'telephone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Exemple : 77 123 45 67'
            }),

            'localisation': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Exemple : Rufisque'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['utilisateur'].queryset = User.objects.filter(
            role='PRODUCTEUR'
        )