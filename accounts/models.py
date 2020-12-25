from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=15, null=True, verbose_name='تلفن همراه')

    def __str__(self):
        if not self.get_full_name() is None:
          return self.get_full_name()
        else:
            pass