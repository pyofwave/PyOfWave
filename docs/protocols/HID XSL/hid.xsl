<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:w="http://pyofwave.info/2013/wave" xmlns:xmlu="http://pyofwave.inof/2013/xmlu">
	<!-- It is necessary, not just for readability, to apply the XSL per element. This is because we want to replace just the elements we're told have changed, not the whole document (as that would drastically inturrupt user interaction) -->
	<!-- Class names are namespaced "w-" to avoid interference with the frame, and OO style upper-camelcase is used to indicate elements we consider "components" -->

	<!-- Javascript is used to push updates to this structure (wrapping the content in profile XML for contacts access), send updates, and apply collapse. -->

	<xsl:import href="participants.xsl" />
	<xsl:include href="content.xsl" />
	<xsl:template match="/" priority="-1">
		<xsl:apply-templates select="//w:*[0]"><xsl:with-param name="collapse" select="0" /></xsl:apply-templates>
	</xsl:template>

	<xsl:template name="collapse">
		<xsl:param name="target" select="@xmlu:src" />
		<xsl:param name="class" />
		<p class="w-collapse w-collapsed {$class}" data-for="{$target}"></p>
	</xsl:template>

	<!-- ########################## -->
	<xsl:template match="w:wave">
		<xsl:apply-templates select="w:wavelet"><xsl:with-param name="collapse" select="0" /></xsl:apply-templates>
	</xsl:template>

	<xsl:template match="w:wavelet">
		<xsl:param name="collapse" select="1" />
		<xsl:if select="$collapse"><xsl:call-template name="collapse" /></xsl:if>

		<div class="w-WaveletView" data-src="{@xmlu:src}">
			<ul class="w-ParticipantBar">
				<xsl:for-each select="w:participant[@w:status=online]">
					<li><xsl:call-template name="userprofile"><xsl:with-param name="border" select="1" /></xsl:call-template></li>
				</xsl:for-each>
				<li class="w-sep"></li>
				<xsl:for-each select="w:participant[@w:status=offline]">
					<li><xsl:call-template name="userprofile" /></li>
				</xsl:for-each>
				<li class="w-add" data-dropdown="select contact"></li>
			</ul>
			<xsl:call-template name="thread"><xsl:with-param name="collapse" select="0" /><xsl:with-param name="thread" select="w:thread[0]" /></xsl:apply-templates>
			<xsl:call-template name="tags"><xsl:with-param name="collapse" select="0" /></xsl:call-template>
		</div>
	</xsl:template>

	<xsl:template name="tags" xmlns:priv="http://pyofwave.info/2013/privaliges" xmlns:fn="http://www.w3.org/2005/xpath-functions">
		<ul class="w-TagBar" data-src="{fn:concat(@xmlu:src, '#tags')}">
			<xsl:for-each select="w:tags@*">
				<li data-src="{..@xmlu:src}">
					<xsl:if select="..@priv:perm"><!-- Private access -->
						<xsl:attribute name="class">w-public</xsl:attribute>
					</xsl:if>
					<span data-edit="key" data-dropdown="select tag"><xsl:value-of select="fn:nodename(.)" /></span>
					<xsl:if select=".">:<span data-edit="value"><xsl:value-of select="." /></span></xsl:if>
				</li>
			</xsl:for-each>
			<li class="w-add" data-edit="new @" data-dropdown="menu newtag">+</li>
		</ul>
	</xsl:template>

	<xsl:template match="w:thread" name="thread" xmlns:fn="http://www.w3.org/2005/xpath-functions">
		<xsl:param name="thread" select="." />		<!-- Calling this template directly ensures you'll always get a "Click to add a post" -->
		<xsl:param name="collapse" select="1" />
		<xsl:if select="$collapse"><xsl:call-template name="collapse" /></xsl:if>

		<ul class="w-ThreadView" data-src="{$thread@xmlu:src}">
			<xsl:apply-templates select="$thread/w:post" />
			<li class="w-add" data-edit="new wave:post">
				<xsl:call-template name="userborder"><xsl:with-param name="user" select="fn:subsring-after(/me, '://')" /></xsl:call-template>
				Click to add a post.
			</li>
		</ul>
	</xsl:template>

	<xsl:template match="w:post">
		<li class="w-PostView" data-src="{@xmlu:src}">
			<aside class="w-control">
				<time><xsl:value-of select="@xmlu:modified" /></time>
				<ul class="w-parts">
					<xsl:for-each select="w:participant">
						<li><xsl:call-template name="usercolor" /></li>
					</xsl:for-each>
				</ul>
			</aside>
			<article class="w-inner" data-edit="selection, -footer, -footer+ul">
				<xsl:call-template name="userborder"><xsl:with-param name="user" select="w:participant[0]" /></xsl:call-template>
				<xsl:apply-templates select="w:p" />
				<footer>
					<xsl:call-template name="collapse">
						<xsl:with-param name="target" select="fn:concat(@xmlu:src, '#tags')" />
						<xsl:with-param name="class" select="'w-tags'" />
					</xsl:call-template>
					<xsl:call-template name="collapse"><xsl:with-param name="target" select="w:thread[0]@xmlu:src" /></xsl:call-template>
				</footer>
				<xsl:call-template name="tags" />
			</article>
			<xsl:call-template name="thread"><xsl:with-param name="thread" select="w:thread[0]" /><xsl:with-param name="collapse" select="0" /></xsl:call-template>
		</li>
	</xsl:template>
</xsl:stylesheet>
