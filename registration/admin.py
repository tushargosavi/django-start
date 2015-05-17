from django.contrib import admin

# Register your models here.
from registration.models import UserProfile

admin.site.register(UserProfile)