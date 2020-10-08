from django.forms import ModelForm, TextInput
from .models import Usuario

class AltaUsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"
        widgets = {
            'username': TextInput(attrs={
                "placeholder" : "Nombre de usuario de Telegram",                
                "class": "form-control"
            }),
            'api_id': TextInput(attrs={
                "placeholder" : "API_ID de Telegram",                
                "class": "form-control"
            }),
            'api_hash': TextInput(attrs={
                "placeholder" : "API_HASH de Telegram",                
                "class": "form-control"
            })
        }