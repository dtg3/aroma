from lxml import etree
from xslt import *

def refactor(input, params, output):

	inputXML = etree.parse(input)
	xslt_root = etree.XML(xsl.HEADER + xsl.IDENTITY + xsl.duplicate("//src:aroma[@refactor='add_parameter']") + xsl.FOOTER)
	transform = etree.XSLT(xslt_root)
	outputXML = transform(inputXML)

	xslt_root = etree.XML(xsl.HEADER + xsl.IDENTITY + xsl.empty("//src:aroma[@refactor='add_parameter']/src:function/src:block/*") + xsl.FOOTER)
	transform = etree.XSLT(xslt_root)
	outputXML = transform(outputXML)

	param = params.split()

	xslt_root = etree.XML(xsl.HEADER + xsl.IDENTITY + xsl.insert_parameter("//src:aroma[@refactor='add_parameter']//src:function/src:parameter_list/src:param[last()]", param[0], param[1]) + xsl.FOOTER)
	transform = etree.XSLT(xslt_root)
	outputXML = transform(outputXML)

	xslt_root = etree.XML(xsl.HEADER + xsl.IDENTITY + xsl.insert_line_comment("//src:aroma[@refactor='add_parameter']", "TODO: Implement") + xsl.FOOTER)
	transform = etree.XSLT(xslt_root)
	outputXML = transform(outputXML)

	xslt_root = etree.XML(xsl.HEADER + xsl.IDENTITY + xsl.remove_aroma("//src:aroma[@refactor='add_parameter']") + xsl.FOOTER)
	transform = etree.XSLT(xslt_root)
	outputXML = transform(outputXML)

	print(etree.tostring(outputXML))
