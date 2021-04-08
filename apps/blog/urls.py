from django.urls import path
from .views import ListBlogsView, ListAllBlogsView, DetailBlogView, CreateBlogView, UpdateBlogView, DeleteBlogView, reportBlog, reportListBlog, DeleteReportView

# Create your urls here.


app_name = 'blogs'

urlpatterns = [
    path('', ListBlogsView.as_view(), name='list_blogs'),
    path('all_blogs/', ListAllBlogsView.as_view(), name='list_all_blogs'),
    path('create/', CreateBlogView.as_view(), name='create_blog'),
    path('<int:pk>/<slug:blog_slug>/', DetailBlogView.as_view(), name='read_blog'),
    path('update/<int:pk>/<slug:blog_slug>/', UpdateBlogView.as_view(), name='update_blog'),
    path('delete/<int:pk>/<slug:blog_slug>/', DeleteBlogView.as_view(), name='delete_blog'),
    path('delete/Report/<int:pk>/<slug:blog_slug>/', DeleteReportView.as_view(), name='delete_blog_reporter'),
    path('report/<int:blogId>/', reportBlog , name='report_blog'),
    path('reportList/', reportListBlog , name='report_list_blogs'),
]
