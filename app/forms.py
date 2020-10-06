from django import forms
from .models import Usuario

class AltaUsuarioForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Nombre de usuario de Telegram",                
                "class": "form-control"
            }
        ))
    api_id = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "API_ID de Telegram",                
                "class": "form-control"
            }
        ))
    api_hash = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "API_HASH de Telegram",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = Usuario
        fields = ['username', 'api_id', 'api_hash']