from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    fields=['subject','text','author','body']
    list_display=['subject','author']

admin.site.register(Post,PostAdmin)