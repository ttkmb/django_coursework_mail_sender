from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from client.forms import ClientForm
from client.models import Client


class ClientListView(ListView):
    model = Client
    template_name = 'client/client_list.html'


class ClientCreateView(CreateView):
    model = Client
    form = ClientForm
    template_name = 'client/client_create.html'
    fields = ['email', 'fullname', 'comment']
    extra_context = {'title': 'Создание нового клиента'}
    success_url = reverse_lazy('client:client_list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'client/client_create.html'
    extra_context = {'title': 'Редактирование клиента'}
    success_url = reverse_lazy('client:client_list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('client:client_list')


class ClientDetailView(DetailView):
    model = Client
