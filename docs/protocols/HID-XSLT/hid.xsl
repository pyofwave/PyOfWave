<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:w="http://pyofwave.info/2013/wave" xmlns:xmlu="http://pyofwave.info/2013/xmlu">
	<xsl:template match="/*" priority="-1">
		<xsl:apply-templates select="w:*"><xsl:with-param name="collapse" select="0" /></xsl:apply-templates>
	</xsl:template>
	<xsl:template name="collapse">
		<xsl:param name="collapse" />
		<xsl:if test="$collapse"><p class="wave-collapse wave-collapsed" /></xsl:if>
	</xsl:template>


	<xsl:template match="w:wave">
		<xsl:param name="collapse" />
		<xsl:apply-templates select="w:wavelet"><xsl:with-param name="collapse" select="$collapse" /></xsl:apply-templates>
	</xsl:template>
	<xsl:template match="w:wavelet">
		<xsl:param name="collapse" select="1" />
		<xsl:call-template name="collapse"><xsl:with-param name="collapse" select="$collapse" /></xsl:call-template>

		<div class="wave-Wavelet">
			<ul class="wave-ParticipantBar">
				<xsl:for-each select="w:participant">
					<li><xsl:value-of select="@xmlu:user" /></li>
				</xsl:for-each>
				<li class="wave-button wave-icon-add wave-add-participant">+</li>
			</ul>
			<xsl:apply-templates select="w:thread" />
		</div>
	</xsl:template>
	<xsl:template match="w:thread">
		<xsl:param name="collapse" select="1" />
		<xsl:call-template name="collapse"><xsl:with-param name="collapse" select="$collapse" /></xsl:call-template>

		<ul class="wave-Thread">
			<xsl:apply-templates />
			<li class="wave-js-appendpost">Edit to add post</li>
		</ul>
	</xsl:template>
	<xsl:template match="w:post">
		<li class="wave-Post">
			<div class="inner">
				<aside class="wave-Info"></aside>
				<xsl:apply-templates select="w:p" />
			</div>
			<xsl:apply-templates select="w:thread" />
		</li>
	</xsl:template>

	<!-- TODO: enhance semantics for stylings/interaction. -->
	<xsl:template match="w:p">
		<div><xsl:apply-templates /></div>
	</xsl:template>
	<xsl:template match="w:a">
		<a><xsl:apply-templates /></a>
	</xsl:template>
</xsl:stylesheet>
