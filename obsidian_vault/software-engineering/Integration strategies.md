## Integration strategies
| Name | Basic Idea | Pro | Cons |
|--------|------------|-----|-------|
|Top-Down|Starting point: Component that only uses other components, but is not used itself. Other components are replaced by dummies.|Less or no drivers needed, as highlevel components are used as a test environment.|May get expensive Low level components have to be replaced by dummies.|
|Bottom-Up|Starting point: Component that does not call other components. Larger subsystems are created step by step.|No dummies required|Requires drivers for high level components.|
|Ad-Hoc|Starting point: Components are integrated when finished.|No waiting time|Both drivers and dummies needed|
|Big Bang|Everything is put together at once| |All errors occur at once Hard to find the source of errors Time wasted until integration|

