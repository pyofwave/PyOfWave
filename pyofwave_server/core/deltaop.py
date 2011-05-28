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
        if not (item.annotations.get(key, '') == attributesUpdate[key][0]):
            raise DeltaNotMatch
        item.annotations[key] = attributesUpdate[key][1]
    new.items.append(item)
    old.cursor += 1

def charactors(old, new, charactors):    
    for char in charactors:
        new.items.append(Item(Item.TYPE_TEXT, char))

def elementStart(old, new, typeI, attrs):
    new.items.append(Item(Item.TYPE_START_TAG, typeI, **attrs))

def elementEnd(old, new):
    new.items.append(Item(Item.TYPE_END_TAG, ''))

def deleteCharactors(old, new, charactors):
    old.cursor += charactors

def deleteElementStart(old, new, typeI, attrs):
    item = old.items[old.cursor]
    print item.name, item.annotations
    if not (item.type == Item.TYPE_START_TAG and
        item.name == typeI and item.annotations == attrs):
        raise DeltaNotMatch
    old.cursor += 1

def deleteElementEnd(old, new):
    if not (old.items[old.cursor].type == Item.TYPE_END_TAG):
        raise DeltaNotMatch
    old.cursor += 1

def annotationsBoundary(old, new, ends, changes):
    item = copy(old.items[old.cursor])

    for end in ends: del item.annotations[end]
    
    for key in changes.keys():
        if not (old.annotations.get(key, '') == changes[key][0]):
            raise DeltaNotMatch
        item.annotations[key] = changes[key][1]
    new.items.append(item)
    old.cursor += 1
