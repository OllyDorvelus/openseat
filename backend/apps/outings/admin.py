from django.contrib import admin
from apps.outings.models import Outing, Category, RSVP, City
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Outing)
class OutingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'city', 'creator', 'starts_at', 'location_name', 'status',)

@admin.register(RSVP)
class RSVPAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'status', 'created_at',)