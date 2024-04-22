from django.urls import path
from .views import login_view, activate_code, activate_invite_code

urlpatterns = [
    path('login/', login_view, name='login'),
    path('activate/', activate_code, name='activate'),
    path('activate_invite_code/', activate_invite_code, name='activate_invite_code'),
]