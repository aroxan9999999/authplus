import phonenumbers
from django.core.exceptions import ValidationError
from django import forms

def validate_phone_number(value):
    try:
        phone_number = phonenumbers.parse(value, None)
        if not phonenumbers.is_valid_number(phone_number):
            raise ValidationError("Номер телефона невалиден")
    except phonenumbers.NumberParseException:
        raise ValidationError("Неверный формат номера телефона")


class CustomUserCreationForm(forms.Form):
    phone_number = forms.CharField(validators=[validate_phone_number], max_length=20)


