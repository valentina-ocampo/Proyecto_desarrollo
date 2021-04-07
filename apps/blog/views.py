from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Blog, Favoritos
from ..usuario.models import User
from .forms import BlogForm

# Create your views here.


class ListBlogsView(ListView):
    model = Blog
    template_name = 'blog/blogs.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.filter(usuario=self.request.user)


class ListAllBlogsView(ListView):
    model = Blog
    template_name = 'blog/blogs_all.html'
    context_object_name = 'blogs'

class CreateBlogView(CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blogs:list_blogs')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        messages.success(self.request, 'Blog creado satisfactoriamente.')
        return super(CreateBlogView, self).form_valid(form)


class DetailBlogView(DetailView):
    model = Blog
    template_name = 'blog/blog.html'


class UpdateBlogView(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('blogs:list_blogs')

    def get_success_url(self):
        messages.success(self.request, 'Blog actualizado satisfactoriamente.')
        return super().get_success_url()


class DeleteBlogView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs:list_blogs')

    def get_success_url(self):
        messages.success(self.request, 'Blog eliminado satisfactoriamente.')
        return super().get_success_url()


def CreateFavoritosView(request, blog_id):
    usuario = User.objects.get(pk=request.user.id)
    blog = Blog.objects.get(pk=blog_id)
    nuevo_favorito = Favoritos(usuario=usuario, pagina=blog)
    nuevo_favorito.save()
    return HttpResponseRedirect(reverse('blogs:list_all_blogs'))


class ListFavoritosView(ListView):
    model = Favoritos
    template_name = 'blog/favoritos.html'
    context_object_name = 'favoritos'

