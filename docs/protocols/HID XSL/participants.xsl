<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0" xmlns:xls="http://www.w3.org/1999/XSL/Transform" xmlns:fn="http://www.w3.org/2005/xpath-functions"
		 xmlns:prof="http://pyofwave.info/2013/profile" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:foaf="http://xmlns.com/foaf/0.1">
	<xsl:template name="userprofile">
		<xsl:param name="border" />
		<xsl:param name="user" select="." />
		<xsl:variable name="u"><xsl:call-template name="loaduser"><xsl:with-param name="user" select="$user" /></xsl:call-template></xsl:variable>
		<img>
			<xsl:attribute name="title"><xsl:value-of select="$user" /></xsl:attribute>
			<xsl:attribute name="data-dropdown">profile <xsl:value-of select="$user" /></xsl:attribute>
			<xsl:attribute name="alt"><xsl:value-of select="$user" />'s avatar.</xsl:attribute>
			<xsl:attribute name="src"><xsl:value-of select="$u@foaf:depiction | $u/foaf:depiction@rdf:resource" /></xsl:attribute>
			<xsl:if select="$border"><xsl:call-template name="userborder"><xsl:with-param name="user" select="$user" /></xsl:call-template></xsl:if>
		</img>
		<span>
			<xsl:value-of select="$u@foaf:nick | $u/foaf:nick | $u@foaf:name | $u/foaf:name | $u@foaf:firstName | $u/foaf:firstName | $u@foaf:givenName | $u/foaf:givenName" />
		</span>
	</xsl:template>

	<xsl:template name="userborder">
		<xsl:param name="user" select="." />
		<xsl:variable name="u"><xsl:call-template name="loaduser"><xsl:with-param name="user" select="$user" /></xsl:call-template></xsl:variable>
		<xsl:attribute name="style">border-color: #<xsl:value-of select="$u@prof:rgbColor | $u/prof:rgbColor" /></xsl:attribute>
	</xsl:template>

	<xsl:template name="usercolor">
		<xsl:param name="user" select="." />
		<xsl:variable name="u"><xsl:call-template name="loaduser"><xsl:with-param name="user" select="$user" /></xsl:call-template></xsl:variable>
		<xsl:variable name="a"><xsl:call-template name="loaduser"><xsl:with-param name="user" select="$user@w:alias" /></xsl:call-template></xsl:variable>
		<xsl:attribute name="style">background: #<xsl:value-of select="$u@prof:rgbColor | $u/prof:rgbColor" />;
																border-color: #<xsl:value-of select="$a@prof:rgbColor | $a/prof:rgbColor" /></xsl:attribute>
		<xsl:attribute name="title"><xsl:value-of select="$user" /> of alias <xsl:value-of select="$user@w:alias" /></xsl:attribute>
	</xsl:template>

	<xsl:template name="loaduser">
		<xsl:param name="user" select="." />
		<xsl:copy-of select="/me//[@rdf:about='wave://'+$user]" />
	</xsl:template>
</xsl:stylesheet>
