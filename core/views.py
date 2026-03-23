from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import (
    Profile, SkillCategory, Education, Achievement,
    Experience, Project, ProjectCategory, ContactMessage
)


def home(request):
    profile = Profile.objects.first()
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    educations = Education.objects.all()
    achievements = Achievement.objects.all()
    experiences = Experience.objects.prefetch_related('technologies', 'achievements').all()
    project_categories = ProjectCategory.objects.all()
    projects = Project.objects.prefetch_related('tags').filter(is_featured=True)
    active_category = request.GET.get('category', 'all')

    if active_category and active_category != 'all':
        projects = projects.filter(category__slug=active_category)

    context = {
        'profile': profile,
        'skill_categories': skill_categories,
        'educations': educations,
        'achievements': achievements,
        'experiences': experiences,
        'project_categories': project_categories,
        'projects': projects,
        'active_category': active_category,
    }
    return render(request, 'core/index.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message_text = request.POST.get('message', '').strip()

        if name and email and subject and message_text:
            # Save to DB
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message_text,
            )
            # Optionally send email
            try:
                profile = Profile.objects.first()
                if profile:
                    send_mail(
                        subject=f"Portfolio Contact: {subject}",
                        message=f"From: {name} <{email}>\n\n{message_text}",
                        from_email=settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@portfolio.com',
                        recipient_list=[profile.email],
                        fail_silently=True,
                    )
            except Exception:
                pass

            messages.success(request, 'Your message has been sent successfully!')
        else:
            messages.error(request, 'Please fill in all required fields.')

    return redirect('home')
