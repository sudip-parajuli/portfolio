# portfolio/views.py
import os

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string


from .models import Profile, Skill, Education, Experience, Project
from .forms import ContactForm


def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    projects = Project.objects.all()

    # Check if success is stored in the session
    success = request.session.pop('form_success', False)

    # Handle contact form submission
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['form_success'] = True  # Store success in session
            return redirect('/#contact')  # Redirect to the contact section
    else:
        form = ContactForm()

    return render(request, 'portfolio/home.html', {
        'profile': profile,
        'skills': skills,
        'educations': educations,
        'experiences': experiences,
        'projects': projects,
        'form': form,
        'success': success,  # Pass the success state to the template
    })

# def download_cv(request):
#     cv_path = 'media/cvs/sudip_cv.pdf'  # Update this path to where your CV PDF is stored
#     if os.path.exists(cv_path):
#         with open(cv_path, 'rb') as pdf:
#             response = HttpResponse(pdf.read(), content_type='application/pdf')
#             response['Content-Disposition'] = 'attachment; filename="Sudip_Parajuli_CV.pdf"'
#             return response
#     else:
#         return HttpResponse("CV not found.", status=404)