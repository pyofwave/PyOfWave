"""
Tests that tags properly create deltas for their deltas.
"""
from .. import tags, datasource

tag = tags.TagDoc(datasource.Document())

blip = tags.Tag(tag, "blip")
tag.append(blip)
blip.id = "lakjsdf"
blip[0] = "Curse your sudden but inevetible betrayal."
blip[1] = tags.Tag(blip, "attachment")

print tag.sendDelta()
