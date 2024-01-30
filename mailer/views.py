from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, TemplateView

from mailer.forms import MessageForm, SettingsForm
from mailer.models import MailerMessage, Mailer


class IndexTemplateView(TemplateView):
    template_name = 'mailer/index.html'


'''
Классы для работы с сообщениями
'''


class MessageListView(ListView):
    model = MailerMessage
    template_name = 'mailer/message_list.html'


class MessageCreateView(CreateView):
    model = MailerMessage
    template_name = 'mailer/message_create.html'
    form_class = MessageForm
    extra_context = {'title': 'Создать сообщение', 'button': 'Создать'}
    success_url = reverse_lazy('mailer:message_list')


class MessageDeleteView(DeleteView):
    model = MailerMessage
    success_url = reverse_lazy('mailer:message_list')


class MessageUpdateView(UpdateView):
    model = MailerMessage
    template_name = 'mailer/message_create.html'
    form_class = MessageForm
    extra_context = {'title': 'Изменить сообщение', 'button': 'Изменить'}
    success_url = reverse_lazy('mailer:message_list')


class MessageDetailView(DetailView):
    model = MailerMessage
    template_name = 'mailer/message_detail.html'


'''
Классы для работы с настройками рассылки
'''


class SettingsListView(ListView):
    model = Mailer
    template_name = 'mailer/settings_list.html'


class SettingsCreateView(CreateView):
    model = Mailer
    template_name = 'mailer/settings_create.html'
    form_class = SettingsForm
    extra_context = {'title': 'Задать настройки для рассылки', 'button': 'Задать'}
    success_url = reverse_lazy('mailer:settings_list')


class SettingsDeleteView(DeleteView):
    model = Mailer
    success_url = reverse_lazy('mailer:settings_list')


class SettingsUpdateView(UpdateView):
    model = Mailer
    template_name = 'mailer/settings_create.html'
    form_class = SettingsForm
    extra_context = {'title': 'Изменить настройки для рассылки', 'button': 'Изменить'}
    success_url = reverse_lazy('mailer:settings_list')


class SettingsDetailView(DetailView):
    model = Mailer
    template_name = 'mailer/settings_detail.html'
