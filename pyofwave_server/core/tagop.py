"""
Alternate delta routines for easier visualising.
"""

def retain(old, new, itemCount):
    pass #No change

def updateAttributes(old, new, oldAttributes, newAttributes):
    new.addTag(2, "", **newAttributes)

def replaceAttributes(old, new, attributesUpdate):
    attrs = {}
    for key in attributesUpdate.keys(): attrs[key] = attributesUpdate[key][1]

    new.addTag(2, "", **attrs)

def charactors(old, new, charactors):
    new.addTag(2, charactors)

def elementStart(old, new, typeI, attrs):
    new.addTag(0, typeI, **attrs)

def elementEnd(old, new):
    new.addTag(1, "")

def deleteCharactors(old, new, charactors):
    new.addTag(2, '!!-'+str(charactors))

def deleteElementStart(old, new, typeI, attrs):
    new.addTag(0, '!!-' + typeI, **attrs)

def deleteElementEnd(old, new):
    new.addTag(1, '')

def annotationsBoundary(old, new, ends, changes):
    #calculate new tags with null for delete
    new.addTag(2, '', **changes)
