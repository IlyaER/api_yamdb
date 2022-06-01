from rest_framework import serializers

from users.models import User


class Registration(serializers.Serializer):
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField(
        required=True
    )

    def validate(self, attrs):
        if attrs.get('username') == 'me':
            raise serializers.ValidationError('Недопустимое имя.')
        if User.objects.filter(
                username=attrs.get('username')
        ).exists():
            raise serializers.ValidationError('Имя уже существует.')
        if User.objects.filter(
                email=attrs.get('email')
        ).exists():
            raise serializers.ValidationError('Почта уже существует.')
        return attrs

    class Meta:
        fields = ('username', 'email')
        model = User


class Confirmation(serializers.Serializer):
    username = serializers.CharField(
        required=True
    )
    confirmation_code = serializers.CharField(
        max_length=200,
        required=True
    )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username',
            'bio', 'email', 'role',)
