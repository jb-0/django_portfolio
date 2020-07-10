from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Skill, Profile
from .forms import NewProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required()
def new_profile(request):
    new_profile_instance = Profile()

    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = NewProfileForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            new_profile_instance.name = form.cleaned_data['name']
            new_profile_instance.email = form.cleaned_data['email']
            new_profile_instance.about = form.cleaned_data['about']
            new_profile_instance.save()

            # Many to many
            new_profile_instance.skills.add(*form.cleaned_data['skills'])

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('about'))

    # If this is a GET (or any other method) create the default form.
    else:
        form = NewProfileForm(initial={'about': 'Tell us about yourself'})

    context = {
        'form': form,
        'new_profile_instance': new_profile_instance,
    }

    return render(request, 'profiles/new_profile.html', context)


def about(request):
    context = {
        'num_profiles': Profile.objects.count(),
        'num_skills': Skill.objects.count(),
        'profiles': Profile.objects.all()
    }

    return render(request, 'profiles/about.html', context=context)


class ProfileDetailView(LoginRequiredMixin, generic.DetailView):
    model = Profile