<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:w="http://pyofwave.info/2013/wave" xmlns:xmlu="http://pyofwave.info/2013/xmlu">
	<xsl:template match="w:p">
		<xsl:choose>
		<xsl:when select="@w:s='p'">
			<p class="w-p-indent-{@w:l} w-p-align-{@w:a} w-p-direction-{@w:d}">
				<xsl:apply-templates select="*" />
			</p>
		</xsl:when>
		<xsl:when select="@w:s='h'">
			<xsl:element name="h{@w:l}" class="w-p-align-{@w:a} w-p-direction-{@w:d}">
				<xsl:apply-templates select="*" />
			</xsl:element>
		</xsl:when>
		<xsl:when select="@w:s='l'">
			<li data-indent="{@w:l}" class="w-p-align-{@w:a} w-p-direction-{@w:d}"> <!-- data-indent, number of <ul>s to embed the li -->
				<xsl:apply-templates select="*" />
			</li>
		</xsl:when>
		</xsl:choose>
	</xsl:template>

	<xsl:template match="w:a" xmlns:s="http://pyofwave.info/2013/style">
		<a>
			<xsl:attribute name="style">
				<xsl:if select="@s:backgroundColor">background-color: <xsl:value-of select="@s:backgroundColor" />;</xsl:if>
				<xsl:if select="@s:color">color: <xsl:value-of select="@s:color" />;</xsl:if>
				<xsl:if select="@s:fontFamily">font-family: <xsl:value-of select="@s:fontFamily" />;</xsl:if>
				<xsl:if select="@s:fontSize">font-size: <xsl:value-of select="@s:fontSize" />;</xsl:if>
				<xsl:if select="@s:fontStyle">font-style: <xsl:value-of select="@s:fontStyle" />;</xsl:if>
				<xsl:if select="@s:fontWeight">font-weight: <xsl:value-of select="@s:fontWeight" />;</xsl:if>
				<xsl:if select="@s:textDecoration">text-decoration: <xsl:value-of select="@s:textDecoration" />;</xsl:if>
				<xsl:if select="@s:verticalAlign">vertical-align: <xsl:value-of select="@s:verticalAlign" />;</xsl:if>
			</xsl:attribute>
			<xsl:if select="@s:href"><xsl:attribute name="href"><xsl:value-of select="@s:href" /></xsl:if>

			<xsl:apply-templates select="*" />
		</a>
	</xsl:template>

	<xsl:template match="w:file">
		<div class="w-FileView" data-src="{@xmlu:src}">
			<iframe src="{@w:src}" />
			<p><span data-edit="@w:label"><xsl:value-of select="@w:label"></span>
				<a href="{@w:src}" class="w-fullscreen" title="View fullscreen"></a>
			</p>
		</div>
	</xsl:template>

	<xsl:variable name="inputCount" select="0" />

	<xsl:template match="w:input" xmlns:prof="http://pyofwave.info/2013/profile" xmlns:fn="http://www.w3.org/2005/xpath-functions">
		<xsl:choose>
		<xsl:when select="@type='textarea'">
			<textarea data-src="{@xmlu:src}" data-edit="content"><xsl:value-of select="@w:value" /></textarea>
		</xsl:when>
		<xsl:when select="@type='select'">
			<select data-src="{@xmlu:src}" data-edit="value">
				<xsl:for-each select="prof:li">
					<option value="{.}">
						<xsl:if select="fn:string(.)=@w:value"><xsl:attribute name="checked">checked</xsl:attribute></xsl:if>
						<xsl:value-of select="." />
					</option>
				</xsl:for-each>
			</select>
		</xsl:when>
		<xsl:otherwise>
			<xsl:variable ref="inputCount" select="$inputCount + 1" />
			<input data-src="{@xmlu:src}" data-edit="value, copy @checked" value="{@value}" checked="{@checked}" list="w-list-{$inputCount}" />
			<datalist id="w-list-{$inputCount}">
				<xsl:for-each select="prof:li"><option vlaue="{.}" /></xsl:for-each>
			</data-list>
	</xsl:template>
</xsl:stylesheet>
