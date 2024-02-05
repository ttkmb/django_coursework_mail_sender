from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from client.forms import ClientForm
from client.models import Client


class ClientListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Client
    template_name = 'client/client_list.html'
    permission_required = 'client.view_client'


class ClientCreateView(CreateView):
    model = Client
    form = ClientForm
    template_name = 'client/client_create.html'
    fields = ['email', 'fullname', 'comment', 'owner']
    extra_context = {'title': 'Создание нового клиента'}
    success_url = reverse_lazy('client:client_list')


class ClientUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'client/client_create.html'
    extra_context = {'title': 'Редактирование клиента'}
    success_url = reverse_lazy('client:client_list')
    permission_required = 'client.change_client'


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('client:client_list')


class ClientDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Client
    permission_required = 'client.view_client'
