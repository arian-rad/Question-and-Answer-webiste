from django.contrib import admin
from questions.models import Question, Category, Answer


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('num_of_views',)
    list_display = ('title', 'user', 'category', 'num_of_views', 'date_created',)

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('author', 'date_created',)
