from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile, Skill


class AboutViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for p in range(5):
            Profile.objects.create(name=f"{p}Simon Says", email=f"{p}simon@says.com", about=f"{p}Test purposes")

        # Create two users
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')

        test_user1.save()
        test_user2.save()

    def test_about_view_url_exists_at_desired_location(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_about_view_accessible_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_about_view_uses_correct_template(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/about.html')


class ProfileDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for p in range(5):
            Profile.objects.create(name=f"{p}Simon Says", email=f"{p}simon@says.com", about=f"{p}Test purposes")

        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user1.save()

    def test_profile_detail_redirect_if_not_logged_in(self):
        response = self.client.get('/about/1')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/about/1')

    def test_profile_detail_logged_in_uses_correct_template(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get('/about/1')
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile_detail.html')


class NewProfileViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for p in range(5):
            Profile.objects.create(name=f"{p}Simon Says", email=f"{p}simon@says.com", about=f"{p}Test purposes")

        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user1.save()

        Skill.objects.create(skill="Test Skill", category="Test Skill Category")

    def test_new_profile_redirect_if_not_logged_in(self):
        response = self.client.get('/about/new-profile/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/about/new-profile/')

    def test_profile_detail_logged_in_uses_correct_template(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get('/about/new-profile/')
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/new_profile.html')

    def test_profile_detail_about_has_correct_initial_value(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get('/about/new-profile/')
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].initial['about'], 'Tell us about yourself')

    def test_profile_detail_redirects_to_about_on_success(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.post(reverse('new-profile'), {'name': 'Test',
                                                             'about': 'Test',
                                                             'email': 'Test@sd.com',
                                                             'skills': Skill.objects.get(id=1)})
        self.assertRedirects(response, reverse('about'))

    def test_profile_detail_invalid_name(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.post(reverse('new-profile'), {'name': '',
                                                             'about': 'Test',
                                                             'email': 'Test@sd.com',
                                                             'skills': Skill.objects.get(id=1)})
        self.assertFormError(response, 'form', 'name', 'This field is required.')