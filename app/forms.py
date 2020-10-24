from django.forms import ModelForm, TextInput, Select
from .models import Usuario, Group, Contact, Message

class AltaUsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ["api_id", "api_hash", "phone"]
        widgets = {
            'api_id': TextInput(attrs={
                "placeholder" : "API_ID de Telegram",                
                "class": "form-control"
            }),
            'api_hash': TextInput(attrs={
                "placeholder" : "API_HASH de Telegram",                
                "class": "form-control"
            }),
            'phone': TextInput(attrs={
                "placeholder" : "Número de teléfono asociado a telegram indicando código de país y área",                
                "class": "form-control"
            })
        }

class AltaGrupoForm(ModelForm):
    class Meta:
        model = Group
        fields = ["name", "career", "comision", "subject"]
        widgets = {
            'name': TextInput(attrs={
                "placeholder" : "",                
                "class": "form-control"
            }),
            'career': Select(attrs={
                "class": "form-control"
            }),
            'comision': TextInput(attrs={
                "placeholder" : "",                
                "class": "form-control"
            }),
            'subject': Select(attrs={
                "placeholder" : "",                
                "class": "form-control"
            })
        }

class CreateContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            'name': TextInput(attrs={
                "placeholder" : "Nombre de Usuario de Telegram",
                "class": "form-control"
            }),
            'first_name': TextInput(attrs={
                "placeholder" : "Nombre",
                "class": "form-control"
            }),
            'last_name': TextInput(attrs={
                "placeholder" : "Apellido",
                "class": "form-control"
            }),
            'contact_rol': Select(attrs={
                "placeholder" : "ses",
                "class": "form-control"
            })
        }

class SendMessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["text_message", "id_group"]
        widgets = {
            'text_message': TextInput(attrs={
                "placeholder" : "Mensaje",
                "class": "form-control"
            }),
            'id_group': TextInput(attrs={
                "placeholder" : "id_grupo",
                "class": "form-control"
            })
        }