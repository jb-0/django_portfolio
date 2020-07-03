from django.contrib import admin
from .models import Skill, Profile, WorkExperience, ProjectExperience

# Register your models here.
#admin.site.register(Skill)
#admin.site.register(Profile)
#admin.site.register(WorkExperience)
#admin.site.register(ProjectExperience)


# Customise admin classes
class WorkExperienceInline(admin.TabularInline):
    model = WorkExperience
    extra = 0

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'display_skills')
    list_filter = ('skills',)
    # fields = [('name','display_name'), 'email', 'about', 'spoken_languages', ('github', 'linkedin'), 'skills']
    fieldsets = (
        ('Personal Details', {
            'fields': (('name', 'display_name'), 'email', 'about')
        }),
        ('Attributes', {
            'fields': ('spoken_languages', ('github', 'linkedin'), 'skills')
        })
    )
    inlines = [WorkExperienceInline]

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill', 'category')
    list_filter = ('category',)


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'company', 'job_title')


@admin.register(ProjectExperience)
class ProjectExperienceAdmin(admin.ModelAdmin):
    list_display = ('project_title', 'programming_languages')
