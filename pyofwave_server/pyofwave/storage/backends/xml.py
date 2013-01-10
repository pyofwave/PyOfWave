"""
Implements in memory XMLu storage.
"""
from xml.etree import ElementTree as et
from copy import deepcopy

doc = {"":{None:et.Element("root"), "version":0}}
doc[""][0] = doc[""][None]

VERSION_TAG = "{http://pyofwave.info/2013/xmlu}version"

class XMLStorage(object):
	def searchDocuments(user, url=None, namespaces={}, xpath="", range_=slice(0,-1), depth=-1, version=None, restore=False):
		xml = doc[user][version]
		if url:
			xpath = "[@xmlu:src='{}']//{}".format(url, xpath)
		if restore:
			doc[user][None] = deepcopy(xml)
			doc[user]["version"] = version

		result = xml.findall(xpath, namespaces)[range_]
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
		permission = permission.get(

		if deltaTag == "append":
			if delta.attrib: xml.attrib.update(delta.attrib)
			if len(delta): xml.attrib.extend(list(delta))
		elif deltaTag == "update":
			if list(delta):
				xml.clear()
				xml.extend(list(delta))
			if delta.attrib: xml.attrib = delta.attrib
		elif deltaTag == "select":
			if xml.get(VERSION_TAG, "0") != delta.get(VERSION_TAG):
				raise ValueError # To maintain consistancy, selection is tied to versions.
##			self.select(xml, slice(*[int(i) for i in delta.get("{http://pyofwave.info/2013/xmlu}range".split("-")]), permission)
		elif deltaTag == "delete":
			xml.getParent().remove(xml)
