from django.urls import path
from .views import SignUpView, UserDetailView, UserEditView, userDelete

# Create your urls here.


app_name = 'usuario'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', UserDetailView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', UserEditView.as_view(), name='edit_profile'),
    path('userDelete/<int:userId>', userDelete , name='userDelete'),
]
