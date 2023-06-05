from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created', 'user')
    list_filter = ('user', 'created')
    search_fields = ('title', 'user__username')
    ordering = ('-created',)
    date_hierarchy = 'created'
    readonly_fields = ('created',)