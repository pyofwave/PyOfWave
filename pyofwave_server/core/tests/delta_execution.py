"""
Testing script to ensure that deltas properly processes documents.
"""

from .. import delta, datasource as ds

print "retain  ('<a>spam</a>' in '<a>spam</a> & </a>eggs</a>')"
#--------------------------------------------------------
document = ds.Document(
    ds.Item(ds.Item.TYPE_START_TAG, 'a'),
    ds.Item(ds.Item.TYPE_TEXT, 's'),  # The standard stores each charactor seperately.
    ds.Item(ds.Item.TYPE_TEXT, 'p'),
    ds.Item(ds.Item.TYPE_TEXT, 'a'),
    ds.Item(ds.Item.TYPE_TEXT, 'm'),
    ds.Item(ds.Item.TYPE_END_TAG, 'a'),

    ds.Item(ds.Item.TYPE_TEXT, ' '),
    ds.Item(ds.Item.TYPE_TEXT, '&'),
    ds.Item(ds.Item.TYPE_TEXT, ' '),

    ds.Item(ds.Item.TYPE_START_TAG, 'a'),
    ds.Item(ds.Item.TYPE_TEXT, 'e'),
    ds.Item(ds.Item.TYPE_TEXT, 'g'),
    ds.Item(ds.Item.TYPE_TEXT, 'g'),
    ds.Item(ds.Item.TYPE_TEXT, 's'),
    ds.Item(ds.Item.TYPE_END_TAG, 'a'))
deltaTest = delta.Delta(delta.Operation('retain', 6))

res = deltaTest.applyToDoc(document)
print res

print "updateAttributes (spam='eggs' to spam=42)"
#--------------------------------------------------------
document = ds.Document(
    ds.Item(ds.Item.TYPE_TEXT, 'w', spam = 'eggs'))
deltaTest = delta.Delta(delta.Operation('updateAttributes',
                                        {'spam' : 'eggs',}, {'spam' : 42}))

res = deltaTest.applyToDoc(document)
print res

print "replaceAttributes (foo='bar' to foo=42)"
#--------------------------------------------------------
document = ds.Document(
    ds.Item(ds.Item.TYPE_TEXT, 'w', spam='eggs'))
deltaTest = delta.Delta(
    delta.Operation('replaceAttributes', {'spam' : ('eggs', 42),}))

res = deltaTest.applyToDoc(document)
print res


print "elementStart, charactors, and elementEnd " + \
"('' to '<spam foo='bar'>eggs</spam>')"
#--------------------------------------------------------
document = ds.Document()
deltaTest = delta.Delta(
    delta.Operation('elementStart', 'spam', {'foo':'bar',}),
    delta.Operation('charactors', 'eggs'),
    delta.Operation('elementEnd')
    )

res = deltaTest.applyToDoc(document)
print res

print "deleteCharactors  ('Spam & Eggs!' to 'Spam!')"
#--------------------------------------------------------
document = ds.Document(
    ds.Item(ds.Item.TYPE_TEXT, 'S'),
    ds.Item(ds.Item.TYPE_TEXT, 'p'),
    ds.Item(ds.Item.TYPE_TEXT, 'a'),
    ds.Item(ds.Item.TYPE_TEXT, 'm'),

    ds.Item(ds.Item.TYPE_TEXT, ' '),
    ds.Item(ds.Item.TYPE_TEXT, '&'),
    ds.Item(ds.Item.TYPE_TEXT, ' '),

    ds.Item(ds.Item.TYPE_TEXT, 'E'),
    ds.Item(ds.Item.TYPE_TEXT, 'g'),
    ds.Item(ds.Item.TYPE_TEXT, 'g'),
    ds.Item(ds.Item.TYPE_TEXT, 's'),
    ds.Item(ds.Item.TYPE_TEXT, '!')
    )
deltaTest = delta.Delta(delta.Operation('retain', 4),
                        delta.Operation('deleteCharactors', 8),
                        delta.Operation('retain', 1))

res = deltaTest.applyToDoc(document)
print res

print "deleteElementStart, deleteCharactors, and deleteElementEnd"
print "('<a>spam</a>!' in '<a>spam</a> & </a>eggs</a>!')"
#--------------------------------------------------------
document = ds.Document(
    ds.Item(ds.Item.TYPE_START_TAG, 'a'),
    ds.Item(ds.Item.TYPE_TEXT, 's'),  
    ds.Item(ds.Item.TYPE_TEXT, 'p'),
    ds.Item(ds.Item.TYPE_TEXT, 'a'),
    ds.Item(ds.Item.TYPE_TEXT, 'm'),
    ds.Item(ds.Item.TYPE_END_TAG, 'a'),

    ds.Item(ds.Item.TYPE_TEXT, ' '),
    ds.Item(ds.Item.TYPE_TEXT, '&'),
    ds.Item(ds.Item.TYPE_TEXT, ' '),

    ds.Item(ds.Item.TYPE_START_TAG, 'a'),
    ds.Item(ds.Item.TYPE_TEXT, 'e'),
    ds.Item(ds.Item.TYPE_TEXT, 'g'),
    ds.Item(ds.Item.TYPE_TEXT, 'g'),
    ds.Item(ds.Item.TYPE_TEXT, 's'),
    ds.Item(ds.Item.TYPE_END_TAG, 'a'),
    ds.Item(ds.Item.TYPE_TEXT, '!')
    )
deltaTest = delta.Delta(delta.Operation('retain', 6),
                        delta.Operation('deleteCharactors', 4),
                        delta.Operation('deleteElementStart', 'a', {}),
                        delta.Operation('deleteCharactors', 4),
                        delta.Operation('deleteElementEnd'),
                        delta.Operation('retain', 1))

res = deltaTest.applyToDoc(document)
print res

print "annotationsBoundary (spam='eggs' to life=42)"
#--------------------------------------------------------
document = ds.Document(ds.Item(ds.Item.TYPE_TEXT, 'w', spam='eggs'))
deltaTest = delta.Delta(delta.Operation('annotationsBoundary',
                                        ('spam',), {'life':('', 42),}))

res = deltaTest.applyToDoc(document)
print res

