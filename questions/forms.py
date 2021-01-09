from django import forms
from questions.models import Question, Answer, QuestionReport, AnswerReport

class QuestionForm(forms.ModelForm):
    tag_input = forms.CharField(label='Tags')

    class Meta:
        model = Question
        fields = ('title', 'text', 'category',)


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('body',)

class QuestionReportForm(forms.ModelForm):
    class Meta:
        model = QuestionReport
        fields = ('title', 'additional_message',)


class AnswerReportForm(forms.ModelForm):
    class Meta:
        model = AnswerReport
        fields = ('title', 'additional_message',)
