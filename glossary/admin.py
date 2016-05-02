from django.contrib import admin

from .models import Acronym

class AcronymAdmin(admin.ModelAdmin):
    list_display = ['abbreviation', 'word']

admin.site.register(Acronym, AcronymAdmin)
