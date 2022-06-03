from django.db import models
from taggit.managers import TaggableManager
from taggit.models import GenericTaggedItemBase, TagBase
from taggit.managers import _TaggableManager

from .managers import _BookmarkTaggableManager

class BookmarkTag(TagBase):
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class TaggedBookmark(GenericTaggedItemBase):
    tag = models.ForeignKey(
        BookmarkTag,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_items",
    )


class Bookmark(models.Model):
    url = models.URLField(blank=False)
    title = models.CharField(blank=False, max_length=255)
    is_private = models.BooleanField(default=False)

    tags = TaggableManager(through=TaggedBookmark)

    def __str__(self):
        return self.title
