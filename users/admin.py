from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class UserAdminConfig(UserAdmin):
    search_fields = ('email','user_name',)
    ordering = ('-start_date',)
    list_filter = ('is_superuser','is_staff')
    list_display = ('email','user_name','is_superuser','is_staff')
    fieldsets = (
        (None, {'fields': ('email','user_name','first_name')}),
        ('Permissions',{'fields': ('is_superuser','is_staff')})
    )
    add_fieldsets = (
        ( None,{
            'classes':('wide',),
            'fields':('email','user_name','first_name','last_name','password1','password2','is_staff')}
        ),
    )

admin.site.register(NewUser,UserAdminConfig)