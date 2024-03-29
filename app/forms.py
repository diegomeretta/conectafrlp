from django.forms import ModelForm, TextInput, Select, SelectMultiple, Textarea
from .models import Usuario, Group, Contact, Message

class AltaUsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ["api_id", "api_hash", "phone", "telegram_id"]
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
            }),
            'telegram_id': TextInput(attrs={
                "placeholder" : "ID de Telegram del usuario",
                "class": "form-control"
            })
        }

class AltaGrupoForm(ModelForm):
    class Meta:
        model = Group
        fields = ["name", "career", "commission", "subject", "contacts"]
        widgets = {
            'name': TextInput(attrs={
                "placeholder" : "",
                "class": "form-control"
            }),
            'career': Select(attrs={
                "class": "form-control"
            }),
            'commission': Select(attrs={
                "class": "form-control"
            }),
            'subject': Select(attrs={
                "placeholder" : "",
                "class": "form-control"
            }),
            'contacts': SelectMultiple(attrs={
                "placeholder" : "",
                "class": "form-control"
            })
        }

    def __init__(self, *args, **kwargs):
        super(AltaGrupoForm, self).__init__(*args, **kwargs)
        self.fields['contacts'].queryset = Contact.objects.filter(contact_rol_id=1)

class EditGroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ["current_year", "career", "commission", "subject", "contacts"]
        widgets = {
            'current_year': TextInput(attrs={
                "class": "form-control"
            }),
            'career': Select(attrs={
                "class": "form-control"
            }),
            'commission': Select(attrs={
                "class": "form-control"
            }),
            'subject': Select(attrs={
                "class": "form-control"
            }),
            'contacts': SelectMultiple(attrs={
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

class EditContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["first_name", "last_name", "contact_rol"]
        widgets = {
            'first_name': TextInput(attrs={
                "class": "form-control"
            }),
            'last_name': TextInput(attrs={
                "class": "form-control"
            }),
            'contact_rol': Select(attrs={
                "class": "form-control"
            })
        }

class SendMessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["text_message", "group"]
        widgets = {
            'text_message': Textarea(attrs={
                "class": "form-control"
            }),
            'group': Select(attrs={
                "class": "form-control"
            })
        }