from django.shortcuts import render
from .models import Course


def index(request, template_name='courses.html'):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, template_name, context)


def details(request, pk, template_name='details.html'):
    course = Course.objects.get(pk=id)
    context = {
        'course': course
    }
    return render(request, context, template_name)
