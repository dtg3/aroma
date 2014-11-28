from lxml import etree

inputXML = etree.parse('../test/add_parameter/param_decl.xml')
xslt_root = etree.parse('test.xsl')
transform = etree.XSLT(xslt_root)
outputXML = transform(inputXML)

print(etree.tostring(outputXML))