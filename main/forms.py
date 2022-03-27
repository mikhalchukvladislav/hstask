from .models import Auth, Code, InviteCode
from django.forms import ModelForm, NumberInput, TextInput


class AuthForm(ModelForm):
    class Meta:
        model = Auth
        fields = ["phone"]
        widgets = {
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+7XXXXXXXXXX',
                'id': 'phone',
            }),
        }


class CodeForm(ModelForm):
    class Meta:
        model = Code
        fields = ["code"]
        widgets = {
            "code": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'XXXX',
                'id': 'code',
            }),
        }


class InviteCodeForm(ModelForm):
    class Meta:
        model = InviteCode
        fields = ["invitecode"]
        widgets = {
            "invitecode": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'XXXXXX',
                'id': 'invitecode',
            }),
        }