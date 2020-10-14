from django.forms import ModelForm, TextInput, Select
from .models import Usuario, Group, Contact

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
        fields = ["name", "career", "comision"]
        career_choices = (
            (1, 'Ingeniería en sistemas de información'),
            (2, 'Ingeniería mecánica'),
            (3, 'Ingeniería eléctrica'),
            (4, 'Ingeniería industrial'),
            (5, 'Ingeniería química'),
            (6, 'Ingeniería civil')
        )
        widgets = {
            'name': TextInput(attrs={
                "placeholder" : "",                
                "class": "form-control"
            }),
            'career': Select(choices=career_choices, attrs={'class': 'form-control'}),
            'comision': TextInput(attrs={
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
                "placeholder" : "Nombre de Usurario de Telegram",
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

