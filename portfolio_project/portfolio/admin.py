from django.contrib import admin
from .models import Project, Experience, Technology, Achievement, ContactInfo
# SocialLink
from django.utils.html import format_html

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'progress')  # project's name +
    fields = ('title', 'description', 'image', 'progress', 'link')  # redacted fields

admin.site.register(Project)

class TechnologyInline(admin.TabularInline):
    model = Technology
    extra = 1  # How much free from to be shown

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

# class SocialLinkInline(admin.TabularInline):
#     model = SocialLink
#     extra = 1
#     fields = ('platform_name', 'icon', 'url')
    # readonly_fields = ('icon_image', 'url_link')

    # def icon_image(self, obj):
    #     if obj.icon:
    #         return format_html('<img src="{}" width="24" height="24" />', obj.icon.url)
    #     return "No Icon"
    # icon_image.short_description = "Icon"

    # def url_link(self, obj):
    #     return format_html('<a href="{}" target="_blank">{}</a>', obj.url, obj.url)
    # url_link.short_description = "Link"

class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'short_description', 'profile_photo_display']
    # inlines = [SocialLinkInline]

    def profile_photo_display(self, obj):
        if obj.profile_photo:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />', obj.profile_photo.url)
        return "No Photo"
    profile_photo_display.short_description = "Profile Photo"

admin.site.register(ContactInfo, ContactInfoAdmin)