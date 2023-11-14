from django.urls import path
from .views import user_logout, create_profile, edit_profile, delete_profile, profile_list, user_login

app_name = 'profiles'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('create/', create_profile, name='create_profile'),
    path('<str:username>/edit/', edit_profile, name='edit_profile'),
    path('<str:username>/delete/', delete_profile, name='delete_profile'),
    path('list/', profile_list, name='profile_list'),
    path('logout/', user_logout, name='logout'),
]