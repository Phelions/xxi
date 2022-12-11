from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import PermissionsMixin
from accounts.models import Usuario
# Register your models here.

admin.site.register(Usuario)