from django.db import models


# TODO cascade updates, deletes etc.
# TODO help text
# TODO explore other Charfield Params
# TODO


# Create your models here.
class Skills(models.Model):
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
    skills = models.ManyToManyField(Skills, help_text='Select skills for this profile')
    name = models.CharField(max_length=50, help_text='Enter your real name')
    display_name = models.CharField(max_length=50, blank=True, help_text='Enter your preferred display name')
    email = models.EmailField(help_text='Enter your email address')
    about = models.CharField(max_length=1000, help_text='Provide a little bit of detail about yourself')
    spoken_languages = models.CharField(max_length=200,
                                        help_text='List the languages you speak including proficiency level')

    # TODO: Fields should be moved into a separate 'Sites' class in the future to make this app more flexible
    github = models.URLField(help_text='Provide a link to your GitHub page')
    linkedin = models.URLField(help_text='Provide a link to your LinkedIn page')

    # Metadata
    class Meta:
        ordering = ['name']

    # Methods
    # def get_absolute_url(self):
    #     """Returns the url to access a particular instance of MyModelName."""
    #     return reverse('model-detail-view', args=[str(self.id)])
    #
    def __str__(self):
        return self.name


class WorkExperience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    company = models.CharField(max_length=50)
    company_alias = \
        models.CharField(max_length=100, blank=True,
                         help_text='If you do not want to display company name, provide an alias description')
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    job_title = models.CharField(max_length=100)
    duties = models.CharField(max_length=1500)

    # Metadata
    class Meta:
        ordering = ['-start_date']

    # Methods
    def __str__(self):
        return self.skill


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
