from django.shortcuts import render
from .models import Skill, Profile
from django.views import generic

# Create your views here.
def about(request):
    # num_profiles = Profile.objects.count()
    # num_skills = Skill.objects.count()
    # profiles = Profile.objects.all()

    context = {
        'num_profiles': Profile.objects.count(),
        'num_skills': Skill.objects.count(),
        'profiles': Profile.objects.all()
    }

    return render(request, 'about.html', context=context)


class ProfileDetailView(generic.DetailView):
    model = Profile
