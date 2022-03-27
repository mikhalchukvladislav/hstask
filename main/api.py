from django.http import JsonResponse
from .models import Auth, InviteCode
from rest_framework import viewsets, permissions
from .serializers import AuthSerializer, InviteCodeSerializer
from .views import *
from rest_framework.decorators import action
from rest_framework.response import Response


class AuthViewSet(viewsets.ModelViewSet):
    queryset = Auth.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AuthSerializer


class InviteCodeViewSet(viewsets.ModelViewSet):
    queryset = InviteCode.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = InviteCodeSerializer

    @action(detail=True, methods=['get'])
    def phones(self, request, phone=None):
        phones = InviteCode.objects.filter(phone_to_invite=phone).values_list('phone_from_invite', flat=True)
        return Response(phones)

    @action(detail=True, methods=['post'])
    def newuser(self, request, phone=None, code=None):
        user_info = Auth.objects.filter(phone=phone).values_list('id', 'my_invite_code').get()
        error = ''
        invitecode_n = code
        phone_from_invite_n = phone
        invite_id_n = Auth.objects.filter(my_invite_code=code).get()
        phone_to_invite_n = Auth.objects.filter(my_invite_code=code).get().phone
        if  phone not in InviteCode.objects.values_list('phone_from_invite', flat=True):
            if code != user_info[1] and code in Auth.objects.values_list('my_invite_code', flat=True):
                InviteCode.objects.create(invitecode=invitecode_n, phone_from_invite=phone_from_invite_n, invite_id=invite_id_n, phone_to_invite=phone_to_invite_n)
            elif code == user_info[1]:
                    error = f'Вы вводите свой инвайт код. Можно ввести только чужой инвайт код.'
                    return Response(error)
            elif code not in Auth.objects.values_list('my_invite_code', flat=True):
                    error = f'Вы вводите несуществующий инвайт код.'
                    return Response(error)
        else:
            usephone_invite_code = InviteCode.objects.filter(phone_from_invite=phone).values_list('invitecode', flat=True).get()
            invite_code_from = Auth.objects.filter(my_invite_code=InviteCode.objects.filter(phone_from_invite=phone).values_list('invitecode', flat=True).get()).values_list('phone', flat=True).get()
            error = f'Вы уже вводили инвайт-код: {usephone_invite_code}, пользователя с номером: {invite_code_from}. \
                Можно ввести только один инвайт код.'
            return Response(error)
        querysets = InviteCode.objects.all()
        serializer = self.get_serializer(querysets, many=True)
        return Response(serializer.data)