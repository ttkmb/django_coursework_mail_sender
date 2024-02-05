from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.views.generic import FormView, UpdateView

from users.forms import LoginUserForm, RegisterUserForm, UserProfileForm
from users.services import send_email_for_verify


class LoginUserView(LoginView):
    template_name = 'users/login.html'
    form_class = LoginUserForm

    def get_success_url(self):
        return reverse_lazy('mailer:index')


class RegisterUserView(FormView):
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:confirm_email')
    form_class = RegisterUserForm

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        user = authenticate(email=email, password=password)
        if not user.is_verified:
            send_email_for_verify(self.request, user)
        return super().form_valid(form)


class LogoutUserView(LogoutView):
    pass


class VerifyEmailView(View):
    template_name = 'users/verify.html'

    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)
        if user is not None and default_token_generator.check_token(user, token):
            user.is_verified = True
            user.save()
            login(request, user)
            return redirect('mailer:index')
        else:
            return redirect('users:invalid_verify')

    @staticmethod
    def get_user(uidb64):
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_user_model().objects.get(pk=uid)
        return user


class ProfileUserView(UpdateView):
    template_name = 'users/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self):
        return self.request.user
