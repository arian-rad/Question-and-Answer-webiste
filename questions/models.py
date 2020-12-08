from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):    
    title = models.CharField(max_length=120, verbose_name='عنوان پرسش')    
    text = models.TextField(max_length=1200,verbose_name='متن پرسش')
    slug = models.SlugField(max_length=90, unique=True, verbose_name='لینک یکتا')    
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='پرسشگر', related_name='questions')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    date_edited = models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')
    # date_created and date_edited have auto_now_add, auto_now property because users are not allowed
    # to edit DateTime field P.S: blank and null are False by default
    category = models.ManyToManyField('Category', verbose_name='دسته بندی')
    # num_of_likes = models.IntegerField()
    # approved_answer = BooleanField(default=False)
    # num_of_reports = models.IntegerField()
    

    class Meta:
        verbose_name = 'سوال'
        verbose_name_plural = 'سوال ها'
        ordering = ('date_created',)
        db_table = 'question'

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=90, unique=True, allow_unicode=True, verbose_name='لینک یکتا')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    date_edited = models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')
      
    
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = ' دسته بندی ها'
        ordering = ('date_created', )
        db_table = 'category'

    def __str__(self):
        return self.title
    