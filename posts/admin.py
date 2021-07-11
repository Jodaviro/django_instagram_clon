from django.contrib import admin

# Register your models here.
from posts.models import Post, Comment


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


@admin.register(Comment)
class Comment(admin.ModelAdmin)
    """Comment Admin"""
    list_display =('post', 'text', 'profile')
    list_editable = ('text')
    readonly_fields = ('created', 'modified',)
