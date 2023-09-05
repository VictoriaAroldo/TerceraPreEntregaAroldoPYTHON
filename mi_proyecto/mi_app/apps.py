from django.apps import AppConfig


class MiAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mi_app'





from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

