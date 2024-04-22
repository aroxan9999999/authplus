from django.urls import path
from . import views

urlpatterns = [
    path('send_activation_code/', views.send_activation_code),
    path('activate_user/', views.activate_user),
    path('profile/', views.profile),
    path('users_with_invites/', views.users_with_invites),
]
