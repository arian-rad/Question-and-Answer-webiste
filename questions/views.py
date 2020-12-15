from django.shortcuts import render, get_object_or_404, redirect
from questions.models import Question
from questions.forms import QuestionForm


def index_view(request): # its home page
    return render(request, 'questions/index.html')

def about_view(request):
    return render(request, 'questions/about.html')

def questions_view(request):
    all_questions = Question.objects.all()
    return render(request, 'questions/posts/allPosts.html',{'all_posts': all_questions})

def question_detail_view(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'questions/posts/detail.html', {'question':question})

def add_question(request):
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            curent_user = request.user
            cleaned_data = question_form.cleaned_data
            question = Question(title=cleaned_data['title'], text=cleaned_data['text'], category=cleaned_data['category'], user=curent_user)
            print('user id: ', curent_user.id)
            question.save()


            # instance = question_form.save(commit=False)
            # instance.user = request.user.username
            # # question_form.user = request.user.username
            # # question_form.save()
            # instance.save()

            return redirect('questions:all_questions')

    else:
        question_form = QuestionForm()
        return render(request,'questions/posts/add_question.html', {'QuestionForm': question_form})