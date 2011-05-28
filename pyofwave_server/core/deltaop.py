"""
Contains implementations of all operations found in deltas.
"""
from copy import copy
from datasource import Item

class DeltaNotMatch(Exception):
    pass


def retain(old, new, itemCount):
    for i in range(old.cursor, old.cursor + itemCount):
        new.items.append(old.items[i])
    old.cursor = i

def updateAttributes(old, new, oldAttributes, newAttributes):
    if not (old.items[old.cursor].annotations == oldAttributes):
        raise DeltaNotMatch
    
    item = copy(old.items[old.cursor])
    for key in newAttributes.keys():
        item.annotations[key] = newAttributes[key]
    new.items.append(item)
    old.cursor += 1

def replaceAttributes(old, new, attributesUpdate):
    item = copy(old.items[old.cursor])
                
    for key in attributesUpdate.keys():
        if not (old.annotations.get(key, '') == attributesUpdate[key][0]):
            raise DeltaNotMatch
        item.annotations[key] = attributeUpdate[key][1]
    new.items.append(item)
    old.cursor += 1

def charactors(old, new, charactors):    
    for char in charactors:
        new.items.append(Item(Item.TYPE_TEXT, char))

def elementStart(old, new, typeI, attrs):
    new.items.append(Item(Item.TYPE_TAG_START, typeI, **attrs))

def elementEnd(old, new):
    new.items.append(Item(Item.TYPE_TAG_END, ''))

def deleteCharactors(old, new, charactors):
    old.cursor += charactors

def deleteElementStart(old, new, typeI, attrs):
    old.cursor += 1
    item = old.items[old.cursor]
    if not (item.type == Item.TYPE_TAG_START and
        item.name == typeI and item.annotations == attrs):
        raise DeltaNotMatch

def deleteElementEnd(old, new):
    old.cursor += 1
    if not (old.items[old.cursor].type == Item.TYPE_TAG_END):
        raise DeltaNotMatch

def annotationsBoundary(old, new, ends, changes):
    old.cursor += 1
    item = copy(old.items[old.cursor])

    for end in ends: del item.annotations[end]
    
    for key in changes.keys():
        if not (old.annotations.get(key, '') == changes[key][0]):
            raise DeltaNotMatch
        item.annotations[key] = changes[key][1]
    new.items.append(item)
