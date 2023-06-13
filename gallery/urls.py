from django.urls import path
from . import views
urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('getToken/', views.getToken, name='getToken'),
]