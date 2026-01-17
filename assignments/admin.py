from django.contrib import admin
from .models import About, SocialLink


class AboutAdmin(admin.ModelAdmin):
    list_display = ["about_heading", "updated_at", "created_at"]

    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count == 0:
            return True
        return False


class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ["platform", "updated_at", "created_at"]
    search_fields = ("platform",)


# Register your models here.
admin.site.register(About, AboutAdmin)
admin.site.register(SocialLink, SocialLinkAdmin)
