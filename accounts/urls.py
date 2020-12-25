from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views as account_views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', account_views.SignupCreateView.as_view(), name='signup'),
]