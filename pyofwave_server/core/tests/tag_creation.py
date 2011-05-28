"""
This file ensures that I can easily create and use Tag objects.
"""

from .. import tags, datasource as ds

tag = tags.Tag(ds.Document(), "blip")
# tag1 = tags.Tag(tag, ds.Item(ds.Item.TYPE_START_TAG, "blip"))
