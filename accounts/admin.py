from django.contrib import admin
from accounts.models import User, Profile


@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ('username', 'last_name', 'first_name', )

admin.site.register(Profile)