from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class InscriptionForm(UserCreationForm):

    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'role',
            'password1',
            'password2',
        ]

        widgets = {

            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Entrez votre nom d'utilisateur",
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Entrez votre adresse email',
                }
            ),

            'role': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # Mot de passe
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Entrez votre mot de passe',
        })

        # Confirmation du mot de passe
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirmez votre mot de passe',
        })