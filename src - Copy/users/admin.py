from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password','username','first_name','last_name','date_joined')}),
        ('Permissions', {'fields': (
            'is_active', 
            'is_staff', 
            'is_superuser',
            'groups', 
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    list_display = ('email', 'username','first_name','last_name', 'is_staff', 'last_login')
    search_fields = ( 'email','username', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


# Register your models here.
## Just add this is the respective admin file of the app you create so we can use it 
admin.site.register(User, UserAdmin)