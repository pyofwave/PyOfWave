<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:w="http://pyofwave.info/2013/wave" 
		xmlns:xmlu="http://pyofwave.info/2013/xmlu" xmlns:s="http://pyofwave.info/2013/style">
	<xsl:template match="w:p">
		<xsl:choose>
			<xsl:when test="@w:s = 'h'">
				<xsl:element name="h{@w:l+1}">
					<xsl:attribute name="class">ws-dir-<xsl:value-of select="@w:d" /> ws-align-<xsl:value-of select="@w:a" /></xsl:attribute>
					<xsl:apply-templates />
				</xsl:element>
			</xsl:when>
			<xsl:otherwise>
				<div class="ws-{@w:s} ws-indent-{@w:l} ws-dir-{@w:d} ws-align-{@w:a}"><xsl:apply-templates /></div>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>
	<xsl:template match="w:a">
		<a>
			<xsl:attribute name="style">
				<xsl:if test="@s:color">color: #<xsl:value-of select="@s:color" />;</xsl:if>
				<xsl:if test="@s:backgroundColor">background-color: #<xsl:value-of select="@s:backgroundColor" />;</xsl:if>
				<xsl:if test="@s:fontFamily">font-family: <xsl:value-of select="@s:fontFamily" />;</xsl:if>
				<xsl:if test="@s:fontSize">font-size: <xsl:value-of select="@s:fontSize" />;</xsl:if>
				<xsl:if test="@s:fontStyle">font-style: <xsl:value-of select="@s:fontStyle" />;</xsl:if>
				<xsl:if test="@s:fontWeight">font-weight: <xsl:value-of select="@s:fontWeight" />;</xsl:if>
				<xsl:if test="@s:textDecoration">text-decoration: <xsl:value-of select="@s:textDecoration" />;</xsl:if>
				<xsl:if test="@s:verticalAlign">position:absolute; line-height: 1em; <xsl:choose>
					<xsl:when test="@s:verticalAlign = 'top'">top: 0.5em;</xsl:when>
					<xsl:when test="@s:verticalAlign = 'bottom'">bottom: 0.5em;</xsl:when>
				</xsl:choose></xsl:if>
			</xsl:attribute>
			<xsl:if test="@s:href"><xsl:attribute name="href"><xsl:value-of select="@s:href" /></xsl:attribute></xsl:if>
			<xsl:if test="@xmlu:user">
				<xsl:attribute name="data-bind">user: '<xsl:value-of select="@xmlu:user" />', userProperty: 'background,border-right'</xsl:attribute>
			</xsl:if>
			<xsl:apply-templates />
		</a>
	</xsl:template>
</xsl:stylesheet>
