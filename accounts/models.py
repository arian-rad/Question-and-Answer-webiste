from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
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


class Notification(models.Model):
    NOTIFICATION_TYPE = (
        ('question liked', 'لایک پرسش'),
        ('answer liked', 'لایک پاسخ'),
        ('question answered', 'پاسخ به سوال'),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر', related_name='owner_notifications')
    notifier = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ایجاد کننده اعلامیه', related_name='notifier_notifs', null=True)
    message = models.TextField(max_length=200, default="", blank=True, null=True, verbose_name='متن اعلامیه')
    type = models.CharField(max_length=30, choices=NOTIFICATION_TYPE, default='', verbose_name='نوع اعلامیه')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = 'اعلامیه'
        verbose_name_plural = 'اعلامیه ها'
        ordering = ('-date',)


