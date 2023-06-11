from django.urls import path
from . import views
urlpatterns = [
    path('', views.images_list, name='images_list'),
    path('images_list/', views.images_list, name='images_list'),
    path('delete_img/<int:id>/', views.delete_img, name='delete_image'),
    path('upload_img/', views.upload_img, name='upload_img'),
    path('download_img/<int:id>/', views.download_img, name='download_img'),
    ]