## Named Entity Recognition
Named entity recognition (NER) takes **texts** and outputs the detected **named entities**
- NER usually outputs the entity **mention** and its **type**
- NER systems work with **rules** (either hand-written or learned by deep learning architectures)
![[NER_example.png]]

NER utilizes two global and local features
	- **Global features** include all known information about a word/named [[entity]] (e.g. databases, dictionaries, latent models, word distributions)
	- **Local features** include the local context (usually the sentence) in which a named entity is mentioned