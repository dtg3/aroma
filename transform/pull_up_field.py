from lxml import etree
from xslt import *

ns = {'src': 'http://www.sdml.info/srcML/src',
          'cpp': 'http://www.sdml.info/srcML/cpp'}

def locate_fields(inputXML):
  result = inputXML.xpath("//src:private/src:aroma[@refactor='pull_up' and @role='source']/src:decl_stmt", namespaces=ns)

  fields = []

  for res in result:
    field = etree.tostring(res).replace(' xmlns="http://www.sdml.info/srcML/src" xmlns:cpp="http://www.sdml.info/srcML/cpp"', '')
    if field not in fields:
      fields.append(field)

  return fields

def protected_accessor(inputXML):
  if len(inputXML.xpath("//src:aroma[@refactor='pull_up' and @role='destination']/src:class/src:block/src:protected",
                     namespaces=ns)) > 0:
    return True
  else:
    return False



def refactor(input, output):

  inputXML = etree.parse(input)
  xslt_root = etree.XML(xsl.HEADER + xsl.IDENTITY + xsl.move_fields('''//src:aroma[@refactor='pull_up' and @role='destination']/src:class/src:block''', locate_fields(inputXML), protected_accessor(inputXML)) + xsl.FOOTER)
  transform = etree.XSLT(xslt_root)
  outputXML = transform(inputXML)

  xslt_root = etree.XML(xsl.HEADER + xsl.IDENTITY + xsl.remove_aroma("//src:aroma[@refactor='pull_up' and @role='destination']") + xsl.FOOTER)
  transform = etree.XSLT(xslt_root)
  outputXML = transform(outputXML)

  print('''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n''' + etree.tostring(outputXML))
