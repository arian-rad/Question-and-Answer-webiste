from django.shortcuts import render, get_object_or_404, redirect
from questions.models import Question
from questions.forms import QuestionForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.urls import reverse_lazy


# def index_view(request): # its home page
#     return render(request, 'questions/index.html')
class HomeTemplateView(TemplateView):
    template_name = 'questions/index.html'


# def about_view(request):
#     return render(request, 'questions/about.html')

class AboutTemplateView(TemplateView):
    template_name = 'questions/about.html'

# def questions_view(request):
#     all_questions = Question.objects.all()
#     return render(request, 'questions/posts/allPosts.html',{'all_posts': all_questions})

class QuestionListView(ListView):
    model = Question
    template_name = 'questions/posts/allPosts.html'


# def question_detail_view(request, question_id):
#     question = get_object_or_404(Question, id=question_id)
#     return render(request, 'questions/posts/detail.html', {'question':question})

class QuestionDetailView(DetailView):
    model = Question
    template_name = 'questions/posts/detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.num_of_views += 1
        self.object.save()
        self.object.refresh_from_db()
        return context

# def add_question(request):
#     if request.method == 'POST':
#         question_form = QuestionForm(request.POST)
#         if question_form.is_valid():
#             cleaned_data = question_form.cleaned_data
#             question = Question(title=cleaned_data['title'], text=cleaned_data['text'], category=cleaned_data['category'])
#             question.save()
#             return redirect('questions:all_questions')

#     else:
#         question_form = QuestionForm()
#         return render(request,'questions/posts/add_question.html', {'QuestionForm': question_form})


class QuestionCreateView(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'questions/posts/add_question.html'
    success_url = reverse_lazy('questions:all_questions')