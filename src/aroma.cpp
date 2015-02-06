#include <iostream>
#include <vector>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <assert.h>

#include <libxml/tree.h>
#include <libxml/parser.h>
#include <libxml/xpath.h>
#include <libxml/xpathInternals.h>

#if defined(LIBXML_XPATH_ENABLED) && defined(LIBXML_SAX1_ENABLED)

int  execute_xpath_expression(const char* filename, const xmlChar* xpathExpr, const char* ns);
int  register_namespaces(xmlXPathContextPtr xpathCtx, const xmlChar* nsList);
void print_xpath_nodes(xmlNodeSetPtr nodes, FILE* output);

int main( int argc, const char* argv[] )
{
	std::vector< std::pair<std::string,std::string> > xml_namespaces;
    xml_namespaces.push_back(std::make_pair(std::string("src"),std::string("http://www.sdml.info/srcML/src")));
    xml_namespaces.push_back(std::make_pair(std::string("xmlns"),std::string("http://www.sdml.info/srcML/src")));
    xml_namespaces.push_back(std::make_pair(std::string("cpp"),std::string("http://www.sdml.info/srcML/cpp")));

	/* Parse command line and process file */
	std::cerr << "NUMBER OF ARGS: " << argc << "\n";
    if(argc != 3) {
		std::cerr << "Error: wrong number of arguments.\n";
		return(-1);
    }

    /* Init libxml */     
    xmlInitParser();
    LIBXML_TEST_VERSION

    const char* filename = argv[1];
    const xmlChar* xpathExpr = BAD_CAST argv[2];

    /* Load XML document */
    xmlDocPtr doc = xmlParseFile(filename);
    if (doc == NULL) {
        fprintf(stderr, "Error: unable to parse file \"%s\"\n", filename);
        return(-1);
    }

    /* Create xpath evaluation context */
    xmlXPathContextPtr xpathCtx = xmlXPathNewContext(doc);
    if(xpathCtx == NULL) {
        fprintf(stderr,"Error: unable to create new XPath context\n");
        xmlFreeDoc(doc); 
        return(-1);
    }

    /* Register namespaces from list */
    for (size_t i = 0; i < xml_namespaces.size(); ++i) {
        if(xmlXPathRegisterNs(xpathCtx, BAD_CAST xml_namespaces[i].first.c_str(), BAD_CAST xml_namespaces[i].second.c_str()) != 0) {
            fprintf(stderr,"Error: unable to register NS with prefix=\"%s\" and href=\"%s\"\n", xml_namespaces[i].first.c_str(), xml_namespaces[i].second.c_str());
            xmlXPathFreeContext(xpathCtx); 
            xmlFreeDoc(doc); 
            return(-1); 
        }
    }

    /* Evaluate xpath expression */
    xmlXPathObjectPtr xpathObj = xmlXPathEvalExpression(xpathExpr, xpathCtx);
    if(xpathObj == NULL) {
        fprintf(stderr,"Error: unable to evaluate xpath expression \"%s\"\n", xpathExpr);
        xmlXPathFreeContext(xpathCtx); 
        xmlFreeDoc(doc); 
        return(-1);
    }

    /* Print results */
    print_xpath_nodes(xpathObj->nodesetval, stdout);

    /* Cleanup */
    xmlXPathFreeObject(xpathObj);
    xmlXPathFreeContext(xpathCtx); 
    xmlFreeDoc(doc); 

    /* Shutdown libxml */
    xmlCleanupParser();

    return 0; 
}


/**
 * print_xpath_nodes:
 * @nodes:		the nodes set.
 * @output:		the output file handle.
 *
 * Prints the @nodes content to @output.
 */
void
print_xpath_nodes(xmlNodeSetPtr nodes, FILE* output) {
    xmlNodePtr cur;
    int size;
    int i;
    
    assert(output);
    size = (nodes) ? nodes->nodeNr : 0;
    
    fprintf(output, "Result (%d nodes):\n", size);
    for(i = 0; i < size; ++i) {
	assert(nodes->nodeTab[i]);
	
	if(nodes->nodeTab[i]->type == XML_NAMESPACE_DECL) {
	    xmlNsPtr ns;
	    
	    ns = (xmlNsPtr)nodes->nodeTab[i];
	    cur = (xmlNodePtr)ns->next;
	    if(cur->ns) { 
	        fprintf(output, "= namespace \"%s\"=\"%s\" for node %s:%s\n", 
		    ns->prefix, ns->href, cur->ns->href, cur->name);
	    } else {
	        fprintf(output, "= namespace \"%s\"=\"%s\" for node %s\n", 
		    ns->prefix, ns->href, cur->name);
	    }
	} else if(nodes->nodeTab[i]->type == XML_ELEMENT_NODE) {
	    cur = nodes->nodeTab[i];   	    
	    if(cur->ns) { 
    	        fprintf(output, "= element node \"%s:%s\"\n", 
		    cur->ns->href, cur->name);
	    } else {
    	        fprintf(output, "= element node \"%s\"\n", 
		    cur->name);
	    }
	} else {
	    cur = nodes->nodeTab[i];    
	    fprintf(output, "= node \"%s\": type %d\n", cur->name, cur->type);
	}
    }
}

#else
int main(void) {
    fprintf(stderr, "XPath support not compiled in\n");
    exit(1);
}
#endif