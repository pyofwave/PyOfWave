"""
Testing script to ensure that deltas properly processes documents.
"""

from .. import delta, datasource

# retain  ('<a>spam</a>' in '<a>spam</a> & </a>eggs</a>')
#--------------------------------------------------------
document = datasource.Document()
deltaTest = delta.Delta(delta.Operation())

res = delta.applyToDoc(document)
#ensure res meets expectations

# updateAttributes (foo='bar' to foo=42)
#--------------------------------------------------------
document = datasource.Document()
deltaTest = delta.Delta(delta.Operation())

res = delta.applyToDoc(document)
#ensure res meets expectations

# replaceAttributes (foo='bar' to foo=42)
#--------------------------------------------------------
document = datasource.Document()
deltaTest = delta.Delta(delta.Operation())

res = delta.applyToDoc(document)
#ensure res meets expectations


# elementStart, charactors, and elementEnd ('' to '<spam>eggs</spam>')
#--------------------------------------------------------
document = datasource.Document()
deltaTest = delta.Delta(delta.Operation())

res = delta.applyToDoc(document)
#ensure res meets expectations

# deleteCharactors  ('Spam & Eggs' to 'Spam')
#--------------------------------------------------------
document = datasource.Document()
deltaTest = delta.Delta(delta.Operation())

res = delta.applyToDoc(document)
#ensure res meets expectations

# deleteElementStart, deleteCharactors, and deleteElementEnd
# ('<a>spam</a>' in '<a>spam</a> & </a>eggs</a>')
#--------------------------------------------------------
document = datasource.Document()
deltaTest = delta.Delta(delta.Operation())

res = delta.applyToDoc(document)
#ensure res meets expectations

# annotationsBoundary (spam='eggs' to life=42)
#--------------------------------------------------------
document = datasource.Document()
deltaTest = delta.Delta(delta.Operation())

res = delta.applyToDoc(document)
#ensure res meets expectations

