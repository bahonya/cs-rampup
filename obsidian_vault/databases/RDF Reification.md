## RDF Reification
[[RDF]] applications sometimes need to describe other [[RDF]] statements using [[RDF]]. E.g., to record when statements were made, who made them, … so-called provenance information

Example:
```
Tolkien -> wrote -> Lord of the rings
           /|\
            |
        Wikipedia said that
```
[[RDF]]:
```xml-doc
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
_:x rdf:type rdf:Statement .
_:x rdf:subject :Tolkien .
_:x rdf:predicate :wrote .
_:x rdf:object :LordOfTheRings .
_:x :said :Wikipedia .
```

### See also
[[RDF Turtle]]