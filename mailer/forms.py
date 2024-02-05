from django import forms

from client.models import Client
from mailer.models import MailerMessage, Mailer


class MessageForm(forms.ModelForm):
    class Meta:
        model = MailerMessage
        fields = ['title', 'message', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }


class SettingsForm(forms.ModelForm):
    STATUS_CHOICES = [
        ('DRAFT', 'Черновик'),
        ('COMPLETE', 'Завершено'),
        ('CREATED', 'Создано'),
        ('LAUNCHED', 'Запущено'),
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES, label='Статус',
                               widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Mailer
        fields = ['title', 'time_start', 'time_stop', 'frequency', 'status', 'mail', 'clients']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'time_start': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'time_stop': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'frequency': forms.Select(attrs={'class': 'form-control'}),
            'mail': forms.Select(attrs={'class': 'form-control'}),
            'clients': forms.SelectMultiple(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['clients'].queryset = Client.objects.filter(owner=user)
        self.fields['mail'].queryset = MailerMessage.objects.filter(author=user)


class ModeratorForm(forms.ModelForm):
    STATUS_CHOICES = [
        ('DRAFT', 'Черновик'),
        ('COMPLETE', 'Завершено'),
        ('CREATED', 'Создано'),
        ('LAUNCHED', 'Запущено'),
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES, label='Статус',
                               widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Mailer
        fields = ['status']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['status'].queryset = Mailer.objects.filter(owner=user)