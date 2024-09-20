from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class Admin(admin.ModelAdmin):
    pass
