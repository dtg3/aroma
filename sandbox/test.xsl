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

   <xsl:template match="//src:aroma[@refactor='add_parameter']//src:parameter_list/src:parameter" xml:space="preserve">
      <xsl:copy-of select="."/><TEMP/>
      <!--<xsl:text>, </xsl:text><param><decl><type><name>TYPE</name></type><xsl:text> </xsl:text><name>PARAM</name></decl></param>-->
   </xsl:template>

</xsl:stylesheet>