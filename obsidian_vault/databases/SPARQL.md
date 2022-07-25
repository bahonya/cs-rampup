## <a>S</a>PARQL <a>P</a>rotocol <a>A</a>nd <a>R</a>DF <a>Q</a>uery <a>L</a>anguage 
SPARQL is a query language and a protocol for accessing [[RDF]] designed by the W3C RDF Data Access Working Group

SPARQL Query language is used to
- extract information in the form of URIs, blank nodes, plain and typed literals
- extract RDF subgraphs
- construct new RDF graphs based on information in the queried graphs

Basic idea is to define a set of Triple Patterns – Similar to an [[RDF]] Triple (subject, predicate, object), but any component can be a query variable, also literal subjects are allowed
- rdf:type rdf:type rdf:Property

Matching a triple pattern to a graph introduces bindings between variables and RDF Terms 
- ?book dc:title ?title

SPARQL uses a SQL-style syntax:
```sql
dc: <http://purl.org/dc/elements/1.1/>
SELECT ?title 
FROM http://example.org/library 
WHERE { dc:title ?title }
```

- <a>SELECT</a> identifies the variables to be returned
- <a>FROM</a> gives the name of the graph to be queried
- <a>WHERE</a> query pattern as a list of triple patterns
- Plus additional functions like <a>LIMIT</a>, <a>OFFSET</a>, or <a>ORDER BY</a>
- <a>CONSTRUCT</a> – Returns an RDF graph constructed by substituting variables in a set of triple templates
- <a>DESCRIBE</a> – Returns an RDF graph that describes the resources found
- <a>ASK</a> – Returns whether a query pattern matches or not

Examples:
- *Find the URL of the blog by the person named Jon Foobar*
```sql
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
SELECT ?url
	FROM <bloggers.rdf>
	WHERE { ?contributor foaf:name "Jon Foobar" .
			?contributor foaf:weblog ?url .
	}
```

- *Assume a graph describing people: return the full names of all people in the graph!*
```xml
@prefix ex: <http://example.org/#>.
@prefix vcard: <http://www.w3.org/vcard-rdf/3.0#>.
ex:john
	vcard:FN "John Smith" ;
	vcard:N [
		vcard:Given "John" ;
		vcard:Family "Smith" ] ;
	ex:hasAge 32 ;
	ex:marriedTo :mary .
ex:mary
	vcard:FN "Mary Smith" ;
	 vcard:N [
		 vcard:Given "Mary" ;
		 vcard:Family "Smith" ] ;
	ex:hasAge 29 .
```
```sql
SELECT ?fullName
WHERE {?x vCard:FN ?fullName}
=================
fullName
=================
‘John Smith’
‘Mary Smith’
```
*Return all people over 30 in the KB*
```sql
SELECT ?x
WHERE {?x hasAge ?age .
FILTER(?age > 30)}
=================
x
=================
<http://example.org/#john>
```
*Are there any married people in the graph?*
```sql
ASK { ?person ex:marriedTo ?spouse }
=================
yes
```