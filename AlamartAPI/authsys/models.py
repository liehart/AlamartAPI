from string import ascii_letters, digits

from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db import models
from django.utils.crypto import get_random_string
from django.utils.translation import ugettext_lazy as _


def generate_email_token():
    return get_random_string(length=32, allowed_chars=ascii_letters + digits)


class UserManager(BaseUserManager):

    def _create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('The given email must set.')
        if not password:
            raise ValueError('The given password must set')

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)

        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        if kwargs.get('is_staff') is False:
            raise ValueError('Superuser must have is_staff=True')
        if kwargs.get('is_superuser') is False:
            raise ValueError('Superuser must have is_superuser=True')

        return self._create_user(email, password, **kwargs)


class User(AbstractUser):

    username = None
    first_name = None
    last_name = None

    full_name = models.CharField(max_length=100)
    email = models.CharField(_('email address'), unique=True, max_length=100)
    birthdate = models.DateField(default=None, null=True)
    is_verified = models.BooleanField(default=False)

    telephone = models.CharField(max_length=13)
    address = models.CharField(max_length=200)

    image_url = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return "{} - {}".format(self.full_name, self.email)

    @property
    def is_profile_complete(self):
        if not self.telephone or not self.address:
            return False
        else:
            return True

    objects = UserManager()


class RegistrationHandler(models.Model):

    user = models.OneToOneField(to=User, related_name='reg_token', on_delete=models.CASCADE)
    token = models.CharField(max_length=32, default=generate_email_token, unique=True)
    is_used = models.BooleanField(default=False)
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.user.full_name, self.user.email)

    @staticmethod
    def send_activation_email():
        return False
