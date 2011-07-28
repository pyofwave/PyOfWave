"""
Tests that tags properly create deltas for their deltas.
"""
from .. import tags, datasource

print \
"""

This script prints the resulting delta from the script:
tag = tags.TagDoc(datasource.Document())

blip = tags.Tag(tag, "blip")
tag.append(blip)
blip.id = "lakjsdf"
blip[0] = "Curse your sudden but inevetible betrayal."
blip[1] = tags.Tag(blip, "attachment")
"""
tag = tags.TagDoc(datasource.Document(""))

blip = tags.Tag(tag, "blip")
tag.append(blip)
blip.id = "lakjsdf"
blip[0] = "Curse your sudden but inevetible betrayal."
blip[1] = tags.Tag(blip, "attachment")

# print tag.sendDelta()
delta = tag.sendDelta()

for op in delta.ops:
    print op.operation, ' '.join(map(str, op.args)), ';'

print "\nJust to ensure I can delete too (delete what I just created as a document)."
doc = datasource.Document("",
    datasource.Item(datasource.Item.TYPE_START_TAG, "blip"),
    datasource.Item(datasource.Item.TYPE_TEXT, "Curse Your sudden but inevitable betrayal."),
    datasource.Item(datasource.Item.TYPE_START_TAG, "attachment"),
    datasource.Item(datasource.Item.TYPE_END_TAG, ''),
    datasource.Item(datasource.Item.TYPE_END_TAG, '')
    )
tag = tags.TagDoc(doc)

tag[0]._delete()

# print tag.sendDelta()
delta = tag.sendDelta()

for op in delta.ops:
    print op.operation, ' '.join(map(str, op.args)), ';'

