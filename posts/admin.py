from django.contrib import admin

# Register your models here.
from posts.models import Post

@admin.register(Post)
class Post(admin.ModelAdmin):
    """Post admin"""
    list_display = ('user','photo')
    list_display_links = ('user',)
    list_editable = ('photo',)
    list_filter = (
        'created',
        'modified',
    )
    search_fields = ('user',)
