from django import forms
from django.conf import settings
# Never import settings, porque só importo o settings.py, no from eu
# importo aquele arquivo inclusive os settings do DJANGO

from src.apps.core.mail import send_mail_template


class ContactCourse(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', required=False)
    message = forms.CharField(
        label='Mensagem/Dúvida', widget=forms.Textarea
    )

    def send_mail(self, course):
        subject = ('Curso: {}'.format(course))
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
        }
        template_name = 'contact_email.html'
        send_mail_template(
            subject, template_name, context, [settings.CONTACT_EMAIL]
        )
