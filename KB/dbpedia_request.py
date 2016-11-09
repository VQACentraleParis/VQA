# -*- coding: utf-8 -*-

from SPARQLWrapper import SPARQLWrapper, JSON



def get_description(word_to_request):

    

    """
    word_to_request : word you want to request on DBPedia as a string, first letter of each word must be in capital letter.

    """
    # Creation of the query
    
    query = """PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT DISTINCT ?comment WHERE{

    ?entry rdfs:label'""" + str(word_to_request) + """'@en.

    ?entry rdfs:comment?comment.

    }"""

    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setReturnFormat(JSON)

    sparql.setQuery(query)  # the previous query as a literal string
    res = sparql.query().convert()
    eng_descrip =''
    for result in res["results"]["bindings"]:
        if result["comment"]["xml:lang"]=='en':
            eng_descrip = result["comment"]["value"]

    return eng_descrip
