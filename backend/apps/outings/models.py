from django.db import models
from django.conf import settings
from config.models import BaseModel, TimeStampedModel
from django.utils.translation import gettext_lazy as _
from apps.users.models import Group, Interest


class Category(BaseModel):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True)

    def __str__(self) -> str:
        return self.name
class City(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
# core model of the app, describes an event a user/group can create. Other users can join event
class Outing(BaseModel):
    class Status(models.TextChoices):
        ACTIVE = 'ACT', _('Active')
        CANCELLED = 'CAN', _('Cancelled')
        COMPLETED = 'COM', _('Completed')
    
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    location_name = models.CharField(max_length=200)
    location_address = models.CharField(max_length=500, blank=True)
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField(blank=True)
    max_attendees = models.PositiveIntegerField()
    chat_link = models.URLField(blank=True)
    status = models.CharField(max_length=3, choices=Status.choices, default=Status.ACTIVE)
    creator_attending = models.BooleanField(default=True)
    requires_approval = models.BooleanField(default=False)
    
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    interests = models.ManyToManyField(Interest, blank=True)

    def __str__(self):
        return self.title

class RSVP(TimeStampedModel):
    class Status(models.TextChoices):
        CONFIRMED = 'CON', _('Confirmed')
        PENDING = 'PEN', _('Pending')
        CANCELLED = 'CAN', _('Cancelled')
    class Type(models.TextChoices):
        GROUP_MEMBER = 'GM', _('Group Member'),
        GUEST = 'GU', _("Guest")

    seat = models.ForeignKey(Outing, on_delete=models.CASCADE, related_name='seat')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=Type.choices, default=Type.GUEST)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.CONFIRMED)
    class Meta:
        unique_together = ('seat', 'user')