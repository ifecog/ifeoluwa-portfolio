from django.shortcuts import render, redirect
from .models import About, Skill, Project, Service
# Create your views here.


def home(request):
    abouts = About.objects.all()
    skills = Skill.objects.all()
    personal_projects = Project.objects.filter(type='personal').order_by('-id')
    contributions_projects = Project.objects.filter(type='contributions').order_by('-id')
    services = Service.objects.order_by('-id')
    
    context = {
        'abouts': abouts,
        'skills': skills,
        'personals': personal_projects,
        'services': services,
    }

    return render(request, 'pages/home.html', context)


