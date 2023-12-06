from django.db import models
from django.contrib.auth import models as auth_models

class PersonManager(auth_models.BaseUserManager):
    def create_user(self, first_name : str, last_name : str, email : str, role : str, password : str, is_staff = False, is_superuser = False) -> "Person":
        if not email:
            raise ValueError("User must have an email")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")
        if not role:
            raise ValueError("User must have a role")

        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.role = role
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser

        user.save()

        return user

    def create_superuser(self, first_name : str, last_name : str, email : str, role : str, password : str) -> "Person":
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            role=role,
            password=password,
            is_staff=True,
            is_superuser=True
        )

        user.save()

        return user

class Person(auth_models.AbstractUser):
    first_name = models.CharField(verbose_name="First Name", max_length=255)
    last_name = models.CharField(verbose_name="Last Name", max_length=255)
    role = models.CharField(verbose_name="Role", max_length=255)
    email = models.EmailField(verbose_name="Email", max_length=255, unique=True)
    password = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to="images/", null=True, blank=True)
    username = None

    objects = PersonManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "role"]

    def __str__(self):
        return f'{self.first_name} {self.last_name}'