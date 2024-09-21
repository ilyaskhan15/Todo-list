from django.contrib import admin
from .models import ListItem  # Import your model

@admin.register(ListItem)
class ListItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')  # Customize as needed


# Register your models here.
