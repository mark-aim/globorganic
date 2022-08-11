from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from authentication.models import User

# Register your models here.
class UserAdmin(BaseUserAdmin):
    list_display = ('last_name', 'first_name','username', 'email', 'phone_number', 'join_date', 'last_login', 'is_active', 'is_staff', 'is_admin', 'is_superuser');
    search_fields = ('username', 'first_name', 'last_name', 'email', 'phone_number');
    readonly_fields = ('join_date', 'last_login');
    filter_horizontal = ();
    list_filter = ('last_login',);
    fieldsets = ();
    add_fieldsets=(
        (None, {
            'classes':('wide'),
            'fields':('first_name', 'last_name', 'username', 'email', 'phone_number', 'password1', 'password2'),
        }),
    )

    ordering = ('username',)



admin.site.register(User, UserAdmin);