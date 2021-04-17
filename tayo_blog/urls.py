from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='tayo_blog-home'),
    path('about/', views.about, name='tayo_blog-about'),
]