from django.shortcuts import render, get_object_or_404

from .models import Course
from .forms import ContactCourse
# Boas práticas: Deixar a view com menos lógica possíve, mantenha seus métodos e regras de negócio em módulos separados (Deixar ela enxuta)

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
    context = {}
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            print(form.cleaned_data)
            # print(form.cleaned_data['name'])
            form.send_mail(course)
            form = ContactCourse()
    else:
        form = ContactCourse()
    context['form'] = form
    context['course'] = course
    return render(request, template_name, context)
