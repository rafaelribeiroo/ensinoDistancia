from django.shortcuts import render
from .models import Course


def index(request, template_name='courses.html'):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, template_name, context)
