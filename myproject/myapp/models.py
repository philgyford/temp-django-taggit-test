from django.db import models
from taggit.managers import TaggableManager
from taggit.models import GenericTaggedItemBase, TagBase
from taggit.managers import _TaggableManager


class ItemTag(TagBase):
    pass


class TaggedItem(GenericTaggedItemBase):
    tag = models.ForeignKey(
        ItemTag, on_delete=models.CASCADE, related_name="tagged_items",
    )


class Item(models.Model):
    is_private = models.BooleanField(default=False)

    tags = TaggableManager(through=TaggedItem)
