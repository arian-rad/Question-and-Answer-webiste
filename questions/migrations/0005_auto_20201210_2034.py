# Generated by Django 3.1.3 on 2020-12-10 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20201201_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.ManyToManyField(related_name='article_rel', to='questions.Category', verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='question',
            name='slug',
            field=models.SlugField(blank=True, max_length=90, null=True, unique=True, verbose_name='لینک یکتا'),
        ),
    ]
