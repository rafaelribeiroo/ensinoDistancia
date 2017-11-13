from django.shortcuts import render, get_object_or_404

from .models import Course
from .forms import ContactCourse


def index(request, template_name='courses.html'):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, template_name, context)


'''def details(request, pk, template_name='details.html'):
    course = get_object_or_404(Course, pk=id)
    context = {
        'course': course
    }
    return render(request, context, template_name)
'''


def details(request, slug, template_name='details.html'):
    course = get_object_or_404(Course, slug=slug)
    if request.method == 'POST':
        form = ContactCourse(request.POST)
    else:
        form = ContactCourse()
    context = {
        'course': course,
        'form': form,
    }
    return render(request, template_name, context)
