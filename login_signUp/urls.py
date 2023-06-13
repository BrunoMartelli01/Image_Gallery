from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='login'),
    path('login/', views.loginView, name='login'),
    path('signUp/', views.signUpView, name='signUp'),
]