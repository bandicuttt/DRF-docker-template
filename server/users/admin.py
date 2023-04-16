from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models.users import User
from django.utils.translation import gettext_lazy as _
from django.db.models import Count


@admin.register(User)
class UserAdmin(UserAdmin):
    change_user_password_template = None
    fieldsets = (
        (None, {'fields': ('email',)}),
        (_('Личная информация'),
         {'fields': ('first_name', 'last_name',)}),
        (_('Permissions'), {
            'fields': ('is_verification', 'is_staff',  'is_superuser', 'groups', 'user_permissions',),
        }),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1','username'),
        }),
    )
    list_display = ('uuid', 'email','first_name','last_name','username','email','date_joined','is_verification','pay_id','is_active')

    list_display_links = ('uuid',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups',)
    search_fields = ('first_name', 'last_name', 'uuid', 'email',)
    ordering = ('-uuid',)
    filter_horizontal = ('groups', 'user_permissions',)
    readonly_fields = ('last_login',)