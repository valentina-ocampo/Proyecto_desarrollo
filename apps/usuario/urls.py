from django.urls import path
from .views import SignUpView, UserDetailView, UserEditView, userDelete, SeguirUsuarioView, VerSiguiendoView, VerSeguidoresView, DeleteSeguidorView

# Create your urls here.
 

app_name = 'usuario'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', UserDetailView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', UserEditView.as_view(), name='edit_profile'),
    path('userDelete/<int:userId>/', userDelete , name='userDelete'),
    path('seguir_usuario/<int:user_id>/', SeguirUsuarioView , name='seguir_usuario'),
    path('ver_siguiendo/', VerSiguiendoView.as_view() , name='ver_siguiendo'),
    path('ver_seguidores/', VerSeguidoresView.as_view() , name='ver_seguidores'),
    path('dejar_seguir/<int:id_seguido>', DeleteSeguidorView , name='dejar_seguir'),
]
