# A connected account of surviving bond entanglement

The physical question is whether increasing network coordination can change an extensive entanglement resource into one that survives complete local particle-number dephasing. Every link begins as an independently supplied single-excitation Bell state. The same random phase acts on all modes at one vertex, independently at different vertices, and the phase records are lost.

The account proceeds from this channel to an exact entropy identity and then to two graph bounds. It measures entanglement across the whole bipartite color cut, with collective quantum processing inside each color class.

1. [Model and resources](model.md) fixes the mode tensor product, physical noise, independent batches and coalition operations.
2. [Charge-sector entropy](entropy_identity.md) derives $`E_D=E_F=m-H(D)`$, where $`D`$ is the indegree vector of a random edge orientation. It also gives the expected integer Bell yield from one ideal batch.
3. [Degree three](degree_three.md) shows that equal-indegree alternatives require directed cycles. Critical branching bounds their abundance and gives zero density on locally tree-like maximum-degree-three sequences.
4. [Degree four](degree_four.md) uses adjacent-charge mutual information in a spanning-tree entropy inequality. Every connected simple four-regular bipartite graph has $`E_D\ge\alpha_4N-I_4`$, with $`\alpha_4>0.0199`$.
5. [Robustness](robustness.md) treats independent edge phase errors and externally supplied whole-edge deletion flags. It distinguishes exact identities from sufficient error margins.
6. [Examples](examples.md) checks trees, cycles, short-cycle counterexamples and finite complete bipartite graphs.
7. [Interpretation](interpretation.md) reconciles the density threshold, limiting order and allowed recovery operations.

The [related-work account](../references/related_work.md) credits sector entanglement, loop activation, maximally correlated distillation, graph cycle reversal, entropy inequalities and critical branching. The proposed addition is their graph-wide density consequence for the specified physical channel. The [verification guide](../verification/README.md) gives reproducible checks and their limits.
