from django.urls import path
from .views import *
app_name = 'coreFa'


urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
    path('', HomeView.as_view(), name='home'),
    ]