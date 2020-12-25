from django.views.generic import CreateView
from accounts.models import User
from accounts.forms import SignupForm
from django.urls import reverse_lazy

class SignupCreateView(CreateView):
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('accounts:login')


