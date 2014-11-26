<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
   xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
   xmlns:src="http://www.sdml.info/srcML/src"
   xmlns="http://www.sdml.info/srcML/src"
   xmlns:cpp="http://www.sdml.info/srcML/cpp"
   xmlns:str="http://exslt.org/strings"
   xmlns:func="http://exslt.org/functions"
   xmlns:exsl="http://exslt.org/common"
   extension-element-prefixes="str exsl func"
   exclude-result-prefixes="src"
   version="1.0">

   <xsl:output method="xml" omit-xml-declaration="no" version="1.0" encoding="UTF-8"/>

   <xsl:template match="@* | node()">
      <xsl:copy>
         <xsl:apply-templates select="@* | node()"/>
      </xsl:copy>
   </xsl:template>

   <xsl:template match="//src:function[@refactor='add_parameter']//src:parameter_list/src:param[last()]" xml:space="preserve">
      <xsl:copy-of select="."/>,<xsl:text> </xsl:text><param><decl><type><name>TYPE</name></type><xsl:text> </xsl:text><name>PARAM</name></decl></param>
   </xsl:template>

   <xsl:template match="//src:call[./src:name = 'successor']//src:argument_list//src:argument[last()]" xml:space="preserve">
      <xsl:copy-of select="."/>,<xsl:text> </xsl:text><argument><expr><name>PARAM</name></expr></argument>
   </xsl:template>

<!-- ADD COMMENT
   <xsl:template match="//src:function[@refactor='add_parameter']" xml:space="preserve">
      <comment>// Test</comment><xsl:text>&#xa;</xsl:text><xsl:copy-of select="."/>
   </xsl:template>
-->

   <xsl:template match="//src:function[@refactor='add_parameter']" xml:space="preserve">
      <xsl:copy-of select="."/>
      <xsl:text>&#xa;&#xa;</xsl:text>
      <xsl:copy-of select="."/>
   </xsl:template>

</xsl:stylesheet>