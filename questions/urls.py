from django.urls import path
from questions import views

app_name = 'questions'

urlpatterns = [
    path('', views.index_view, name='home'),
    path('questions/', views.questions_view, name='all_questions'),
    path('add_question', views.add_question, name='add_question'),
    path('questions/<int:question_id>/detail', views.question_detail_view, name='question_detail'),
    path('about/', views.about_view, name='about'),
]
