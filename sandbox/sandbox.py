from lxml import etree

inputXML = etree.parse('../test/pull_up/pull_up.xml')
xslt_root = etree.parse('test.xsl')
transform = etree.XSLT(xslt_root)
outputXML = transform(inputXML)

print(etree.tostring(outputXML))