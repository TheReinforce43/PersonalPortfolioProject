from django.contrib import admin
from .models import (
    Profile, SkillCategory, Skill, Education, Achievement,
    Experience, ExperienceTechnology, ExperienceAchievement,
    ProjectCategory, Project, ProjectTag, ContactMessage
)


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    inlines = [SkillInline]


class ExperienceTechInline(admin.TabularInline):
    model = ExperienceTechnology
    extra = 1


class ExperienceAchievementInline(admin.TabularInline):
    model = ExperienceAchievement
    extra = 1


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    inlines = [ExperienceTechInline, ExperienceAchievementInline]
    list_display = ['title', 'company', 'start_date', 'end_date', 'is_current', 'job_type']


class ProjectTagInline(admin.TabularInline):
    model = ProjectTag
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectTagInline]
    list_display = ['title', 'category', 'date', 'is_featured', 'order']
    list_filter = ['category', 'is_featured']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'start_date', 'end_date']


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['title', 'year']


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']
