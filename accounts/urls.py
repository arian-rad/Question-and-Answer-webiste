from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views as account_views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', account_views.SignupCreateView.as_view(), name='signup'),
    path('profile/<int:pk>/edit/', account_views.EditProfileView.as_view(), name='edit_profile'),
    path('profile/<int:pk>/page/', account_views.ShowProfileView.as_view(), name='view_profile_page'),
    path('password/', account_views.EditPasswordView.as_view(), name='pass_change'),
    path('password-change/success/', account_views.PasswordChangeSuccessView.as_view(), name='pass_success'),

]
