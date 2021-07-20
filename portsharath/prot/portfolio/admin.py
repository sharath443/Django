from django.contrib import admin
from .models import user_Table
@admin.register(user_Table)
class user_info(admin.ModelAdmin):
    list_display = ('name','email','txt')

