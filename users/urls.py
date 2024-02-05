from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import TemplateView

from users.apps import UsersConfig
from users.views import LoginUserView, RegisterUserView, VerifyEmailView, ProfileUserView

app_name = UsersConfig.name


urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('invalid_verify/', TemplateView.as_view(template_name='users/invalid_verify.html'), name='invalid_verify'),
    path('verify/<uidb64>/<token>/', VerifyEmailView.as_view(), name='verify'),
    path('confirm_email/', TemplateView.as_view(template_name='users/confirm_email.html'), name='confirm_email'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileUserView.as_view(), name='profile'),
]