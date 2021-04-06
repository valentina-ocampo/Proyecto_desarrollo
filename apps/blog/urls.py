from django.urls import path
from .views import ListBlogsView, ListAllBlogsView, DetailBlogView, CreateBlogView, UpdateBlogView, DeleteBlogView

# Create your urls here.


app_name = 'blogs'

urlpatterns = [
    path('', ListBlogsView.as_view(), name='list_blogs'),
    path('all_blogs/', ListAllBlogsView.as_view(), name='list_all_blogs'),
    path('create/', CreateBlogView.as_view(), name='create_blog'),
    path('<int:pk>/<slug:blog_slug>/', DetailBlogView.as_view(), name='read_blog'),
    path('update/<int:pk>/<slug:blog_slug>/', UpdateBlogView.as_view(), name='update_blog'),
    path('delete/<int:pk>/<slug:blog_slug>/', DeleteBlogView.as_view(), name='delete_blog'),
]
