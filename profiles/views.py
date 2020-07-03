from django.shortcuts import render
from .models import Skill, Profile


# Create your views here.
def index(request):
    num_profiles = Profile.objects.count()
    num_skills = Skill.objects.count()

    context = {
        'num_profiles': num_profiles,
        'num_skills': num_skills
    }

    return render(request, 'index.html', context=context)

