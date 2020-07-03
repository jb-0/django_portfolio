from django.contrib import admin
from .models import Skill, Profile, WorkExperience, ProjectExperience


# Register your models here.
admin.site.register(Skill)
admin.site.register(Profile)
admin.site.register(WorkExperience)
admin.site.register(ProjectExperience)
