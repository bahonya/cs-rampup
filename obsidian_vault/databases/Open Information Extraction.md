## Open Information Extraction
Open information extraction (Open IE) does not require pre-known relations and [[entity|entities]]
- It extracts statement **based on the grammatical structure** of sentences, i.e., it automatically detects relevant noun and verb phrases

Open IE systems are usually precision-oriented
- Relationships expressed in complex sentences (long sentences with several clauses) are not extracted
Open IE extractions are not canonicalized
- Several noun phrases and verb phrases might have the same meaning (e.g., has birthplace, is born)
Open IE might extract complex arguments
- (Einstein, won, the Nobel Price in 1921)

### Open IE Tools
- Rule-based systems like Stanford CoreNLP
	- Fast, reliable and well-documented – https://stanfordnlp.github.io/CoreNLP/
- Systems that utilize neural architectures:
	- Offer a higher extraction quality
	- Often require much computation power (GPU)
	- The latest best-performing system is OpenIE6 https://www.aclweb.org/anthology/2020.emnlp-main.306/