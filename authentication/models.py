import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

USER_TYPE_CHOICES = (
    ('student', 'Student'),
    ('staff', 'Staff'),
    ('admin', 'Admin'),
)

class TicketingUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password)
        user.is_staff = True
        user.save(using=self._db)
        return user

class TicketingUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    registration_number = models.CharField(max_length=100, unique=True, null=True, blank=True)

    objects = TicketingUserManager()

    def __str__(self):
        return self.username

