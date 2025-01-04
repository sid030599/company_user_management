from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)

    # Add unique related_name attributes to resolve the conflict
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",  # Unique related_name
        blank=True,
        help_text="The groups this user belongs to.",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_set",  # Unique related_name
        blank=True,
        help_text="Specific permissions for this user.",
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
