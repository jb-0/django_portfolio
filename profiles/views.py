from django.shortcuts import render
from .models import Skill, Profile
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


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


class ProfileDetailView(LoginRequiredMixin, generic.DetailView):
    def get_queryset(self):
        return Profile.objects.filter(user_account=self.request.user)
    #model = Profile