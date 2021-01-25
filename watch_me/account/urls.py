from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('welcome/', views.welcome, name="welcome"),
    path('profile/', views.profile, name="profile"),
    path('register/', views.sign_up, name="register"),
    path('login/', views.sign_in, name="login"),
    path('logout/', views.sign_off, name="logout"),
    path('edit-profile/', views.edit_profile, name="edit_profile"),
    path('user/<username>/', views.user_profile, name="user_profile"),
    path('follow/<username>/', views.follow, name="follow"),
    path('unfollow/<username>/', views.unfollow, name="unfollow"),
]