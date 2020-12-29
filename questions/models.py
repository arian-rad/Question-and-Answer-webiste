from django.db import models
# from django.contrib.auth.models import User
from accounts.models import User
from django.conf import settings
from ckeditor.fields import RichTextField


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
    

class Question(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان پرسش')    
    text = RichTextField(verbose_name='متن پرسش')
    slug = models.SlugField(max_length=90, unique=True, verbose_name='لینک یکتا', blank=True, null=True)    
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=settings.AUTH_USER_MODEL, verbose_name='پرسشگر', related_name='user_questions') # , blank=True, null=True default settings.AUTH_USER_MODE
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    date_edited = models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')
    # date_created and date_edited have auto_now_add, auto_now property because users are not allowed
    # to edit DateTime field P.S: blank and null are False by default
    category = models.ForeignKey(Category, on_delete=models.CASCADE ,verbose_name='دسته بندی', related_name='category_questions')    
    num_of_views = models.IntegerField(default=0, verbose_name='تعداد بازدید')
    likes = models.ManyToManyField(User, default=None, blank=True, related_name='like_questions')
    # approved_answer = BooleanField(default=False)

    def get_num_of_answers(self):
        return self.question_answers.count()
        

    class Meta:
        verbose_name = 'سوال'
        verbose_name_plural = 'سوال ها'
        ordering = ('-date_created',) # - is because we want to see the latest questions first!
        db_table = 'question'

    def __str__(self):
        return self.title

    def get_num_of_likes(self):
        num_likes = self.likes.count()
        return num_likes

    def get_like_status(self,request,id):
        if self.likes.filter(id=self.request.user.id).exists():
            return True
        else:
            return False


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=settings.AUTH_USER_MODEL, verbose_name='پاسخ دهنده', related_name='answer_rel')
    related_question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='سوال مربوطه', related_name='question_answers')
    body = RichTextField(verbose_name='متن جواب')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    date_edited = models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')
    likes = models.ManyToManyField(User, default=None, blank=True, related_name='like_answers')

    class Meta:
        verbose_name = 'جواب'
        verbose_name_plural = 'جواب ها'
        # ordering = want to be num of likes but how?
        db_table = 'answer'

    def get_num_of_likes(self):
        num_likes = self.likes.count()
        return num_likes

    def get_likea_status(self,request, id):
        if self.likes.filter(id=self.request.user.id).exists():
            return True
        else:
            return False





# class AnswerLike(models.Model):
#     LIKE_CHOICES = (
#         ('like', 'Like'),
#         ('Unlike', 'Unlike'),
#     )
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_answer_likes')
#     liked_answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='answer_like_rel')
#     value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)


# class Tag(models.Model):
