from django.shortcuts import render
from .models import Skill, Profile
from django.views import generic


# Create your views here.
def about(request):
    num_profiles = Profile.objects.count()
    num_skills = Skill.objects.count()

    context = {
        'num_profiles': num_profiles,
        'num_skills': num_skills,
    }

    return render(request, 'about.html', context=context)


class ProfileListView(generic.ListView):
    model = Profile
    context_object_name = 'my_profile_list'  # your own name for the list as a template variable


class ProfileDetailView(generic.DetailView):
    model = Profile