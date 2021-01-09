from django.urls import path
from questions import views

app_name = 'questions'

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('questions/', views.QuestionListView.as_view(), name='all_questions'),
    # path('add_question', views.add_question, name='add_question'),
    path('add_question/', views.QuestionCreateView.as_view(), name='add_question'),
    # path('questions/<int:question_id>/detail', views.question_detail_view, name='question_detail'),
    path('questions/<int:pk>/<str:slug>/detail/', views.QuestionDetailView.as_view(), name='question_detail'),
    path('about/', views.AboutTemplateView.as_view(), name='about'),
    path('category/<int:pk>/questions/', views.CategoryQuestionsDetailView.as_view(), name='category_detail'),
    path('create_answer/<int:pk>/', views.AnswerCreateView.as_view(), name='create_answer'),
    path('like-answer/<int:pk>/', views.AnswerLikeCreateVeiw.as_view(), name='like_answer'),
    path('like-question/<int:pk>/', views.QuestionLikeCreateView.as_view(), name='like_question'),
    path('report-question/<int:pk>/', views.QuestionReportCreateView.as_view(), name='report'),
    path('report-answer/<int:pk>/', views.AnswerReportCreateView.as_view(), name='report'),
    path('report/success/',views.ReportSuccessTemplateView.as_view(), name='report-success'),
    path('tag/<int:pk>/questions/', views.TagQuestionDetailView.as_view(), name='tag_detail')

]
