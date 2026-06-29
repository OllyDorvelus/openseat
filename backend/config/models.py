import uuid
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class BaseModel(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

class GenericRelatedModel(BaseModel):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_id = models.UUIDField()
    content_object = GenericForeignKey('content_type', 'content_id')

    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=['content_type', 'content_id'])
        ]