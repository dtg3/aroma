HEADER = '''\
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

'''

IDENTITY = '''\
   <xsl:template match="@* | node()">
      <xsl:copy>
         <xsl:apply-templates select="@* | node()"/>
      </xsl:copy>
   </xsl:template>

'''

FOOTER = '''\
</xsl:stylesheet>
'''


INSERT_ARGUMENT = '''\
   <xsl:template match="//src:call[./src:name = 'successor']//src:argument_list//src:argument[last()]" xml:space="preserve">
      <xsl:copy-of select="."/>,<xsl:text> </xsl:text><argument><expr><name>PARAM</name></expr></argument>
   </xsl:template>

'''

def insert_parameter(match, param_type, param_name):
   param = "<xsl:template match=" + "\"" + match + "\"" + " xml:space=\"preserve\">"
   param += "<xsl:copy-of select=\".\"/><xsl:text>, </xsl:text><param><decl><type><name>" + param_type + "</name></type><xsl:text> </xsl:text><name>" + param_name + "</name></decl></param></xsl:template>"
   return param

def insert_line_comment(match, content):
   comment = "<xsl:template match=" + "\"" + match + "\"" + " xml:space=\"preserve\">"
   comment += "<comment>// " + content + "</comment><xsl:text>&#xa;</xsl:text><xsl:copy-of select=\".\"/>"
   comment += "</xsl:template>"
   return comment

def duplicate(match):
   dup = "<xsl:template match=" + "\"" + match + "\"" + " xml:space=\"preserve\">"
   dup += "<xsl:copy-of select=\"./*\"/>"
   dup += "<xsl:text>&#xa;&#xa;</xsl:text>"
   dup += "<xsl:copy-of select=\".\"/>"
   dup += "</xsl:template>"
   return dup;

def remove_aroma(match):
   rem = "<xsl:template match=" + "\"" + match + "\"" + " xml:space=\"preserve\">"
   rem += "<xsl:copy-of select=\"./*\"/>"
   rem += "</xsl:template>"
   return rem;

def empty(match):
   clear =  "<xsl:template match=" + "\"" + match + "\"" + " xml:space=\"preserve\"/>"
   return clear

def replace_contents(match, contents):
   new =  "<xsl:template match=" + "\"" + match + "\"" + " xml:space=\"preserve\"/>"
   new += contents
   new += "</xsl:template>"
   return new
