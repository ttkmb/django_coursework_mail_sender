from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, TemplateView

from mailer.forms import MessageForm, SettingsForm, ModeratorForm
from mailer.models import MailerMessage, Mailer


class IndexTemplateView(TemplateView):
    template_name = 'mailer/index.html'


'''
Классы для работы с сообщениями
'''


class MessageListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = MailerMessage
    template_name = 'mailer/message_list.html'
    login_url = reverse_lazy('users:login')
    permission_required = 'mailer.view_mailer'


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = MailerMessage
    template_name = 'mailer/message_create.html'
    form_class = MessageForm
    extra_context = {'title': 'Создать сообщение', 'button': 'Создать'}
    success_url = reverse_lazy('mailer:message_list')
    login_url = reverse_lazy('users:login')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = MailerMessage
    success_url = reverse_lazy('mailer:message_list')


class MessageUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = MailerMessage
    template_name = 'mailer/message_create.html'
    form_class = MessageForm
    extra_context = {'title': 'Изменить сообщение', 'button': 'Изменить'}
    success_url = reverse_lazy('mailer:message_list')
    permission_required = 'mailer.change_mailermessage'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            return self.object
        raise PermissionError('Недостаточно прав для редактирования этого сообщения')


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = MailerMessage
    template_name = 'mailer/message_detail.html'


'''
Классы для работы с настройками рассылки
'''


class SettingsListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Mailer
    template_name = 'mailer/settings_list.html'
    login_url = reverse_lazy('users:login')
    permission_required = 'mailer.view_mailer'

    def get_queryset(self):
        if self.request.user.has_perm('mailer.view_mailer'):
            return self.model.objects.all()
        return self.model.objects.filter(owner=self.request.user)


class SettingsCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Mailer
    template_name = 'mailer/settings_create.html'
    form_class = SettingsForm
    extra_context = {'title': 'Задать настройки для рассылки', 'button': 'Задать'}
    success_url = reverse_lazy('mailer:settings_list')
    permission_required = 'mailer.add_mailer'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class SettingsDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailer
    success_url = reverse_lazy('mailer:settings_list')


class SettingsUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailer
    template_name = 'mailer/settings_create.html'
    extra_context = {'title': 'Изменить настройки для рассылки', 'button': 'Изменить'}
    success_url = reverse_lazy('mailer:settings_list')

    def get_form_class(self):
        if self.request.user == self.get_object().owner:
            return SettingsForm
        elif self.request.user.has_perm('mailer.change_mailer'):
            return ModeratorForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class SettingsDetailView(LoginRequiredMixin, DetailView):
    model = Mailer
    template_name = 'mailer/settings_detail.html'
