import secrets
import string

from django.conf import settings
from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy

from users.models import User


def create_secret_key(length):
    """создаем ключ"""
    combination = string.ascii_letters + string.digits
    secret_key = ''.join(secrets.choice(combination) for _ in range(length))
    return secret_key


def confirm_user_email(request, user):
    """ссылка + письмо для подтверждения почты"""
    secret_key = create_secret_key(30)
    user.email_confirm_key = secret_key
    user.save()

    current_site = get_current_site(request)
    message = render_to_string('users/confirm_email_message.html', {
        'domain': current_site.domain,
        'key': secret_key,
    })
    send_mail(
        subject='Подтверждение почты',
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email]
    )


def generate_password(request):
    new_password = create_secret_key(12)
    request.user.set_password(new_password)
    request.user.save()
    send_mail(
        subject='Вы сменили пароль из профиля',
        message=f'Новый пароль {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    return redirect(reverse_lazy('users:login'))