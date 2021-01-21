from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name='تلفن همراه')

    def __str__(self):
        if self.get_full_name():
          return self.get_full_name()
        else:
            return self.get_username()



class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    # profile_image = models.ImageFiled(default='default.jpg',null=True, blank=True, uplode_to='images/profile-images/')

