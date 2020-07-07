from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User

# TODO cascade updates, deletes etc.
# TODO help text
# TODO explore other Charfield Params


# Create your models here.
class Skill(models.Model):
    # Fields
    skill = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

    # Metadata
    class Meta:
        ordering = ['category', 'skill']

    # Methods
    def __str__(self):
        return self.skill


class Profile(models.Model):
    # Fields
    user_account = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    skills = models.ManyToManyField(Skill, help_text='Select skills for this profile')
    name = models.CharField(max_length=50, help_text='Enter your real name')
    display_name = models.CharField(max_length=50, blank=True, help_text='Enter your preferred display name')
    email = models.EmailField(help_text='Enter your email address')
    about = models.CharField(max_length=1000, help_text='Provide a little bit of detail about yourself')
    spoken_languages = models.CharField(blank=True, max_length=200,
                                        help_text='List the languages you speak including proficiency level')

    # TODO: Fields should be moved into a separate 'Sites' class in the future to make this app more flexible
    github = models.URLField(blank=True, help_text='Provide a link to your GitHub page')
    linkedin = models.URLField(blank=True, help_text='Provide a link to your LinkedIn page')

    # Metadata
    class Meta:
        ordering = ['name']

    # Methods
    def get_absolute_url(self):
        return reverse('profile-detail', args=[str(self.id)])

    def display_skills(self):
        # Return 3 skills
        # TODO if there are more than 3 then a trailing "..." should be added
        return ', '.join(skill.skill for skill in self.skills.all()[:3])



    def __str__(self):
        return self.name


class WorkExperience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    company = models.CharField(max_length=50)
    company_alias = \
        models.CharField(max_length=100, blank=True,
                         help_text='If you do not want to display company name, provide an alias description')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    job_title = models.CharField(max_length=100)
    duties = models.CharField(max_length=1500)

    # Metadata
    class Meta:
        ordering = ['-start_date']

    # Methods
    def __str__(self):
        return self.job_title


class ProjectExperience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project_title = models.CharField(max_length=100)
    duties = models.CharField(max_length=1500)
    programming_languages = models.CharField(max_length=200)
    link = models.URLField()

    # Metadata
    class Meta:
        ordering = ['project_title']

    # Methods
    def __str__(self):
        return self.project_title
