from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at', 'completed')
    search_fields = ('title', 'description', 'created_at', 'updated_at')
    ordering = ('completed',)

# Register your models here.

admin.site.register(Todo, TodoAdmin)