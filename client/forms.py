from django import forms

from client.models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['email', 'fullname', 'comment']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }