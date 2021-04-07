from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

# Create your forms here.

class UserCreationFormWithOtherFields(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'foto_perfil',
            'username',
            'email',
            'first_name',
            'last_name',
            'genero',
            'identificacion',
            'telefono',
            'pais',
            'ciudad',
        ]

    def __init__(self, *args, **kwargs):
        super(UserCreationFormWithOtherFields, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field is not 'foto_perfil':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control mb-2'
                })
        
        self.fields['username'].widget.attrs.update({'placeholder': 'Nombre de usuario'})
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password2'].widget.attrs['placeholder'] = 'Repite la contraseña'
        self.fields['email'].widget.attrs['placeholder'] = 'Correo electrónico'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Nombre'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Apellido'
        self.fields['identificacion'].widget.attrs['placeholder'] = 'Identificación'
        self.fields['telefono'].widget.attrs['placeholder'] = 'Teléfono'
        self.fields['pais'].widget.attrs['placeholder'] = 'País'
        self.fields['ciudad'].widget.attrs['placeholder'] = 'Ciudad'
