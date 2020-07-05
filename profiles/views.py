from django.shortcuts import render
from .models import Skill, Profile
from django.views import generic


# Create your views here.
def index(request):
    num_profiles = Profile.objects.count()
    num_skills = Skill.objects.count()

    context = {
        'num_profiles': num_profiles,
        'num_skills': num_skills
    }

    return render(request, 'index.html', context=context)


class ProfileListView(generic.ListView):
    model = Profile
    context_object_name = 'my_profile_list'  # your own name for the list as a template variable
    #queryset = Profile.objects.filter(name__icontains='Tony')[:5]  # Get 5 names containing Tony
    paginate_by = 1


class ProfileDetailView(generic.DetailView):
    model = Profile