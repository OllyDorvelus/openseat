from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django_softdelete.models import SoftDeleteModel 


from config.models import GenericRelatedModel

class Review(GenericRelatedModel, SoftDeleteModel):
    class Rating(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    rating = models.IntegerField(choices=Rating.choices)
    body = models.TextField(max_length=1000, blank=True)

    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews_given')

    class Meta:
        unique_together = ('reviewer', 'content_type', 'content_id')
    

class Report(GenericRelatedModel, SoftDeleteModel):
    class Reason(models.TextChoices):
        SPAM = 'SPA', _('Spam')
        HARASSMENT = 'HAR', _('Harassment')
        INAPPROPRIATE = 'INA', _('Inappropriate Content')
        SCAM = 'SCA', _('Scam')
        OTHER = 'OTH', _('Other')

    class Status(models.TextChoices):
        PENDING = 'PEN', _('Pending')
        REVIEWED = 'REV', _('Reviewed')
        RESOLVED = 'RES', _('Resolved')
        DISMISSED = 'DIS', _('Dismissed')

    reason = models.CharField(max_length=3, choices=Reason.choices)
    status = models.TextField(max_length=3, blank=True)
    details = models.TextField(max_length=1000, blank=True)

    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reports_filed')