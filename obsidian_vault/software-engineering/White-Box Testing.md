## White-Box Testing
**Fundamental Idea**: Structure-based test approach 

**Particularities:**
- Information about internal structures or source code is known
- Test cases are generated mainly from source code or models 
- Idea: Coverage of structural elements 
- important for [[unit test]] phase

**Types of coverage**
- <a>Statement coverage</a>: $C_0$ - Percentage of executed instructions. Each statement (numbered line) of the program is executed at least once. Benefit:
	- Reveals unreachable statements in code
	- Easy to reach
	**Metric**:
	$C_0 = \dfrac{\text{Number of executed statements}}{\text{Total no. of statements}}*100$
- <a>Branch coverage</a>: $C_1$ - Percentage of statements and branches executed. 
	- Each decision (including loops) is executed using all possibilities
	- Branch coverage aims to traverse all transitions (branches) at least once
	- Includes “empty” transitions, which bypass statements
	Benefit:
	- Reveals unreachable branches
	- A well chosen functional test usually already achieves a high coverage!
	**Metric**:
	$C_1 = \dfrac{\text{Number of traversed branches}}{\text{Total number of branches}}*100$
- <a>Path coverage</a>: $C_2$ - Percentage of executed program flow paths. Dynamic control-flow based test design approach, which demands, that every path is traversed at least once.
	Benefit::
	- Theoretically optimal test procedure
	- Cyclic control-flow graphs (loops) with potentially infinite number of paths
	- Often unreachable in practice, rather used as theoretical comparative measure
	- More practical variant: Boundary Interior Coverage: Each loop in a test case is not executed, executed exactly once, executed several times (e.g. 2 times)
