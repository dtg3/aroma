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

INSERT_PARAMETER = '''\
   <xsl:template match="//src:aroma[@refactor='add_parameter']//src:function/src:parameter_list/src:param[last()]" xml:space="preserve">
      <xsl:copy-of select="."/>,<xsl:text> </xsl:text><param><decl><type><name>TYPE</name></type><xsl:text> </xsl:text><name>PARAM</name></decl></param>
   </xsl:template>

'''

INSERT_ARGUMENT = '''\
   <xsl:template match="//src:call[./src:name = 'successor']//src:argument_list//src:argument[last()]" xml:space="preserve">
      <xsl:copy-of select="."/>,<xsl:text> </xsl:text><argument><expr><name>PARAM</name></expr></argument>
   </xsl:template>

'''

def insert_parameter(match, param_type, param_name):
   param = "<xsl:template match=" + "\"" + match + "\"" + " xml:space=\"preserve\">\n"
   param += "<xsl:copy-of select=\".\"/>,<xsl:text> </xsl:text><param><decl><type><name>" + param_type + "</name></type><xsl:text> </xsl:text><name>" + param_name + "</name></decl></param>\n"
   param += "</xsl:template>\n"
   return param

def insert_line_comment(match, content):
   comment = "<xsl:template match=" + "\"" + match + "\"" + " xml:space=\"preserve\">\n"
   comment += "<comment>// " + content + "</comment><xsl:text>&#xa;</xsl:text><xsl:copy-of select=\".\"/>\n"
   comment += "</xsl:template>"
   return comment

def duplicate(match):
   dup = "<xsl:template match=" + "\"" + match + "\"" + " xml:space=\"preserve\">\n"
   dup += '''\
      <xsl:copy-of select="./*"/>
      <xsl:text>&#xa;&#xa;</xsl:text>
      <xsl:copy-of select="."/>
      </xsl:template>

      '''
   return dup;

def remove_aroma(match):
   rem = "<xsl:template match=" + "\"" + match + "\"" + " xml:space=\"preserve\">\n"
   rem += '''\
      <xsl:copy-of select="./*"/>
      </xsl:template>

      '''
   return rem;

def empty(match):
   clear =  "<xsl:template match=" + "\"" + match + "\"" + " xml:space=\"preserve\"/>\n"
   return clear

def replace_contents(match, contents):
   new =  "<xsl:template match=" + "\"" + match + "\"" + " xml:space=\"preserve\"/>\n"
   new += contents
   new += "</xsl:template>"
   return new
