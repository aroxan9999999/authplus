from django.shortcuts import render, redirect
from .models import Userplus, InviteCode
from .forms import CustomUserCreationForm
from .utils import send_sms, code, generate_code


def login_view(request):
    number_is_valid = False
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            number_is_valid = True
            phone_number = form.cleaned_data['phone_number']
            codde = generate_code()
            message = f'Your code is {codde}'
            send_sms(phone_number, message)
            code[codde] = phone_number
            return redirect('activate')
        return redirect('login')
    else:
        form = CustomUserCreationForm()
        return render(request, 'auth_templates/login.html', {'form': form, 'number_is_valid': number_is_valid})


def activate_code(request):
    if request.method == 'POST':
        entered_code = request.POST.get('code')
        if entered_code and int(entered_code) in code:
            phone_number = code[int(entered_code)]
            user, created = Userplus.objects.get_or_create(phone_number=phone_number)
            user.save()
            del code[int(entered_code)]
            return render(request, 'auth_templates/profile.html', {'user': user})
        else:
            return render(request, 'auth_templates/activate_code.html', {'error': 'Invalid code'})
    else:
        return render(request, 'auth_templates/activate_code.html')


def activate_invite_code(request):
    if request.method == 'POST':
        entered_code = request.POST.get('invite_code')
        try:
            invite_code = InviteCode.objects.get(code=entered_code)
            if not invite_code.user.activated_invite_code:
                invite_code.user.activated_invite_code = entered_code
                invite_code.user.save()
                invite_code.delete()
                return render(request, 'auth_templates/profile.html', )
            else:
                return render(request, 'auth_templates/pr.html',
                              {'error': 'Invite code has already been activated'})
        except InviteCode.DoesNotExist:
            return render(request, 'auth_templates/activate_code.html', {'error': 'Invalid invite code'})
    return render(request, 'auth_templates/activate_code.html')
