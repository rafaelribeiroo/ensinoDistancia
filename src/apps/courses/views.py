from django.shortcuts import render


def courses(request, template_name='courses.html'):
    return render(request, template_name)
