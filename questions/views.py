from django.shortcuts import render, get_object_or_404
from questions.models import Question


def index_view(request): # its home page
    return render(request, 'questions/index.html')

def about_view(request):
    return render(request, 'questions/about.html')

def questions_view(request):
    all_questions = Question.objects.all()
    return render(request, 'questions/posts/allPosts.html',{'all_posts': all_questions})

def question_detail_view(request, slug):
    question = get_object_or_404(Question, slug=slug)
    return render(request, 'questions/posts/detail.html', {'question':question})