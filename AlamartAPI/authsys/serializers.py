from rest_framework.validators import UniqueValidator

from .models import User
from rest_framework import serializers


class UserSerializers(serializers.ModelSerializer):
    full_name = serializers.CharField(max_length=100)
    email = serializers.EmailField(read_only=True)
    is_verified = serializers.BooleanField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)
    last_login = serializers.DateTimeField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = ('full_name', 'email', 'is_staff', 'is_verified', 'last_login', 'date_joined', 'is_profile_complete',
                  'telephone', 'birthdate', 'address')
        read_only_fields = ('email', 'is_staff', 'is_verified', 'last_login', 'date_joined', 'is_profile_complete')


class LoginReqSerializers(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class RegistrationReqSerializers(serializers.Serializer):
    full_name = serializers.CharField(max_length=100)
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all(), message='This email address is already used by other '
                                                                         'user')]
    )


class ResendActivationReqSerializers(serializers.Serializer):
    email = serializers.EmailField()


class EmailConfirmationReqSerializers(serializers.Serializer):
    token = serializers.CharField(max_length=32)


class UpdateProfileReqSerializers(serializers.Serializer):
    full_name = serializers.CharField(max_length=100)
    birthdate = serializers.DateField()
    telephone = serializers.CharField(max_length=13)
    address = serializers.CharField(max_length=200)


class UpdateProfileImageReqSerializers(serializers.Serializer):
    image_url = serializers.CharField(max_length=100)
