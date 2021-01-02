from django import forms
from questions.models import Question, Answer, QuestionReport, AnswerReport

class QuestionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['tags'].required = False
    class Meta:
        model = Question
        fields = ('title', 'text', 'category', 'tags' )
        widgets = {
            'tags': forms.Textarea(attrs={'cols': 80, 'rows': 1}),
        }

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
