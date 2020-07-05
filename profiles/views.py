from django.shortcuts import render
from .models import Skill, Profile
from django.views import generic


# Create your views here.
def index(request):
    num_profiles = Profile.objects.count()
    num_skills = Skill.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_profiles': num_profiles,
        'num_skills': num_skills,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)


class ProfileListView(generic.ListView):
    model = Profile
    context_object_name = 'my_profile_list'  # your own name for the list as a template variable


class ProfileDetailView(generic.DetailView):
    model = Profile