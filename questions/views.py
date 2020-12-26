from django.shortcuts import render, get_object_or_404, redirect
from questions.models import Question, Category, Answer
from questions.forms import QuestionForm, AnswerForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class HomeTemplateView(TemplateView):
    template_name = 'questions/index.html'


class AboutTemplateView(TemplateView):
    template_name = 'questions/about.html'


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
        context['answers'] = self.object.question_answers.all()
        # context['category1'] = self.object.category
        self.object.num_of_views += 1
        self.object.save()
        self.object.refresh_from_db()
        return context


# class QuestionCreateView(CreateView):
#     model = Question
#     form_class = QuestionForm
#     template_name = 'questions/posts/add_question.html'
#     success_url = reverse_lazy('questions:all_questions')


@method_decorator(login_required, name='dispatch')
class QuestionCreateView(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'questions/posts/add_question.html'
    success_url = reverse_lazy('questions:all_questions')

    def get(self, request):
         question_form = QuestionForm()
         return render(request,'questions/posts/add_question.html', {'form': question_form})

    def post(self, request):
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            cleaned_data = question_form.cleaned_data
            current_user = request.user
            question = Question(title=cleaned_data['title'], text=cleaned_data['text'], category=cleaned_data['category'], user=current_user)
            question.save()
            return redirect('questions:all_questions')



class CategoryQuestionsDetailView(DetailView):
    model = Category
    template_name = 'questions/categories/category_questions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_ques'] = context['category'].category_questions.all()  # related_name = category_questions

        return context

@method_decorator(login_required, name='dispatch')
class AnswerCreateView(CreateView):
    model = Answer
    template_name = 'questions/posts/create_answer.html'
    form_class = AnswerForm
    success_url = reverse_lazy('questions:question_detail')

    def post(self, request, pk):
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            cleaned_data = answer_form.cleaned_data
            current_user = request.user
            question = get_object_or_404(Question, id=pk)
            answer = Answer(body=cleaned_data['body'], related_question=question, author=current_user)
            answer.save()
            return redirect('questions:question_detail', pk)

