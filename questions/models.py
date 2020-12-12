from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# !! needs makemigrations & migrate 12/12/2020 12:35 Arian Radmehr !!

class Question(models.Model):    

    title = models.CharField(max_length=120, verbose_name='عنوان پرسش')    
    text = RichTextField(verbose_name='متن پرسش')
    slug = models.SlugField(max_length=90, unique=True, verbose_name='لینک یکتا', blank=True, null=True)    
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='پرسشگر', related_name='questions', blank=True, null=True)
    # blank and null are both set to True for user beacuse i still dont know how to make djagno to assging the 
    # currently logged in  user as default
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    date_edited = models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')
    # date_created and date_edited have auto_now_add, auto_now property because users are not allowed
    # to edit DateTime field P.S: blank and null are False by default
    category = models.ManyToManyField('Category', verbose_name='دسته بندی', related_name='question_rel')
    # num_of_likes = models.IntegerField()
    # approved_answer = BooleanField(default=False)
    # num_of_reports = models.IntegerField()    

    class Meta:
        verbose_name = 'سوال'
        verbose_name_plural = 'سوال ها'
        ordering = ('-date_created',) # - is beacuse we want to see the latest questions first!
        db_table = 'question'

    def __str__(self):
        return self.title


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='پاسخ دهنده', related_name='answer_rel')
    body = RichTextField(verbose_name='متن جواب')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    date_edited = models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')
    liked = ManyToManyField(User, default=None, blank=True, related_name='answer_rel') 

    class Meta:
        verbose_name = 'جواب'
        verbose_name_plural = 'جواب ها'
        # ordering = want to be num of likes but how?
        db_table = 'answer'

class AnswerLike(models.Model):
    LIKE_CHOICES = {
        'like': 'like',
        'Unlike': 'Unlike',
    }
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answer_like_rel')
    liked_answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='answer_like_rel')
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)



class Category(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=90, unique=True, allow_unicode=True, verbose_name='لینک یکتا')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    date_edited = models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')      
    
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = ' دسته بندی ها'
        ordering = ('-date_created', )
        db_table = 'category'

    def __str__(self):
        return self.title
    