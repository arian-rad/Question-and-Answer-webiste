from django.views.generic import CreateView, UpdateView, TemplateView, DetailView, ListView
from accounts.models import User, Notification
from accounts.forms import SignupForm, EditProfileForm, PasswordResetForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, get_object_or_404, redirect


class EditPasswordView(PasswordChangeView):
    form_class = PasswordResetForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('accounts:pass_success')


class SignupCreateView(CreateView):
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('accounts:login')


class EditProfileView(UpdateView):
    model = User
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('questions:all_questions')


class PasswordChangeSuccessView(TemplateView):
    template_name = 'registration/change-pass-success.html'


class ShowProfileView(DetailView):
    model = User
    template_name = 'accounts/profile_page.html'


class NotificationView(ListView):
    model = Notification
    template_name = 'accounts/all_notifications.html'
