from .forms import UserCreationFormWithOtherFields
from django.views.generic import ListView, CreateView, TemplateView, UpdateView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from .models import User, Seguidores
from django.shortcuts import render

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

def userDelete(request, userId):
    userdel = User.objects.get(identificacion=userId)
    userdel.delete()
    results = User.objects.all()
    return render(request, 'core/home.html', {"user": results})

def SeguirUsuarioView(request, user_id):
    seguidor = User.objects.get(id=request.user.id)
    usuario_seguido = User.objects.get(id=user_id)
    nuevo_seguidor = Seguidores(usuario_seguido=usuario_seguido, seguidor=seguidor)
    nuevo_seguidor.save()
    return HttpResponseRedirect(reverse('blogs:list_all_blogs'))

class VerSiguiendoView(ListView):
    model = Seguidores
    template_name = 'registration/siguiendo.html'
    context_object_name = 'siguiendo'

    def get_queryset(self):
        return self.model.objects.filter(seguidor=self.request.user)

class VerSeguidoresView(ListView):
    model = Seguidores
    template_name = 'registration/seguidores.html'
    context_object_name = 'seguidores'

    def get_queryset(self):
        return self.model.objects.filter(usuario_seguido=self.request.user)
