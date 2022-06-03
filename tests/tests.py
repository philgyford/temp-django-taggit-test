from django.test import TestCase

from myproject.myapp.models import Item


class ItemTestCase(TestCase):

    def test_most_common(self):
        item = Item.objects.create(is_private=True)
        item.tags.add("red")

        tags = Item.tags.most_common()
        self.assertEqual(len(tags), 1)

    def test_most_common_extra_filters(self):
        item = Item.objects.create(is_private=True)
        item.tags.add("red")

        tags = Item.tags.most_common(
            extra_filters={"item__is_private": True}
        )
        self.assertEqual(len(tags), 1)
