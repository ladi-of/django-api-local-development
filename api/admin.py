from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserSpec


class UserSpecAdmin(UserAdmin):
    list_display = ('id', 'username')


admin.site.register(UserSpec, UserSpecAdmin)
