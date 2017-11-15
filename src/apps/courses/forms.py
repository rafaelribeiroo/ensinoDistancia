from django import forms
from django.core.mail import send_mail
from django.conf import settings
# Never import settings, porque só importo o settings.py, no from eu
# importo aquele arquivo inclusive os settings do DJANGO


class ContactCourse(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', required=False)
    message = forms.CharField(
        label='Mensagem/Dúvida', widget=forms.Textarea
    )

    def send_mail(self, course):
        subject = '[%s] Contato' % course
        message = 'Nome: %(name)s;Email: %(email)s;%(message)s'
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
        }
        message = message % context
        send_mail(
            subject, message, settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_EMAIL]
        )
