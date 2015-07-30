# ---
# had to install rdflib using "pip rdflib"
# see https://rdflib.readthedocs.org/en/latest/gettingstarted.html
import rdflib

# this is Python's built-in XML processor
import xml.etree.ElementTree as etree

# results.xml is the SPARQL results file that I saved after querying for GeoNames IRIs
tree = etree.parse('results.xml')

# I searched the XML to find the uri elements, then put them in an array
resultsArray=tree.findall('.//{http://www.w3.org/2005/sparql-results#}uri')

#builtGraph is where I'm going to accumulate triples that I've scraped
builtGraph=rdflib.Graph()

#addedGraph contains triples that I got from a particular GeoNames RDF file
addedGraph=rdflib.Graph()

fileIndex=0
while fileIndex<len(resultsArray):
    #put something on the screen so that we can track progress
    print(fileIndex)
    #pull the text value for a particular node
    baseUri=resultsArray[fileIndex].text
    #the basUri is the IRI of the abstract place resource, must append 'about.rdf'
    #to get the URL of the file that contains the RDF that describes it
    getUri=baseUri+"about.rdf"
    try:
        #this retrieves the file and parses it into rdflib's triple form
        result = addedGraph.parse(getUri)
    except:
        #added this for the case where a URL is bad and an HTTP 404 results
        print(getUri)
    else:
        #when the file is retrieved successfully and parsed, UNION it into the
        #graph where I'm accumulating the whole set of triples
        builtGraph = builtGraph + addedGraph
    fileIndex=fileIndex+1
#this will serialize the triples as RDF/XML and save the results in a file
s = builtGraph.serialize(destination='geonames.rdf', format='xml')
