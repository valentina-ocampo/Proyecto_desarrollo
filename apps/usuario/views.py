from .forms import UserCreationFormWithOtherFields
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import User

# Create your views here.


class SignUpView(CreateView):
    form_class = UserCreationFormWithOtherFields
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('core:home')

    def get_success_url(self):
        messages.success(self.request, 'Usuario creado satisfactoriamente.')
        return super().get_success_url()

class UserDetailView(TemplateView):
    template_name = 'registration/user_detail.html'

class UserEditView(UpdateView):
    model = User
    form_class = UserCreationFormWithOtherFields
    template_name = 'registration/user_update_form.html'
    success_url = reverse_lazy('core:home')

    def get_success_url(self):
        messages.success(self.request, 'Usuario actualizado satisfactoriamente.')
        return super().get_success_url()
