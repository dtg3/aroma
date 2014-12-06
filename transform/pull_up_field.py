from lxml import etree
from xslt import *

def locate_fields(inputXML):
  ns = {'src': 'http://www.sdml.info/srcML/src',
          'cpp': 'http://www.sdml.info/srcML/cpp'}  

  result = inputXML.xpath("//src:private/src:aroma[@refactor='pull_up' and @role='source']/src:decl_stmt", namespaces=ns)

  fields = []

  for res in result:
    field = etree.tostring(res).replace(' xmlns="http://www.sdml.info/srcML/src" xmlns:cpp="http://www.sdml.info/srcML/cpp"', '')
    if field not in fields:
      fields.append(field)

  return fields


def refactor(input, output):

  inputXML = etree.parse(input)
  xslt_root = etree.XML(xsl.HEADER + xsl.IDENTITY + xsl.move_fields('''//src:aroma[@refactor='pull_up' and @role='destination']/src:class/src:block/src:private[last()]''', locate_fields(inputXML)) + xsl.FOOTER)
  transform = etree.XSLT(xslt_root)
  outputXML = transform(inputXML)

  xslt_root = etree.XML(xsl.HEADER + xsl.IDENTITY + xsl.remove_aroma("//src:aroma[@refactor='pull_up' and @role='destination']") + xsl.FOOTER)
  transform = etree.XSLT(xslt_root)
  outputXML = transform(outputXML)

  print('''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n''' + etree.tostring(outputXML))
