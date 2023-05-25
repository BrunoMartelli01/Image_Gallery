from django.urls import path
from . import views
urlpatterns = [
    path('images_list/', views.images_list, name='images_list'),
    path('delete_image/<int:id>/', views.delete_image, name='delete_image'),
    ]