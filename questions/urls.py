from django.urls import path
from questions import views

app_name = 'questions'

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    # path('questions/', views.questions_view, name='all_questions'),
    path('questions/', views.QuestionListView.as_view(), name='all_questions'),
    # path('add_question', views.add_question, name='add_question'),
     path('add_question', views.QuestionCreateView.as_view(), name='add_question'),
    #  path('questions/<int:question_id>/detail', views.question_detail_view, name='question_detail'),
    path('questions/<int:pk>/detail', views.QuestionDetailView.as_view(), name='question_detail'),
    path('about/', views.AboutTemplateView.as_view(), name='about'),
    path('category/<int:pk>/questions', views.CategoryQuestionsDetailView.as_view(), name='category_detail')
]
