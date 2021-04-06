from django import forms
from .models import Blog

# Create your forms here.


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['titulo', 'contenido']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo'}), 
            'contenido': forms.TextInput(attrs={'class': 'form-control'}), 
        }
