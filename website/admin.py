from django.contrib import admin
from .models import Profile, Password_recovery

# Register your models here.
admin.site.register(Profile)
admin.site.register(Password_recovery)