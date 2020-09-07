from django import forms
from .models import ChatGroup

class ChatGroupForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Chat Group Name",                
                "class": "form-control"
            }
        ))
    user_chat1 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Usuario",                
                "class": "form-control"
            }
        ))
    user_chat2 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Usuario",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = ChatGroup
        fields = ['name', 'user_chat1', 'user_chat2']
