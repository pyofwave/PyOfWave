"""
Implements in memory XMLu storage.
"""
from xml.etree import ElementTree as et
from copy import deepcopy

VERSION_TAG = "{http://pyofwave.info/2013/xmlu}version"

class XMLStorage(object):
	def __init__(self):
		self.data = {}
		self.addVersion("", "", et.Element("root"))

	def addVersion(self, user, url, xml):
		if user in self.data: data = self.data[user]
		else: data = self.data[user] = {}
		if url in data: data = data[url]
		else: data = self.data[url] = {"version":0}

		data[""] = data[data["version"]] = xml
		data["version"] += 1

	def searchDocuments(self, user, url="", namespaces={}, xpath="", range_=slice(0,-1), depth=-1, version="", restore=False):
		"""
		Retrieves specified documents (selected by url, xpath, and namespaces), sliced by *range_*.

		Prepare context:

		>>> store = XMLStorage()
		>>> xml = et.XML("<menu><foo><bar /></foo><eggs><spam /><ham /></eggs></menu>"
		>>> store.addVersion("spock", "", xml))
		>>> store.searchDocuments("spock")[0] == xml and store.searchDocuments("spock")[0] is not xml
		True

		Search by identifier:

		>>> store.addVersion("spock", "http://restaurant.example.com/mains", xml[1])
		>>> store.searchDocuments("spock", "http://restaurant.example.com/mains") == xml[1]
		True
		>>> store.searchDocuments("spock", "http://restaurant.example.com/mains") is xml[1]
		False

		Search by XPath (and limit selection by range and depth):

		>>> store.searchDocuments("spock", xpath="eggs/spam")[0] == xml.find("eggs/spam")
		>>> store.searchDocuments("spock", xpath="eggs/*", range_=slice(0,1))[0] == xml[1][0]
		>>> et.tostring(store.searchDocuments("spock", depth=1))
		'<menu><foo /><eggs /></menu>'
		"""
		xml = deepcopy(doc[user][url][version])
		if restore:
			doc[user][url][""] = deepcopy(xml)
			doc[user][url]["version"] = version

		result = xml.findall(xpath, namespaces)[range_] if xpath else [xml]
		return [self.trimXML([el], depth).next() for el in result]

	def trimXML(self, xml, todepth, curdepth=0):
		curdepth+=1
		for child in xml:
			cloned = et.Element(child.tag, child.attrib, tail=child.tail)
			yield cloned
			if child.tag != todepth and curdepth != todepth:
				cloned.text = child.text
				cloned.extend(list(self.trimXML(child, todepth, curdepth)))
	
	def applyDelta(self, user, xml, delta):
		deltaTag = delta.tag.split('}')[1]
##		permission = self.getPermission(user, xml, deltaTag)

		version = int(xml.get(VERSION_TAG)) or None
		if deltaTag == "append":
			if delta.attrib: xml.attrib.update(delta.attrib)
			if len(delta): xml.attrib.extend(list(delta))
			if version is not None: version += 1
		elif deltaTag == "update":
			if list(delta):
				xml.clear()
				xml.extend(list(delta))
			if delta.attrib: xml.attrib = delta.attrib
			if version is not None: version += 1
		elif deltaTag == "select":
			if xml.get(VERSION_TAG, "0") != delta.get(VERSION_TAG):
				raise ValueError # To maintain consistancy, selection is tied to versions.
##			self.select(xml, slice(*[int(i) for i in delta.get("{http://pyofwave.info/2013/xmlu}range".split("-")]), permission)
		elif deltaTag == "delete":
			xml.getParent().remove(xml)

		if version is not None: xml.set(VERSION_TAG, verrsion)
