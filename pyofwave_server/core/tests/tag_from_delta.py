"""
Ensure that tags can be created from deltas.
"""
from .. import delta, tags

def printTagList(tagList):
    print [str(item) for item in tagList]

print "\nThis test prints Tag objects for deltas which are printed in Federation format."

print "\nTags for 'updateAttributes spam:eggs spam:42;':"
deltaTest = delta.Delta(delta.Operation('updateAttributes',
                                        {'spam' : 'eggs',}, {'spam' : 42}))
printTagList(tags.TagDelta(deltaTest))

print "\nTags for 'replaceAttributes spam:(eggs,42);':"
deltaTest = delta.Delta(
    delta.Operation('replaceAttributes', {'spam' : ('eggs', 42),}))
printTagList(tags.TagDelta(deltaTest))

print "\nTags for 'elementStart spam foo:bar;charactors eggs;elementEnd;':"
deltaTest = delta.Delta(
    delta.Operation('elementStart', 'spam', {'foo':'bar',}),
    delta.Operation('charactors', 'eggs'),
    delta.Operation('elementEnd')
    )
printTagList(tags.TagDelta(deltaTest))

print "\nTags for 'retain 6;deleteCharactors 4;deleteElementStart a;deleteElementEnd;retain 1;':"
deltaTest = delta.Delta(delta.Operation('retain', 6),
                        delta.Operation('deleteCharactors', 4),
                        delta.Operation('deleteElementStart', 'a', {}),
                        delta.Operation('deleteCharactors', 4),
                        delta.Operation('deleteElementEnd'),
                        delta.Operation('retain', 1))
printTagList(tags.TagDelta(deltaTest))

print "\nTags for 'annotationsBoundary spam life:((),42);':"
deltaTest = delta.Delta(delta.Operation('annotationsBoundary',
                                        ('spam',), {'life':('', 42),}))
printTagList(tags.TagDelta(deltaTest))
