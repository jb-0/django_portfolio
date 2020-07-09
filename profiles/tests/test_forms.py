from django.test import TestCase
from profiles.forms import NewProfileForm


class NewProfileFormTest(TestCase):
    def test_new_profile_form_name_label(self):
        form = NewProfileForm()
        self.assertTrue(form.fields['name'].label is None or form.fields['name'].label == 'Name')

    def test_new_profile_form_email_label(self):
        form = NewProfileForm()
        self.assertTrue(form.fields['email'].label is None or form.fields['email'].label == 'Email')

    def test_new_profile_form_about_label(self):
        form = NewProfileForm()
        self.assertTrue(form.fields['about'].label is None or form.fields['about'].label == 'About')

    def test_new_profile_form_skills_label(self):
        form = NewProfileForm()
        self.assertTrue(form.fields['skills'].label is None or form.fields['skills'].label == 'Skills')

    def test_new_profile_form_name_is_blank(self):
        # With other values valid, assert that blank name is not valid
        form = NewProfileForm(data={'name': '', 'email': 'some@where.com', 'about': 'This is an about',
                                    'skills': (1, 2)})
        self.assertFalse(form.is_valid())
