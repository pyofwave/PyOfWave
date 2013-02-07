"""
Implements in memory XMLu storage.
"""
from xml.etree import ElementTree as et
from xml.dom import minidom # minidom has parent links, and works with py-dom-xpath for full XPath.
import xpath
from copy import deepcopy

VERSION_TAG = "{http://pyofwave.info/2013/xmlu}version"

class XMLStorage(object):
	def __init__(self, **users):
		self.data = users

	def addUser(self, user, xml):
		self.data[user] = xml

	def searchDocuments(self, user, url="", namespaces={}, xpath_="", range_=slice(0, -1), depth=-1, version="", restore=False):
		""" Returns selected documents.

		>>> store = XMLStorage(spock=minidom.parseString("<restaurant><meal><eggs /><spam /></meal><meal><eggs /><spam /><spam /></meal><foo bar='42'>6*7</foo></restaurant>"))
		>>> et.tostring(store.searchDocuments("spock")[0])
		'<restaurant><meal><eggs /><spam /></meal><meal><eggs /><spam /><spam /></meal><foo bar="42">6*7</foo></restaurant>'
		>>> list(et.tostring(el) for el in store.searchDocuments("spock", xpath_="//spam"))
		['<spam />', '<spam />']
		"""
		xml = self.data[user]
		xctxt = xpath.XPathContext()
		if url:
			xml = xctxt.find("//*[xmlu:src='{}']".format(url), xml)[0]
		results = xctxt.find(xpath_, xml, **namespaces)[range_] if xpath_ else (xml,)

		return tuple(et.XML(el.toxml()) for el in results) # Generator causes issues

	def trimXML(self, xml, todepth, curdepth=0):
		pass
	
	def applyDelta(self, user, xml, delta):
		pass

if __name__ == '__main__':
	from doctest import testmod
	testmod()
