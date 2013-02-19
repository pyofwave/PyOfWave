<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:w="http://pyofwave.info/2013/wave" 
		xmlns:xmlu="http://pyofwave.info/2013/xmlu">
	<xsl:include href="content.xsl" />
	<xsl:strip-space elements="*" />

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
					<li>
						<xsl:attribute name="data-bind">with: contacts()['<xsl:value-of select="@xmlu:user" />']</xsl:attribute>
						<img src="unknown.png">
							<xsl:attribute name="data-bind">attr: {src: 'depiction', alt: '<xsl:value-of select="@xmlu:user" />\'s avatar.', style: 'border-color: #' + color}</xsl:attribute>
						</img>
						<span data-bind="text: nick"></span>
					</li>
				</xsl:for-each>
				<li class="wave-button wave-icon-add wave-add-participant">+</li>
			</ul>
			<xsl:call-template name="thread"><xsl:with-param name="el" select="w:thread" /><xsl:with-param name="collapse" select="0" /></xsl:call-template>
		</div>
	</xsl:template>
	<xsl:template name="thread" match="w:thread">
		<xsl:param name="collapse" select="1" /><xsl:param name="el" select="." />
		<xsl:call-template name="collapse"><xsl:with-param name="collapse" select="$collapse" /></xsl:call-template>

		<ul class="wave-Thread">
			<xsl:apply-templates select="$el/w:post" />
			<li class="wave-js-appendpost">Edit to add post</li>
		</ul>
	</xsl:template>
	<xsl:template match="w:post">
		<li class="wave-Post">
			<div class="inner" data-bind="user: '{w:participant/@xmlu:user}'">
				<aside class="wave-Info">
					<time><xsl:value-of select="@xmlu:modified" /></time>
					<ol class="contributors"><xsl:for-each select="w:participant/@xmlu:user">
						<li data-bind="user: '{.}', userProperty: 'background/border'"></li>
					</xsl:for-each></ol>
				</aside>
				<xsl:apply-templates select="w:p" />
			</div>
			<xsl:call-template name="thread"><xsl:with-param name="el" select="w:thread" /></xsl:call-template>
		</li>
	</xsl:template>
</xsl:stylesheet>
