from django.contrib import admin

from jobs.models import PostJob

# Register your models here.


@admin.register(PostJob)
class PostAdmin(admin.ModelAdmin):
    pass
