## Entity Linking
Entity linking (EL) requires that a **pre-known set** of **[[Entity|entities]]** is **given** (e.g. knowledge base)
- Also known as Named Entity Disambiguation (NED)
Example: [[Wikidata]]

Naïve solution are **dictionary**-based **lookups**
- Test if words in a text appear in an entity dictionary
- All synonyms have to be in that dictionary
- **Fails** if words have several meanings (**homonyms**)

Advanced approaches for entity linking are
- Mention-entity popularity
	- Consider popular entities first
- Mention-entity context similarity
	- Consider the textual context (e.g. words)
- Entity-entity coherence similarity
	- Consider known relationships between entities

### Improving Entity Linking
Entity linking can be improved by utilizing Coreference Resolution (CR):
- Coreference resolution resolves terms in texts that refer to the same meaning (e.g. “he” to ”Einstein”)
- Frequent examples are pronouns (he, she, it), short names (Einstein instead of Albert Einstein), common abbreviations (Apple instead of Apple Inc.)
Coreference Resolution is still challenging in [[NLP]]
![[Coreference_resolution_example.png]]
### Combining NER and EL
Another approach is to combine NER and EL
- [Named entity recognition](NER) detects relevant entity mentions and then, EL links only the detected mentions against KBs
- Advantages: 
	- Reduces the linking complexity
	- NER yields entity types which improve EL quality