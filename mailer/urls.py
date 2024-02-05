from django.urls import path

from mailer.apps import MailerConfig
from mailer.views import MessageListView, MessageCreateView, MessageUpdateView, MessageDetailView, MessageDeleteView, \
    SettingsListView, SettingsCreateView, SettingsDeleteView, SettingsUpdateView, SettingsDetailView, IndexTemplateView

app_name = MailerConfig.name

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('list/', MessageListView.as_view(), name='message_list'),
    path('create/', MessageCreateView.as_view(), name='message_create'),
    path('update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('detail/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),

    path('settings/list/', SettingsListView.as_view(), name='settings_list'),
    path('settings/create/', SettingsCreateView.as_view(), name='settings_create'),
    path('settings/delete/<int:pk>/', SettingsDeleteView.as_view(), name='settings_delete'),
    path('settings/update/<int:pk>/', SettingsUpdateView.as_view(), name='settings_update'),
    path('settings/detail/<int:pk>/', SettingsDetailView.as_view(), name='settings_detail'),
]
