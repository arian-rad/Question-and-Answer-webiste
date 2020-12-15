# Generated by Django 3.1.3 on 2020-12-15 00:32

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', ckeditor.fields.RichTextField(verbose_name='متن جواب')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('date_edited', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_rel', to=settings.AUTH_USER_MODEL, verbose_name='پاسخ دهنده')),
                ('liked', models.ManyToManyField(blank=True, default=None, related_name='liked_answers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'جواب',
                'verbose_name_plural': 'جواب ها',
                'db_table': 'answer',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='عنوان دسته بندی')),
                ('slug', models.SlugField(allow_unicode=True, max_length=90, unique=True, verbose_name='لینک یکتا')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('date_edited', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': ' دسته بندی ها',
                'db_table': 'category',
                'ordering': ('-date_created',),
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='عنوان پرسش')),
                ('text', ckeditor.fields.RichTextField(verbose_name='متن پرسش')),
                ('slug', models.SlugField(blank=True, max_length=90, null=True, unique=True, verbose_name='لینک یکتا')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('date_edited', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_questions', to='questions.category', verbose_name='دسته بندی')),
                ('user', models.ForeignKey(blank=True, default='auth.User', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_questions', to=settings.AUTH_USER_MODEL, verbose_name='پرسشگر')),
            ],
            options={
                'verbose_name': 'سوال',
                'verbose_name_plural': 'سوال ها',
                'db_table': 'question',
                'ordering': ('-date_created',),
            },
        ),
        migrations.CreateModel(
            name='AnswerLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=10)),
                ('liked_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_like_rel', to='questions.answer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answer_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='related_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_answers', to='questions.question', verbose_name='سوال مربوطه'),
        ),
    ]