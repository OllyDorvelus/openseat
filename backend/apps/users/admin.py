from django.contrib import admin
from apps.users.models import Profile, Interest, Group, GroupMembership
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'bio',)

@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(GroupMembership)
class GroupMembershipAdmin(admin.ModelAdmin):
    pass