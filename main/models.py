from enum import unique
from imghdr import what
from django.db import models
import random
import string
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Auth(models.Model):

    global value_before
    value_before = ''


    def validate_invitecode():
        global value_before
        value = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
        if value == value_before:
            value = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
        else:
            value_before = value
            return value


    phone = models.CharField(max_length=12, unique=True)
    my_invite_code = models.CharField(max_length=6, default=validate_invitecode)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'Авторизация'
        # verbose_name_plural = 'Пользователи'


class Code(models.Model):
    def validate_code(value):
        if len(str(value)) != 4 and value != 0000:
            raise ValidationError(
                _('%(value)s is not a code'),
                params={'value': value},
            )

    code = models.IntegerField(validators=[validate_code])

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Код подтверждения'


class InviteCode(models.Model):

    invitecode = models.CharField(max_length=6)
    phone_from_invite = models.CharField(max_length=12, unique=True)
    phone_to_invite = models.CharField(max_length=12, null=True)
    invite_id = models.ForeignKey(Auth, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.invitecode

    class Meta:
        verbose_name = 'Код подтверждения'