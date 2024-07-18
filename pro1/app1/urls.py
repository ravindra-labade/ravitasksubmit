from django.urls import path
from .views import create_post, show_post, update_post, delete_post


urlpatterns = [
    path('add/', create_post, name='add_url'),
    path('show/', show_post, name='show_url'),
    path('update/<int:pk>', update_post, name='update_url'),
    path('delete/<int:pk>', delete_post, name='delete_url'),
]
