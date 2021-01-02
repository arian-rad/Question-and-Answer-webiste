from django.shortcuts import render, get_object_or_404, redirect
from questions.models import Question, Category, Answer, QuestionReport, AnswerReport, Tag
from questions.forms import QuestionForm, AnswerForm, AnswerReportForm, QuestionReportForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType


class HomeTemplateView(TemplateView):
    template_name = 'questions/index.html'


class AboutTemplateView(TemplateView):
    template_name = 'questions/about.html'


class QuestionListView(ListView):
    model = Question
    template_name = 'questions/posts/allPosts.html'


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     """Handling likes for the questions in Question List View"""
    #     question = get_object_or_404(Question, id=self.kwargs['pk'])
    #     question_liked = False
    #     if question.likes.filter(id=self.request.user.id).exists():
    #         question_liked = True
    #     context['question_liked'] = question_liked
    #
    #     return context



@method_decorator(login_required, name='dispatch')
class AnswerLikeCreateVeiw(CreateView):
    model = Answer
    template_name = 'questions/posts/detail.html'
    success_url = reverse_lazy('questions:question_detail')

    def post(self, request, pk):
        answer = get_object_or_404(Answer, id=request.POST.get('answer_id'))
        if answer.likes.filter(id=request.user.id).exists():
            answer.likes.remove(request.user)
        else:
            answer.likes.add(request.user)

        related_question_id = answer.related_question.id
        return HttpResponseRedirect(reverse('questions:question_detail', args=[str(related_question_id), answer.related_question.slug]))



@method_decorator(login_required, name='dispatch')
class QuestionLikeCreateView(CreateView):
    model = Question
    template_name = 'questions/posts/detail.html'
    success_url = reverse_lazy('questions:question_detail')

    def post(self, request, pk):
        question = get_object_or_404(Question, id=request.POST.get('question_id'))
        if question.likes.filter(id=request.user.id).exists():
            question.likes.remove(request.user)
        else:
            question.likes.add(request.user)

        return HttpResponseRedirect(reverse('questions:question_detail', args=[str(pk), question.slug]))



class QuestionDetailView(DetailView):
    model = Question
    template_name = 'questions/posts/detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['answers'] = self.object.question_answers.all()
        # answer = get_object_or_404(Answer, id=self.object.context['pk'])
        # context['category1'] = self.object.category

        """Handling likes for answers"""
        # answers = Answer.objects.filter(related_question=self.kwargs['pk'])
        answers = context['answers']
        answer_liked = {}
        for ans in answers:
            if ans.likes.filter(id=self.request.user.id).exists():
                answer_liked[ans.id] = True
        context['answer_liked'] = answer_liked

        """Handling likes for the questions"""
        question = get_object_or_404(Question, id=self.kwargs['pk'])
        question_liked = False
        if question.likes.filter(id=self.request.user.id).exists():
            question_liked = True
        context['question_liked'] = question_liked

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
        print("test11")
        if question_form.is_valid(): # doesnt pass this if!
            print("test12")
            cleaned_data = question_form.cleaned_data
            print("test13")
            current_user = request.user
            print("test14")
            question = Question(title=cleaned_data['title'], text=cleaned_data['text'], category=cleaned_data['category'], user=current_user)
            question.save(commit=False)
            print("test")
            list_of_tags = cleaned_data['tags'].split()
            tags_set = set({})
            tags_set.update(list_of_tags)
            for tag in tags_set:
                tag_obj = Tag.objects.get_object_or_create(title=tag.title)[0] # get_or_create returns a tuple!
                question.tags.add(*list(tags_set))

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
            return redirect('questions:question_detail', pk, question.slug)

@method_decorator(login_required, name='dispatch')
class QuestionReportCreateView(CreateView):
    model = QuestionReport
    template_name = 'questions/report/report_form.html'
    form_class = QuestionReportForm
    success_url = reverse_lazy('questions:report-success')


    def post(self, request, pk):
        report_form = QuestionReportForm(request.POST)
        if report_form.is_valid():
            cleaned_data = report_form.cleaned_data
            current_user = request.user
            reported_question = get_object_or_404(Question, id=pk)
            report = QuestionReport(reported_question=reported_question, title=cleaned_data['title'], additional_message=cleaned_data['additional_message'], user=current_user)
            report.save()
            return redirect('questions:report-success')


@method_decorator(login_required, name='dispatch')
class AnswerReportCreateView(CreateView):
    model = AnswerReportForm
    template_name = 'questions/report/report_form.html'
    form_class = AnswerReportForm
    success_url = reverse_lazy('questions:report-success')


    def post(self, request, pk):
        report_form = AnswerReportForm(request.POST)
        if report_form.is_valid():
            cleaned_data = report_form.cleaned_data
            current_user = request.user
            reported_answer = get_object_or_404(Question, id=pk)
            report = AnswerReport(reported_answer=reported_answer, title=cleaned_data['title'], additional_message=cleaned_data['additional_message'], user=current_user)
            report.save()
            return redirect('questions:report-success')


class ReportSuccessTemplateView(TemplateView):
    template_name = template_name = 'questions/report/success_template.html'

