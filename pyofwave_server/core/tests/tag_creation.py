"""
This file ensures that I can easily create and use Tag objects.
"""

from .. import tags, datasource as ds

print "\nThis script creates and minipulates core.tags.Tag objects. It outputs" + \
      " various values which should be 'eggs', 'blip', 0, and a core.tags.Text object."

tag = tags.Tag(ds.Document(), "blip")
tag1 = tags.Tag(tag, ds.Item(ds.Item.TYPE_START_TAG, "blip", spam="eggs"))

tag1.spam = 42
print tag1.spam
print tag1._name

print len(tag)

tag[0] = tag1
tag[1] = "Hello world!"
del tag[0]

print tag[0]

tag["link/manual"] = True
