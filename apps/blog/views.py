from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from .forms import BlogForm
from .models import Blog
from django.urls import reverse_lazy

# Create your views here.


class ListBlogsView(ListView):
    model = Blog
    template_name = 'blog/blogs.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.filter(usuario=self.request.user)


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
    success_url = reverse_lazy('blogs:update_blog')

    def get_success_url(self):
        messages.success(self.request, 'Blog actualizado satisfactoriamente.')
        return super().get_success_url()


class DeleteBlogView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs:list_blogs')

    def get_success_url(self):
        messages.success(self.request, 'Blog eliminado satisfactoriamente.')
        return super().get_success_url()
