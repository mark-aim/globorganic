from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, username, phone_number, password=None):
        if not email:
            raise ValueError('email is required!');
        if not username:
            raise ValueError('username is required!');
        if not phone_number:
            raise ValueError('phone number is required!');

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            phone_number = phone_number
        );
        user.set_password(password);
        user.save(using=self._db);
        return user;
    
    def create_superuser(self, email, username, phone_number, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username, 
            phone_number=phone_number, 
            password=password);
        user.is_admin = True;
        user.is_superuser = True;
        user.is_staff = True;
        user.save(using=self._db);
        return user;


class User(AbstractBaseUser):
    first_name = models.CharField(verbose_name="first name", max_length=25);
    last_name = models.CharField(verbose_name="last name", max_length=25);
    username = models.CharField(verbose_name="username", max_length=16, unique=True);
    email = models.EmailField(verbose_name="email address", max_length=60, unique=True);
    phone_number = models.CharField(verbose_name="phone number", max_length=20, unique=True);
    join_date = models.DateTimeField(verbose_name="join in date", auto_now_add=True);
    last_login = models.DateTimeField(verbose_name="last time login", auto_now=True);
    is_admin = models.BooleanField(verbose_name="is admin", default=False);
    is_active = models.BooleanField(verbose_name="is active", default=True);
    is_staff = models.BooleanField(verbose_name="is staff", default=False);
    is_superuser = models.BooleanField(verbose_name="is superuser", default=False);

    USERNAME_FIELD = "username";
    REQUIRED_FIELDS=['phone_number', 'email'];

    objects = UserManager();

    def __str__(self):
        return self.username;
    
    def has_perm(self, perm, obj=None):
        return True;

    def has_module_perms(self, app_label):
        return True;