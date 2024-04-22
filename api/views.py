import phonenumbers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from auth_app.models import Userplus
from .serializers import *
from auth_app.utils import send_sms, generate_code, code
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def send_activation_code(request):
    phone_number = phonenumbers.parse(request.data.get('phone_number'), None)
    if not phonenumbers.is_valid_number(phone_number):
        return Response(status=400, data=f'no valid naumber {phone_number}')
    codde = generate_code()
    code[codde] = phone_number
    send_sms(phone_number, f'your actvation code is {codde}')
    return Response(data={'code': code}, status=200)


@api_view(['POST'])
def activate_user(request):
    codde = request.data.get("codde")
    if codde in code.keys():
        del code[codde]
        return Response(status=200, data={"messages": 'your code activated succesfuly'})
    return Response(status=400, data={"messages": 'error code {code} try again'})


@api_view(['GET'])
def profile(request):
    user = request.user
    serializer = ProfileSerializer(user)
    return Response(serializer.data)


@api_view(['GET'])
def users_with_invites(request):
    user = request.user
    users_with_invites = Userplus.objects.filter(activated_invite_code=user.invite_code)
    serializer = ProfileSerializer(users_with_invites, many=True)
    return Response(serializer.data)
