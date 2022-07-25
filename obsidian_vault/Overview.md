## Data-Driven Systems

### Data 
- different types of data
	- structured
	- semi-structured
	- unstructured
- data lakes vs. data swamps
- challeges in modern data-driven systems
	- data cleaning
	- data mangement

### Databases
- data models
	- structure (data structures to represent the data)
	- constraints (rules the data has to fulfill)
	- manipulation (querying)
- building blocks
	- entities
		- weak entities
	- attributes
	- relations (show how the entity sets interact with each other)
- database models
	- conceptual model
	- logical model
	- physical model
	$\to$ schema
- ER diagrams (represent relations between entities)
	- components (entities, relations, attributes)
	- translation into logical models

### Relational data bases 
- relation $\to$ mathematical definition
- constraints
	- key constraints (can be directly represented in ER)
	- uniqueness constraint
	- `NOT NULL`-constraint
	- foreign key constraint
- relational algebra (RA)
	- strategy for data manipulation
	- set operations ($\cup$, $\cap$, $\setminus$ , $\times$ )
	- RA operations
		- selection $\sigma$ (SQL: `WHERE`, pyspark: `filter`)
		- projection $\pi$ (SQL: `SELECT {cols}`, pyspark: `select`)
		- renaming $\rho$ (SQL: `AS`, pyspark: `withColumnRenamed`)
- Extended RA
	- extends RA with **joins**
	- joins
		- $\Join_{\,\theta}$ (SQL: `JOIN {table 2} ON {condition}`)
		- $\theta$ is boolean condition
		- equivalent to $\sigma_\text{condition} (R \times S)$
- table design
	- redudancy
	- anomalies
- [[Normalization]]
	- [[Normalform]]


## Knowledge Graphs and Semantic Web
### Semantic Web
- [[Semantic Web]]
- [[URI]]
- [[RDF]]
	- [[RDF Turtle]]
	- [[RDF Reification]]
	- [[RDF Schema]]
- [[OWL]]
- [[Knowledge Graph]]
	- [[DBPedia]]
	- [[Wikidata]]
- [[SPARQL]]

### Text Mining
- [[Text Mining]]
- [[NLP]]
	- [[Syntactical analysis]]
	- [[Semantical analysis]]
	- [[Statistical language model]]
	- [[NLP tasks]]
	- [[Entity Detection]]
	- [[Named entity recognition]]
	- [[Entity Linking]]
	- [[Information Extraction]]
	- [[Relation Extraction]]
	- [[Open Information Extraction]]



## Software Engineering

### Quality citeria
- quality of use (How good is it **in practice**?)
- outer and inner quality (How good is it **in theory**?)

### Process Models
- benefits of usage
- commonly used process models in software development
	- waterfall
	- V-model
	- SCRUM
- agile software development

### Requirements Analysis
- types of requirements
	- non-functional/technical requirements (**How** shall it be implemented?)
	- functional requirements (**What** shall it do?)
- criteria for good requirements
- modelling requirements
	- tools
	- use cases
- use case diagrams
	- actors
	- relationships between actors and use cases (multipliers, associations)
	- generalizations
	- relationships between use cases (`<<include>>` , `<<extend>>`)

### Object-oriented Analysis
- split **static model** (classes, relations) and **dynamic model** (states, transitions between states)

### Class diagrams
- macro level
	- building blocks
		- classes
		- associations
		- aggregations
		- compositions
		- inherictance
- micro-level
	- building blocks
		- attributes
		- operations
		- data types
		- default values
- further concepts
	- interfaces
	- comparision: abstract class $\leftrightarrow$ interface

### Package diagrams
- structure of the modelled system
- package
	- understandable on its own
	- strong cohesion
	- weak coupling with other packages

## Testing
- [[Quality]]
- [[Error Chain]]
- [[Testing]]
- [[Unit Test]]
- [[Integration Test]]
- [[System Test]]
- [[Acceptance Test]]
- [[Static Testing]]
- [[Dynamic Testing]]
	- [[Black-Box Testing]]
		- [[Equivalence classes testing]]
		- [[Boundary Value Analysis]]
	- [[White-Box Testing]]


## Security

### Basics
- Security goals
	- confidentiality
		Protection against access 
	- integrity
		Protection against manipulation
	- availablity
		Protection against disruption
- threats
	- disclosure
	- deception
	- disruption
	- usurpation
- safety $\leftrightarrow$ security
- attack
- strategies
	- prevention (**avoid** issues)
	- detection (**find** issues)
	- analysis (**prevent** the same error to **reoccur**)
- security policy $\leftrightarrow$ security mechanism

### Cryptography
- Cryptosystem (basic structure, encryption/decryption)
- cipher 
- keyspace
- symmetric cryptography $\leftrightarrow$ public-key cryptography
	- different sources of security
- properties of a strong cipher
	- confusion $\to$  hard to extract $K$ from $M$ and $C$
	- diffusion $\to$ hard to extract $M$ from $C$
	- Kerckhoff's principle
- symmetric ciphers
	- block ciphers
	- stream ciphers
- hash functions
	- one-way property
	- keyless and keyed hash functions
	- applications:
		- checksums
		- public-key cryptography
- key exchange (problems for multi-party cryptosystems)
- public and private keys (scalabitily, structure of a cryptosystem that uses this approach)
- Trapdoor one-way functions
	- usable problems
		- discrete logarithms
		- integer factorization
- Man-in-the-Middle Attacks
	- weaknesses of asymmetric cryptosystems
	- prevention mechanisms (key fingerprints, signing)