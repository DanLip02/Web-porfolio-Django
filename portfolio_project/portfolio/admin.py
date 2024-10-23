from django.contrib import admin
from .models import Project, Experience, Technology, Achievement

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'progress')  # Отображение названия проекта и процента выполнения в списке проектов
    fields = ('title', 'description', 'image', 'progress', 'link')  # Поля для редактирования

admin.site.register(Project)

class TechnologyInline(admin.TabularInline):
    model = Technology
    extra = 1  # Сколько пустых форм показывать

admin.site.register(Technology)

class AchievementInline(admin.TabularInline):
    model = Achievement
    extra = 1

admin.site.register(Achievement)

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('institution', 'role', 'type', 'start_date', 'end_date')
    list_filter = ('type', 'start_date')
    search_fields = ('institution', 'role', 'technologies')
    inlines = [TechnologyInline, AchievementInline]

admin.site.register(Experience, ExperienceAdmin)