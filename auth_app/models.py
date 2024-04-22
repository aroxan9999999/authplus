from django.db import models
from django.contrib.auth.models import AbstractUser
import random
import string


class Userplus(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    invite_code = models.CharField(max_length=6, null=True, blank=True)
    activated_invite_code = models.CharField(max_length=6, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:  # If the user is being created
            self.generate_invite_code()
        super(Userplus, self).save(*args, **kwargs)

    def generate_invite_code(self):
        if not self.invite_code:
            self.invite_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))


class InviteCode(models.Model):
    code = models.CharField(max_length=6, unique=True)
    user = models.ForeignKey(Userplus, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code
