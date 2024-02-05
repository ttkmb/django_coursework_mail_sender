from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms


class LoginUserForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'password': forms.PasswordInput(attrs={'class': 'form-input'}),
        }


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким E-mail уже существует')
        return email


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'avatar', 'phone_number', 'country')

