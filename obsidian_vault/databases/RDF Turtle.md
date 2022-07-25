## RDF Turtle
Nowadays Terse [[RDF]] Triple Language (TURTLE) is used to express [[RDF]] in a machine readable way – TURTLE is also a W3C Recommendation

Schema:
```mermaid
graph TD;
	http://dbpedia.org/page/Alan_Turing--http://dbpedia.org/ontology/academicDiscipline-->http://dbpedia.org/page/Mathematician;
	http://dbpedia.org/page/Alan_Turing--http://dbpedia.org/property/birthPlace-->http://dbpedia.org/page/London;
```

RDF Turtle:
```xml-doc
@prefix dbo:<http://dbpedia.org/ontology/> .
@base <http://dbpedia.org/resource/> .

<Alan_Turing> dbo:academicDiscipline <Mathematician>;
              dbo:birthPlace         <London> .
```

All entities in <> specified by the [[URI]] http://dbpedia.org/resource/
