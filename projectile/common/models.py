import uuid
from django.utils import timezone
from django.db import models
from django.db.models import Q
from django.utils.text import slugify
from .enums import Status


class CreatedAtUpdatedAtBaseModel(models.Model):
    alias = models.UUIDField(
        default=uuid.uuid4, editable=False, db_index=True, unique=True)
    status = models.IntegerField(
        choices=[(choice.value, choice.name.replace("_", " ")) for choice in Status], default=Status.ACTIVE.value)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    entry_by = models.ForeignKey(
        'core.Person',
        models.DO_NOTHING,
        default=None,
        null=True,
        verbose_name=('entry by'),
        related_name="%(app_label)s_%(class)s_entry_by"
    )

    updated_by = models.ForeignKey(
        'core.Person',
        models.DO_NOTHING,
        default=None,
        null=True,
        verbose_name=('last updated by'),
        related_name="%(app_label)s_%(class)s_updated_by"
    )

    class Meta:
        abstract = True
        ordering = ('-created_at',)


class NameSlugDescriptionBaseModel(CreatedAtUpdatedAtBaseModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True, editable=False)
    description = models.TextField(blank=True)

    class Meta:
        abstract = True
        ordering = ('name',)

    def __unicode__(self):
        return self.get_name()

    def get_name(self):
        return u"ID: {}, Name: {}".format(self.id, self.name)

    def save(self, *args, **kwargs):
        # just check if name is exist
        if self.name:
            self.slug = slugify(self.name)
            super(NameSlugDescriptionBaseModel, self).save(*args, **kwargs)
