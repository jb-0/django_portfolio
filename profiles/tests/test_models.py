from django.test import TestCase
from profiles.models import Skill, Profile, WorkExperience, ProjectExperience


class ProfileModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Profile.objects.create(name="Simon Says", email="simon@says.com", about="Test purposes")

    ############################################################################################
    # Verbose name tests
    def test_user_account_label(self):
        profile_instance = Profile.objects.get(id=1)
        field_label = profile_instance._meta.get_field('user_account').verbose_name
        self.assertEquals(field_label, 'user account')

    def test_skills_label(self):
        profile_instance = Profile.objects.get(id=1)
        field_label = profile_instance._meta.get_field('skills').verbose_name
        self.assertEquals(field_label, 'skills')

    def test_name_label(self):
        profile_instance = Profile.objects.get(id=1)
        field_label = profile_instance._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_display_name_label(self):
        profile_instance = Profile.objects.get(id=1)
        field_label = profile_instance._meta.get_field('display_name').verbose_name
        self.assertEquals(field_label, 'display name')

    def test_email_label(self):
        profile_instance = Profile.objects.get(id=1)
        field_label = profile_instance._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_about_label(self):
        profile_instance = Profile.objects.get(id=1)
        field_label = profile_instance._meta.get_field('about').verbose_name
        self.assertEquals(field_label, 'about')

    def test_spoken_languages_label(self):
        profile_instance = Profile.objects.get(id=1)
        field_label = profile_instance._meta.get_field('spoken_languages').verbose_name
        self.assertEquals(field_label, 'spoken languages')

    def test_github_label(self):
        profile_instance = Profile.objects.get(id=1)
        field_label = profile_instance._meta.get_field('github').verbose_name
        self.assertEquals(field_label, 'github')

    def test_linkedin_label(self):
        profile_instance = Profile.objects.get(id=1)
        field_label = profile_instance._meta.get_field('linkedin').verbose_name
        self.assertEquals(field_label, 'linkedin')

    ############################################################################################
    # Max length tests
    def test_name_max_length(self):
        profile_instance = Profile.objects.get(id=1)
        max_length = profile_instance._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_display_name_max_length(self):
        profile_instance = Profile.objects.get(id=1)
        max_length = profile_instance._meta.get_field('display_name').max_length
        self.assertEquals(max_length, 50)

    def test_about_max_length(self):
        profile_instance = Profile.objects.get(id=1)
        max_length = profile_instance._meta.get_field('about').max_length
        self.assertEquals(max_length, 1000)

    def test_spoken_languages_max_length(self):
        profile_instance = Profile.objects.get(id=1)
        max_length = profile_instance._meta.get_field('spoken_languages').max_length
        self.assertEquals(max_length, 200)

    ############################################################################################
    # Custom methods tests
    def test_get_absolute_url(self):
        profile_instance = Profile.objects.get(id=1)
        self.assertEquals(profile_instance.get_absolute_url(), '/about/1')

    def test_display_skills(self):
        profile_instance = Profile.objects.get(id=1)
        Skill.objects.create(skill="Test1", category="Test1")
        Skill.objects.create(skill="Test2", category="Test2")
        profile_instance.skills.add(1)
        profile_instance.skills.add(2)
        self.assertEquals(profile_instance.display_skills(), 'Test1, Test2')