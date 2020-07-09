from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import Skill


class NewProfileForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    about = forms.CharField()

    choice_values = Skill.objects.values_list('id', 'skill')
    skills = forms.MultipleChoiceField(choices=choice_values)

    # We should always clean user input
    def clean_profile_data(self):
        data = {'name': self.cleaned_data['name'],
                'email': self.cleaned_data['email'],
                'about': self.cleaned_data['about'],
                'skills': self.cleaned_data['skills']}

        if not data['name']:
            raise ValidationError(_('Invalid name - name field is blank'))

        # TODO any further validation? Email shouldn't exist in DB?

        return data

