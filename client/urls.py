from django.urls import path

from client import views
from client.apps import ClientConfig
from client.views import ClientListView

app_name = ClientConfig.name

urlpatterns = [
    path('list/', ClientListView.as_view(), name='client_list'),
    path('create/', views.ClientCreateView.as_view(), name='client_create'),
    path('update/<int:pk>/', views.ClientUpdateView.as_view(), name='client_update'),
    path('delete/<int:pk>/', views.ClientDeleteView.as_view(), name='client_delete'),
    path('client/<int:pk>/', views.ClientDetailView.as_view(), name='client_detail'),
]