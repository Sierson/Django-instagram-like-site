from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.home, name='home'),
    path('create-post/', views.create_post, name='create_post'),
    path('like/<int:pk>', views.like, name="like"),
    path('unlike/<int:pk>', views.unlike, name="unlike"),
]