from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Register your models here.
from users.models import Profile, Contact

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """profile admin"""

    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user')
    list_editable = ('phone_number', 'website')
    search_fields = ('user__email','user__first_name', 'user__last_name', 'phone_number')
    list_filter = ('created', 'modified')

    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),)
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography'),
            )
        }),
        ('Metadata', {
            'fields':('created', 'modified')
        }),
    )
    readonly_fields = ('created', 'modified',)


class ProfileInline(admin.StackedInline):
    """Inline admin for Users in django user panel"""
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """Displays new user django panel"""
    inlines = (ProfileInline,)
    #shows the fields displayed when users are listed
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Contact Admin """
    list_display = ('profile',)
    list_display_links = ('profile',)


