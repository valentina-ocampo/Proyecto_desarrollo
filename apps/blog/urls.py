from django.urls import path
from .views import ListBlogsView, ListAllBlogsView, DetailBlogView, CreateBlogView, UpdateBlogView, DeleteBlogView, CreateFavoritosView, ListFavoritosView, reportBlog, reportListBlog, DeleteReportView, ListBuscarBlogsView, DeleteFavoritoView

# Create your urls here.


app_name = 'blogs'

urlpatterns = [
    path('', ListBlogsView.as_view(), name='list_blogs'),
    path('all_blogs/', ListAllBlogsView.as_view(), name='list_all_blogs'),
    path('create/', CreateBlogView.as_view(), name='create_blog'),
    path('<int:pk>/<slug:blog_slug>/', DetailBlogView.as_view(), name='read_blog'),
    path('update/<int:pk>/<slug:blog_slug>/', UpdateBlogView.as_view(), name='update_blog'),
    path('delete/<int:pk>/<slug:blog_slug>/', DeleteBlogView.as_view(), name='delete_blog'),
    path('create_favoritos/<int:blog_id>/', CreateFavoritosView, name='create_favoritos'),
    path('favoritos/', ListFavoritosView.as_view(), name='list_favoritos'),
    path('delete/Report/<int:pk>/<slug:blog_slug>/', DeleteReportView.as_view(), name='delete_blog_reporter'),
    path('report/<int:blogId>/', reportBlog , name='report_blog'),
    path('reportList/', reportListBlog , name='report_list_blogs'),
    path('buscar_blogs/', ListBuscarBlogsView.as_view() , name='buscar_blogs'),
    path('eliminar_favorito/<int:id_blog>/', DeleteFavoritoView , name='eliminar_favorito'),
]
