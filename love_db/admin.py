from django.contrib import admin

from .models import Reason

class ReasonAdmin(admin.ModelAdmin):
    list_display = ('reason_text', 'created_date', 'been_used')
    list_filter = ('been_used', 'created_date')

admin.site.register(Reason, ReasonAdmin)
