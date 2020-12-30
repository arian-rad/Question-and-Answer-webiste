from django import forms
from questions.models import Question, Answer, Report

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'text', 'category')

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('body',)

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('title', 'additional_message',)
