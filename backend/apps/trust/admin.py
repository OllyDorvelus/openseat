from django.contrib import admin
from apps.trust.models import Review, Report

# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'content_type', 'content_id', 'rating', 'reviewer',)

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'content_type', 'content_id', 'reason', 'status', 'reporter')

