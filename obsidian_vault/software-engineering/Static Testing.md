## Static Testing
**Static Testing** verifies documents and specification.
- Informal documents are verified by reviews.
- Formal documents are verified by static analysis.
![[Static_testing.png]]

```mermaid
flowchart TD
SoftwareQA[Software QA]--Guidlines, Methods-->Constructive
SoftwareQA[Software QA]-->Analytical
Analytical--Program is not executed-->StaticTesting[Static Testing]
Analytical--Program is executed-->DynamicTesting[Dynamic Testing]
DynamicTesting-->DynamicTestingTools[Black-Box/White-Box Testing, Simulation, Prototyping, etc.]
StaticTesting--Tool-based-->StaticAnalysis[Static Analysis]
StaticTesting--Manual-->Review
```