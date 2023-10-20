from django.shortcuts import render, redirect
from django.core.mail import send_mail

from .models import About, Skill, Project, Service, Contact
from .forms import ContactForm
# Create your views here.


def home(request):
    abouts = About.objects.all()
    skills = Skill.objects.all()
    personal_projects = Project.objects.filter(type='personal').order_by('-id')
    contributions_projects = Project.objects.filter(type='contributions').order_by('-id')
    services = Service.objects.order_by('id')
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Save the contact message to the database
            contact_message = Contact(name=name, email=email, message=message)
            contact_message.save()
            # form.save()

            # Send an email
            send_mail(
                f'Inquiry from {name}... email address: {email}',
                message,
                email,
                ['ifeoluwasamson90@gmail.com'],  # Replace with your email address
            )

            return redirect('home')  # Redirect to a thank you page
    else:
        form = ContactForm()
    
    context = {
        'abouts': abouts,
        'skills': skills,
        'personals': personal_projects,
        'contributions': contributions_projects,
        'services': services,
        'form': form,
    }

    return render(request, 'pages/home.html', context)


# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Save the contact message to the database
#             form.save()

#             # Send an email
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             send_mail(
#                 f'Contact Form Submission from {name}',
#                 message,
#                 email,
#                 ['ifeoluwasamson90@gmail.com'],  # Replace with your email address
#             )

#             return redirect('home')  # Redirect to a thank you page
#     else:
#         form = ContactForm()

#     return render(request, 'contact_form.html', {'form': form})