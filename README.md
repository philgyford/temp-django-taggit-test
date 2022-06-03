Testing a possible bug in django-taggit with Django 4.1a1

Either `pipenv install` or `pip -r requirements.txt`.

Then either `manage.py test` or, in `manage.py shell`, do this:

```python
from myproject.myapp.models import Item
extra_filters = {"item__is_private": False}
Item.tags.most_common(extra_filters=extra_filters)
```

Using Django 4.1a1, this generates an error like the one below. But if we use Django 4.0, there is no error.


```
Traceback (most recent call last):
  File "/Users/phil/.local/share/virtualenvs/temp-django-taggit-test-bvQO61Tk/lib/python3.10/site-packages/taggit/managers.py", line 77, in get_queryset
    return self.instance._prefetched_objects_cache[self.prefetch_cache_name]
AttributeError: 'NoneType' object has no attribute '_prefetched_objects_cache'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/Users/phil/.local/share/virtualenvs/temp-django-taggit-test-bvQO61Tk/lib/python3.10/site-packages/taggit/managers.py", line 357, in most_common
    self.get_queryset(extra_filters)
  File "/Users/phil/.local/share/virtualenvs/temp-django-taggit-test-bvQO61Tk/lib/python3.10/site-packages/taggit/managers.py", line 80, in get_queryset
    return self.through.tags_for(self.model, self.instance, **kwargs).order_by(
  File "/Users/phil/.local/share/virtualenvs/temp-django-taggit-test-bvQO61Tk/lib/python3.10/site-packages/taggit/models.py", line 161, in tags_for
    return cls.tag_model().objects.filter(**kwargs).distinct()
  File "/Users/phil/.local/share/virtualenvs/temp-django-taggit-test-bvQO61Tk/lib/python3.10/site-packages/django/db/models/manager.py", line 85, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/Users/phil/.local/share/virtualenvs/temp-django-taggit-test-bvQO61Tk/lib/python3.10/site-packages/django/db/models/query.py", line 1395, in filter
    return self._filter_or_exclude(False, args, kwargs)
  File "/Users/phil/.local/share/virtualenvs/temp-django-taggit-test-bvQO61Tk/lib/python3.10/site-packages/django/db/models/query.py", line 1413, in _filter_or_exclude
    clone._filter_or_exclude_inplace(negate, args, kwargs)
  File "/Users/phil/.local/share/virtualenvs/temp-django-taggit-test-bvQO61Tk/lib/python3.10/site-packages/django/db/models/query.py", line 1420, in _filter_or_exclude_inplace
    self._query.add_q(Q(*args, **kwargs))
  File "/Users/phil/.local/share/virtualenvs/temp-django-taggit-test-bvQO61Tk/lib/python3.10/site-packages/django/db/models/sql/query.py", line 1532, in add_q
    clause, _ = self._add_q(q_object, self.used_aliases)
  File "/Users/phil/.local/share/virtualenvs/temp-django-taggit-test-bvQO61Tk/lib/python3.10/site-packages/django/db/models/sql/query.py", line 1562, in _add_q
    child_clause, needed_inner = self.build_filter(
  File "/Users/phil/.local/share/virtualenvs/temp-django-taggit-test-bvQO61Tk/lib/python3.10/site-packages/django/db/models/sql/query.py", line 1470, in build_filter
    col = self._get_col(targets[0], join_info.final_field, alias)
  File "/Users/phil/.local/share/virtualenvs/temp-django-taggit-test-bvQO61Tk/lib/python3.10/site-packages/django/db/models/sql/query.py", line 387, in _get_col
    return target.get_col(alias, field)
AttributeError: 'ManyToManyRel' object has no attribute 'get_col'
```