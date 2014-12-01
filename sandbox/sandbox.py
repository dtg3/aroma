from lxml import etree

ns = {'src': 'http://www.sdml.info/srcML/src',
                  'cpp': 'http://www.sdml.info/srcML/cpp'}

inputXML = etree.parse('../test/pull_up/pull_up.xml')

'aroma refactor="pull_up" role="source"'

result = inputXML.xpath("//src:private/src:aroma[@refactor='pull_up' and @role='source']/src:decl_stmt",
							namespaces=ns)

for res in result:
	print(etree.tostring(res))

xslt_root = etree.parse('test.xsl')
transform = etree.XSLT(xslt_root)
outputXML = transform(inputXML)

print(etree.tostring(outputXML))
