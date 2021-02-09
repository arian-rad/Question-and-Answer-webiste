from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from accounts.models import User
from django import forms


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        for field_name in ['username', 'password', 'bio', 'profile_image']:
            self.fields[field_name].help_text = None
    first_name = forms.CharField(max_length=90)
    last_name = forms.CharField(max_length=90)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'phone', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for field_name in ['username', 'password1', 'password2']:
            self.fields[field_name].help_text = None

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) != 12:
            raise forms.ValidationError('invalid phone number')


class EditProfileForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        for field_name in ['username', 'password']:
            self.fields[field_name].help_text = None

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'bio', 'profile_image')


class PasswordResetForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=20, widget=forms.PasswordInput())
    new_password1 = forms.CharField(label='New password', max_length=20, widget=forms.PasswordInput())
    new_password2 = forms.CharField(label='Confirm new password', max_length=20, widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        for field_name in ['old_password', 'new_password1', 'new_password2', ]:
            self.fields[field_name].help_text = None

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2',)
