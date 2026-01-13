from django.contrib import admin

feature_32.1
from users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email',)

# Register your models here.
develop
