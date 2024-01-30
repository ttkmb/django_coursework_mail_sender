from django.contrib import admin

from mailer.models import Mailer, MailerLogger, MailerMessage

# Register your models here.
admin.site.register(Mailer)
admin.site.register(MailerLogger)
admin.site.register(MailerMessage)