from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name='تلفن همراه')
    profile_image = models.ImageField(default='default.jpg', null=True, blank=True, upload_to='images/profile-images/')
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.get_full_name():
            return self.get_full_name()
        else:
            return self.get_username()

    def get_num_of_questions(self):
        return self.user_questions.count()

    def get_num_of_answers(self):
        return self.answer_rel.count()
