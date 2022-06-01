from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import action, api_view
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt import tokens
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.permissions import (
    IsAdmin
)
from users.serializers import UserSerializer, Confirmation, Registration


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = [IsAdmin, IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['user__username', ]

    @action(methods=['patch', 'get'],
            permission_classes=[IsAuthenticated],
            detail=False,
            url_path='me',
            url_name='me')
    def me(self, request, *args, **kwargs):
        user = self.request.user
        serializer = self.get_serializer(user)
        if self.request.method == 'PATCH':
            serializer = self.get_serializer(
                user,
                data=request.data,
                partial=True
            )
            serializer.is_valid(
                raise_exception=True
            )
            serializer.save()
        return Response(serializer.data)


@api_view(['POST'])
def send_code(request):
    serializer = Registration(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')
    username = serializer.data.get('username')
    user = User.objects.get_or_create(
        email=email,
        username=username
    )[0]
    confirmation_code = PasswordResetTokenGenerator().make_token(user)
    send_mail('Код подтверждения для Yamdb',
              f'Ваш код подтверждения: {confirmation_code}',
              'support@yamdb.ru',
              [email])
    answer = {'email': f'{email}', 'username': f'{username}'}
    return Response(
        answer,
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
def get_token(request):
    serializer = Confirmation(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.data.get('username')
    confirmation_code = serializer.data.get('confirmation_code')
    user = get_object_or_404(User, username=username)
    if not PasswordResetTokenGenerator().check_token(user, confirmation_code):
        return Response(
            {'confirmation_code': 'Invalid confirmation code'},
            status=status.HTTP_400_BAD_REQUEST
        )
    token = tokens.AccessToken.for_user(user)
    return Response({'token': f'{token}'}, status=status.HTTP_200_OK)
