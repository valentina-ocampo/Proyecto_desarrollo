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
            'genre',
            'identification',
            'telephone',
            'country',
            'city',
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
        self.fields['identification'].widget.attrs['placeholder'] = 'Identificación'
        self.fields['telephone'].widget.attrs['placeholder'] = 'Teléfono'
        self.fields['country'].widget.attrs['placeholder'] = 'País'
        self.fields['city'].widget.attrs['placeholder'] = 'Ciudad'
