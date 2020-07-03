from django.contrib import admin
from .models import Skill, Profile, WorkExperience, ProjectExperience

# Register your models here.
#admin.site.register(Skill)
#admin.site.register(Profile)
#admin.site.register(WorkExperience)
#admin.site.register(ProjectExperience)


# Customise admin classes
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'display_skills')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill','category')


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'company', 'job_title')


@admin.register(ProjectExperience)
class ProjectExperienceAdmin(admin.ModelAdmin):
    list_display = ('project_title', 'programming_languages')
