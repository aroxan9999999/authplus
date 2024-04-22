from django.contrib import admin
from .models import Userplus, InviteCode


@admin.register(Userplus)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'invite_code', 'activated_invite_code')
    search_fields = ('phone_number', 'invite_code', 'activated_invite_code')


@admin.register(InviteCode)
class InviteCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'created_at')
    search_fields = ('code', 'user__username', 'created_at')
