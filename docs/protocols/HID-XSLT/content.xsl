<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:w="http://pyofwave.info/2013/wave" xmlns:xmlu="http://pyofwave.info/2013/xmlu">
	<xsl:template match="w:p">
		<xsl:choose>
			<xsl:when test="@s = 'h'">
				<xsl:element name="h{@l+1}">
					<xsl:attribute name="class">ws-dir-<xsl:value-of select="@d" /> ws-align-<xsl:value-of select="@a" /></xsl:attribute>
					<xsl:apply-templates />
				</xsl:element>
			</xsl:when>
			<xsl:otherwise>
				<div class="ws-{@s} ws-indent-{@l} ws-dir-{@d} ws-align-{@a}"><xsl:apply-templates /></div>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>
	<xsl:template match="w:a">
		<a>
			<xsl:attribute name="style">
				<xsl:if test="@color">color: #<xsl:value-of select="@color" />;</xsl:if>
				<xsl:if test="@backgroundColor">background-color: #<xsl:value-of select="@backgroundColor" />;</xsl:if>
				<xsl:if test="@fontFamily">font-family: <xsl:value-of select="@fontFamily" />;</xsl:if>
				<xsl:if test="@fontSize">font-size: <xsl:value-of select="@fontSize" />;</xsl:if>
				<xsl:if test="@fontStyle">font-style: <xsl:value-of select="@fontStyle" />;</xsl:if>
				<xsl:if test="@fontWeight">font-weight: <xsl:value-of select="@fontWeight" />;</xsl:if>
				<xsl:if test="@textDecoration">text-decoration: <xsl:value-of select="@textDecoration" />;</xsl:if>
				<xsl:if test="@verticalAlign">position:absolute; <!-- position above, below in center --></xsl:if>
			</xsl:attribute>
			<xsl:if test="@href"><xsl:attribute name="href"><xsl:value-of select="@href" /></xsl:attribute></xsl:if>
			<xsl:apply-templates />
		</a>
	</xsl:template>
</xsl:stylesheet>
