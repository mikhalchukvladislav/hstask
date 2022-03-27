from multiprocessing import context
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .models import Auth, Code, InviteCode
import time

def welcome(request):
    error = ''
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/authentication/user/' + str(Auth.objects.filter(phone=form.data.get('phone')).values_list('id', flat=True).get()))
        else:
            error = 'Форма была неверной'

    form = AuthForm()

    context = {
        'form': form,
        'error': error,
    }

    return render(request, 'main/welcome.html', context)


def auth(request, userid):
    error = ''
    if request.method == 'POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            time.sleep(2)
            return redirect('/profile/user/' + userid)
        else:
            error = 'Неверный код, повторите попытку'

    form = CodeForm()
    context = {
        'form': form,
        'error': error,
    }

    return render(request, 'main/auth.html', context)


def userpage(request, userid):
    
    user_info = Auth.objects.filter(id=int(userid)).values_list('phone', 'my_invite_code').get()

    error = ''
    if request.method == 'POST':
        if  user_info[0] not in InviteCode.objects.values_list('phone_from_invite', flat=True):
            form = InviteCodeForm(request.POST)
            if form.data.get('invitecode') != user_info[1] and form.data.get('invitecode') in Auth.objects.values_list('my_invite_code', flat=True):
                changes = form.save(commit=False)
                changes.phone_from_invite = user_info[0]
                changes.invite_id = Auth.objects.filter(my_invite_code=form.data.get('invitecode')).get()
                changes.phone_to_invite = Auth.objects.filter(my_invite_code=form.data.get('invitecode')).get().phone
                changes.save()
                # changes.save_m2m()
            elif form.data.get('invitecode') == user_info[1]:
                error = f'Вы вводите свой инвайт код. Можно ввести только чужой инвайт код.'
            elif form.data.get('invitecode') not in Auth.objects.values_list('my_invite_code', flat=True):
                error = f'Вы вводите несуществующий инвайт код.'
        else:
            usephone_invite_code = InviteCode.objects.filter(phone_from_invite=user_info[0]).values_list('invitecode', flat=True).get()
            invite_code_from = Auth.objects.filter(my_invite_code=InviteCode.objects.filter(phone_from_invite=user_info[0]).values_list('invitecode', flat=True).get()).values_list('phone', flat=True).get()
            error = f'Вы уже вводили инвайт-код: {usephone_invite_code}, пользователя с номером: {invite_code_from}. \
                Можно ввести только один инвайт код.'
    
    form = InviteCodeForm()

    context = {
        'form': form,
        'error': error,
        'userphone': user_info[0],
        'my_invite_code': user_info[1]
    }

    return render(request, 'main/userpage.html', context)