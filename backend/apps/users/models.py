from django.db import models
from django.conf import settings
from config.models import BaseModel
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

# default user to email and remove username

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email

class Interest(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    icon = models.CharField(max_length=50, blank=True)

# profile model, extends django user model to include extra fields
class Profile(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=100)
    avatar_url = models.URLField(blank=True)
    bio = models.TextField(blank=True, max_length=500)
    interests = models.ManyToManyField(Interest, blank=True)

    def __str__(self) -> str:
        return self.name

# A group consist of members and a owner. Multiple members can be granted the owner permission though
class Group(BaseModel):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='GroupMembership', related_name='seat_groups')

class GroupMembership(BaseModel):
    class Role(models.TextChoices):
        OWNER = 'OWN', _('Owner')
        MEMBER = 'MEM', _('Member')
    
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.MEMBER)
    class Meta:
        unique_together = ('group', 'user')

    