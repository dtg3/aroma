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

   <xsl:template match="@* | node()" name="identity">
      <xsl:copy>
         <xsl:apply-templates select="@* | node()"/>
      </xsl:copy>
   </xsl:template>

   <xsl:template match="//src:unit[@filename='animal.hpp']/src:class/src:block/src:private[last()]" xml:space="preserve">
      <xsl:copy-of select="."/>
      <xsl:apply-templates select="//src:private/src:aroma[@refactor='pull_up']">
         <xsl:copy-of select="."/>
      </xsl:apply-templates>
      <xsl:text>&#xa;</xsl:text>
   </xsl:template>

<!-- REMOVE OLD STUFF
   <xsl:template match="//src:aroma[@refactor='pull_up']"/> -->

</xsl:stylesheet>
