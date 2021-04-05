from django.urls import path
from .views import HomePageView

# Create your urls here.


app_name = 'core'

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
]
