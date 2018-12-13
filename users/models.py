from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=False, blank=False, null=True)
    age = models.PositiveIntegerField(default=0)
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return '(id: ' + str(self.id) + ') ' + self.email

