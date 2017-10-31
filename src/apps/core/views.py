from django.shortcuts import render

# Create your views here.
def home(request, template_name='home.html'):
	return render(request, template_name)

def contact(request, template_name='contact.html'):
	return render(request, template_name)