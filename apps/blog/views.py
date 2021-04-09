from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Blog, Favoritos
from ..usuario.models import User, Seguidores
from .forms import BlogForm
from django.shortcuts import render

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

    def get(self, request, *args, **kwargs):
        if self.request.user != "AnonymousUser":
            self.extra_context = { "all_favoritos": self.obtener_ids_favoritos(Favoritos.objects.filter(usuario=self.request.user)),
                                   "all_seguidos": self.obtener_ids_seguidos(Seguidores.objects.filter(seguidor=self.request.user))}
            print(self.extra_context)
        print(self.request.user)
        return super().get(request, *args, **kwargs)

    def obtener_ids_favoritos(self, lista_favoritos):
        lista_ids = []
        for favorito in lista_favoritos:
            lista_ids.append(favorito.pagina.id)
        return lista_ids

    def obtener_ids_seguidos(self, lista_seguidos):
        lista_ids = []
        for seguido in lista_seguidos:
            lista_ids.append(seguido.usuario_seguido.id)
        return lista_ids



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
    messages.success(request, f'Agregaste el blog {blog.titulo} a tus favoritos.')
    return HttpResponseRedirect(reverse('blogs:list_all_blogs'))


class ListFavoritosView(ListView):
    model = Favoritos
    template_name = 'blog/favoritos.html'
    context_object_name = 'favoritos'

    def get_queryset(self):
        return self.model.objects.filter(usuario=self.request.user)


class DeleteReportView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs:report_list_blogs')

    def get_success_url(self):
        messages.success(self.request, 'Blog eliminado satisfactoriamente.')
        return super().get_success_url()

def reportBlog(request, blogId):
    blogReport = Blog.objects.get(id=blogId)
    blogReport.reportada = True
    blogReport.save()
    messages.success(request, 'Blog reportado satisfactoriamente')
    return HttpResponseRedirect(reverse('blogs:list_all_blogs'))

def reportListBlog(request):
    blogsReport = Blog.objects.filter(reportada=True)
    return render(request, 'blog_list_report.html', {"blogsReport": blogsReport})


class ListBuscarBlogsView(ListView):
    model = Blog
    template_name = 'blog/blogs_all.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        texto_busqueda = self.request.GET.get('texto_busqueda')
        return self.model.objects.filter(titulo__icontains=texto_busqueda)

    def get(self, request, *args, **kwargs):
        if self.request.user != "AnonymousUser":
            self.extra_context = { "all_favoritos": self.obtener_ids_favoritos(Favoritos.objects.filter(usuario=self.request.user)),
                                   "all_seguidos": self.obtener_ids_seguidos(Seguidores.objects.filter(seguidor=self.request.user))}
            print(self.extra_context)
        print(self.request.user)
        return super().get(request, *args, **kwargs)

    def obtener_ids_favoritos(self, lista_favoritos):
        lista_ids = []
        for favorito in lista_favoritos:
            lista_ids.append(favorito.pagina.id)
        return lista_ids

    def obtener_ids_seguidos(self, lista_seguidos):
        lista_ids = []
        for seguido in lista_seguidos:
            lista_ids.append(seguido.usuario_seguido.id)
        return lista_ids

def DeleteFavoritoView(request, id_blog):
    blog = Blog.objects.get(id=id_blog)
    user = User.objects.get(id=request.user.id)
    favorito = Favoritos.objects.get(pagina=blog, usuario=user)
    favorito.delete()
    messages.success(request, f'Eliminaste el blog {blog.titulo} de tus favoritos.')
    return HttpResponseRedirect(reverse('blogs:list_all_blogs'))
