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


# elementStart, charactors, and elementEnd ('' to '<spam>eggs</spam>')
#--------------------------------------------------------
##document = ds.Document()
##deltaTest = delta.Delta(delta.Operation())
##
##res = deltaTest.applyToDoc(document)
##print res

# deleteCharactors  ('Spam & Eggs' to 'Spam')
#--------------------------------------------------------
##document = ds.Document()
##deltaTest = delta.Delta(delta.Operation())
##
##res = deltaTest.applyToDoc(document)
##print res

# deleteElementStart, deleteCharactors, and deleteElementEnd
# ('<a>spam</a>' in '<a>spam</a> & </a>eggs</a>')
#--------------------------------------------------------
##document = ds.Document()
##deltaTest = delta.Delta(delta.Operation())
##
##res = deltaTest.applyToDoc(document)
##print res

# annotationsBoundary (spam='eggs' to life=42)
#--------------------------------------------------------
##document = ds.Document()
##deltaTest = delta.Delta(delta.Operation())
##
##res = deltaTest.applyToDoc(document)
##print res

