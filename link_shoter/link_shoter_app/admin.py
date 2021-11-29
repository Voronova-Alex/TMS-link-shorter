from django.contrib import admin
from .models import Link


@admin.register(Link)
class LinkAdmin (admin.ModelAdmin):
    list_display = ['input_link', 'output_link', 'date_create_link', 'date_last_click', 'clicks']