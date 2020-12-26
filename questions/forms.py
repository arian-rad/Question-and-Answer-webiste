from django import forms
from questions.models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'text', 'category')

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('body', )