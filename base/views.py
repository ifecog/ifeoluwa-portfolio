from django.shortcuts import render, redirect
from .models import About

# Create your views here.


def home(request):
    abouts = About.objects.all()
    context = {
        'abouts': abouts,
    }

    return render(request, 'pages/home.html', context)


