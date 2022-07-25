## Relation Extraction
Relation extraction is the task of extracting known relations between [[entity|entities]] in a sentence
RE methods are based on machine learning by understanding RE as a **classification** problem
- Given a sentence and entity mentions, classify the relation between these entities in the sentence
| Sentence  | Relation |
| ----------------  | ----------------- |
| <a>Steve Jobs</a> and Wozniak co-founded <a>Apple</a> in 1976. | *Founder* |
| <a>Michael Jordan</a> is an American retired professional <a>basketball player</a>. | *Career* |
| <a>Washington D.C.</a> is the capital of <a>United States. </a>                  | *CapitalOf* |
Nowadays, RE is performed by neural architectures or language models (BERT, BioBERT)
**Distant-supervised** relation extraction
- No labeled sentences are required as training data
- A ground truth of correct facts is enough
- The system will generate noise training data
	- See Snorkel for a good implementation
**Zero-shot** relation extraction
- **Trained systems** can be used to classify a new relation without relying on additional training data for it
- It’s questionable how well and far these systems can be transferred

Relation extraction targets binary relations, but
- N-ary relations might be beneficial to **keep** the **original information** and **don’t loose** the **connection** (e.g. who wins a price at which date)