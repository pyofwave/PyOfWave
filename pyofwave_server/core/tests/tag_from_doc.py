"""
Test script ensuring that core.datasource.Document objects may be viewed as
core.tags.Tag objects.
"""

from .. import tags, datasource as ds

print "\n\nThis test ensures that tag objects can be created from documents."
document = ds.Document(
    ds.Item(ds.Item.TYPE_START_TAG, 'conversation'),
    ds.Item(ds.Item.TYPE_START_TAG, 'blip'),
    ds.Item(ds.Item.TYPE_TEXT, 'w'),
    ds.Item(ds.Item.TYPE_TEXT, 'a'),
    ds.Item(ds.Item.TYPE_TEXT, 'v'),
    ds.Item(ds.Item.TYPE_TEXT, 'e'),
    ds.Item(ds.Item.TYPE_END_TAG, ''),
    ds.Item(ds.Item.TYPE_START_TAG, 'blip'),
    ds.Item(ds.Item.TYPE_END_TAG, ''),
    ds.Item(ds.Item.TYPE_END_TAG, ''),
    )
tag, i = tags.TagItem(document, 0)
tagList = tags.TagDoc(document)

print "TagItem:\n", tag

print "TagDoc:"
for tag in tagList:
    print tag
