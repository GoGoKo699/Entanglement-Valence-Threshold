# Thirty milestones through the valence threshold

These are project-defined understanding targets. **M01–M14** build the background/preliminaries; **M15–M30** connect the narrative/innovation. Each phase moves from individual objects and mechanisms toward an integrated account. The 14/16 allocation gives the operational model and the sparse-graph tools enough space before following the graph-wide argument. It does not subdivide every proof step or cover every neighboring subject.

The sole educational anchor is [Bartlett–Rudolph–Spekkens (BRS), arXiv:quant-ph/0610030v3](https://arxiv.org/abs/quant-ph/0610030v3), the 2007 review selected in the [learning overview](README.md). BRS section labels below follow its PDF/journal version. In the converted [HTML](https://arxiv.org/html/quant-ph/0610030v3), §II.B becomes §II.2, §II.C becomes §II.3, §III.A.1 becomes §III.1.1, and §§III.C.1–3 become §§III.3.1–3.3. The [bridge](bridge.md) gives the connected reading path. A project source pointer identifies the actual statement or derivation used by a milestone.

## Background/preliminaries M01–M14

### M01 Modes and particles

- **Phase:** Background/preliminaries.
- **Central question:** What are the distinct physical subsystems when one particle is distributed between two laboratories?
- **Understanding target:** Explain occupation states of labeled endpoint modes and distinguish mode labels from labels assigned to identical particles.
- **Dependencies and story role:** Entry point; establishes the objects carried by one edge before forming a network.
- **Conceptual connection:** The tensor product belongs to endpoint modes, so one excitation can occupy a coherent superposition of two spatial locations.
- **Source pointers:** [Model: Graph, modes and supplied links](../science/model.md#graph-modes-and-supplied-links); BRS §II.B (HTML §II.2) and §III.C.1 (HTML §III.3.1).

### M02 One bond and the color cut

- **Phase:** Background/preliminaries.
- **Central question:** Across which partition is an edge Bell state entangled?
- **Understanding target:** Identify the two endpoint occupation registers, the complementary basis strings and the natural bipartite color cut.
- **Dependencies and story role:** M01; combines single-edge subsystems into the partition used throughout the entanglement calculation.
- **Conceptual connection:** One endpoint of every edge lies in each color coalition, making a full edge configuration distinguishable on both sides.
- **Source pointers:** [Model: Graph, modes and supplied links](../science/model.md#graph-modes-and-supplied-links); BRS §III.C.1.

### M03 A phase shared by incident modes

- **Phase:** Background/preliminaries.
- **Central question:** How does one laboratory's phase act when it holds several edge modes?
- **Understanding target:** Read $`N_v=\sum_{e\ni v}n_{v,e}`$ as a total local number and explain why one phase rotates every incident mode together.
- **Dependencies and story role:** M01–M02; introduces the local physical disturbance whose effect must be tracked globally.
- **Conceptual connection:** A common phase distinguishes total-number sectors while leaving relative mode patterns within a sector available.
- **Source pointers:** [Model: Physical local number dephasing](../science/model.md#physical-local-number-dephasing); BRS §II.B, especially the multimode total-number representation.

### M04 Twirling as charge pinching

- **Phase:** Background/preliminaries.
- **Central question:** Which coherences survive averaging an unknown phase over a full turn?
- **Understanding target:** Explain the equivalence between the local phase integral and projection onto total-number blocks, including the independence of phases at different vertices.
- **Dependencies and story role:** M03; turns a physical disturbance into a tractable quantum channel.
- **Conceptual connection:** Group averaging selects equal-charge matrix elements, providing the bridge from phase noise to the classical charge record.
- **Source pointers:** [Model: Physical local number dephasing](../science/model.md#physical-local-number-dephasing); BRS §II.B, PDF Eqs. (2.7)–(2.9), and §II.C (HTML §II.3).

### M05 Physical noise and missing references

- **Phase:** Background/preliminaries.
- **Central question:** When does a twirled description represent irreversible noise rather than a change in available reference information?
- **Understanding target:** State why this project applies an actual dephasing channel before recovery and discards its phase record.
- **Dependencies and story role:** M04; fixes the physical interpretation before discussing any recovery operation.
- **Conceptual connection:** The mathematical twirl comes from the reference-frame framework, while the resource here is a specified mixed state after a physical channel.
- **Source pointers:** [Model: Physical local number dephasing](../science/model.md#physical-local-number-dephasing); [Interpretation: Recovery operations and batch order](../science/interpretation.md#recovery-operations-and-batch-order); BRS §§II.B–II.C.

### M06 Fixed-charge logical information

- **Phase:** Background/preliminaries.
- **Central question:** How can a laboratory manipulate a qubit without coherence between different total particle numbers?
- **Understanding target:** Describe a dual-rail or more general fixed-number encoding and the operations acting within its logical subspace.
- **Dependencies and story role:** M03–M05; identifies what remains controllable after charge dephasing.
- **Conceptual connection:** The invariant subspace stores information in relative occupation patterns rather than in superpositions of different local totals.
- **Source pointers:** [Model: Which operations and entanglement are counted?](../science/model.md#which-operations-and-entanglement-are-counted); BRS §III.A.1 (HTML §III.1.1), PDF Eq. (3.1), and §II.C.

### M07 Laboratories and coalitions

- **Phase:** Background/preliminaries.
- **Central question:** What operations are allowed when entanglement is measured across the complete color cut?
- **Understanding target:** Distinguish separate vertex operations from collective quantum processing inside each color coalition, and state which model the distillation claim uses.
- **Dependencies and story role:** M02 and M06; makes the operational meaning of the eventual rate explicit.
- **Conceptual connection:** Entanglement depends on the chosen partition and its local operations; conserving charge does not by itself make a gate spatially local.
- **Source pointers:** [Model: Which operations and entanglement are counted?](../science/model.md#which-operations-and-entanglement-are-counted); BRS §III.C.3 (HTML §III.3.3) for operational entanglement quantification.

### M08 Orientation uncertainty and entropy

- **Phase:** Background/preliminaries.
- **Central question:** How can a collection of independent edge choices be described as a classical information source?
- **Understanding target:** Interpret a fair edge orientation, its vertex indegrees, Shannon entropy and conditional uncertainty after the charge vector is known.
- **Dependencies and story role:** M01–M04; introduces the classical objects that will encode the quantum calculation.
- **Conceptual connection:** A particle's occupied endpoint becomes the head of an edge, and local particle number becomes indegree.
- **Source pointers:** [Model: Orientations and charges](../science/model.md#orientations-and-charges); [Entropy identity: Orientation fibers](../science/entropy_identity.md#orientation-fibers).

### M09 Sector flags and pure-state entanglement

- **Phase:** Background/preliminaries.
- **Central question:** What does measuring a locally readable charge label reveal without destroying the conditional resource?
- **Understanding target:** Explain a flagged ensemble, a pure state's Schmidt rank, and the distinction between entanglement of formation and distillable entanglement.
- **Dependencies and story role:** M06–M08; prepares the operational calculation for one charge sector and then its average.
- **Conceptual connection:** Measuring the sector identifies which encoded entangled state is present while preserving coherence inside that sector.
- **Source pointers:** [Entropy identity: Orientation fibers](../science/entropy_identity.md#orientation-fibers) and [Exact identity](../science/entropy_identity.md#exact-identity); BRS §III.C.3, PDF Eq. (3.33).

### M10 Independent batches and repeated use

- **Phase:** Background/preliminaries.
- **Central question:** Why does repeating a physical dephasing channel differ from using one stable unknown phase for several inputs?
- **Understanding target:** Distinguish independent copies of the dephased state from a collective twirl of many undephased copies, and explain why their activation properties can differ.
- **Dependencies and story role:** M04–M05 and M09; fixes the repeated-resource convention before using an asymptotic entanglement rate.
- **Conceptual connection:** Correlations in a hidden phase can preserve cross-copy coherences that independent physical dephasing removes.
- **Source pointers:** [Model: Physical local number dephasing](../science/model.md#physical-local-number-dephasing); [Interpretation: Recovery operations and batch order](../science/interpretation.md#recovery-operations-and-batch-order); BRS §III.C.2 (HTML §III.3.2), including the two-copy projection in PDF Eq. (3.32).

### M11 Graph degree and local tree likeness

- **Phase:** Background/preliminaries.
- **Central question:** What does a sparse graph look like near one vertex, and how can long loops remain globally abundant?
- **Understanding target:** Distinguish degree, connectedness, girth, an induced radius ball and the fraction of vertices with a non-tree ball.
- **Dependencies and story role:** M08; supplies the graph language needed for a density statement across a family of networks.
- **Conceptual connection:** Local tree likeness constrains nearby path branching without requiring the full graph to be a tree.
- **Source pointers:** [Degree three: A finite-graph local-tree bound](../science/degree_three.md#a-finite-graph-local-tree-bound), [Locally tree-like sequences](../science/degree_three.md#locally-tree-like-sequences) and [High girth as a concrete sufficient condition](../science/degree_three.md#high-girth-as-a-concrete-sufficient-condition).

### M12 Correlated records and a tree entropy bound

- **Phase:** Background/preliminaries.
- **Central question:** Why can the entropy of a full environmental record be smaller than the sum of its local entropies?
- **Understanding target:** Explain mutual information and the spanning-tree entropy inequality as a consequence of the chain rule and conditioning.
- **Dependencies and story role:** M08 and M11; introduces the record-correlation tool that will make degree four sufficient.
- **Conceptual connection:** Adjacent laboratories share an edge, so their occupation records cannot be treated as independent even when edge orientations are independent.
- **Source pointers:** [Degree four: A spanning-tree entropy inequality](../science/degree_four.md#a-spanning-tree-entropy-inequality); [Interpretation: Why correlations in the environmental record matter](../science/interpretation.md#why-correlations-in-the-environmental-record-matter).

### M13 Directed exploration and critical branching

- **Phase:** Background/preliminaries.
- **Central question:** How does a fair random orientation turn local graph degree into a path-survival problem?
- **Understanding target:** Explain fresh candidate edges, forward-edge probability and why a degree-three nonroot vertex has mean one forward child.
- **Dependencies and story role:** M08 and M11; prepares the probabilistic mechanism behind the degree-three upper bound.
- **Conceptual connection:** The graph's local coordination determines whether directed alternatives can sustain themselves as the exploration radius grows.
- **Source pointers:** [Degree three: The critical survival estimate, with indexing](../science/degree_three.md#the-critical-survival-estimate-with-indexing).

### M14 Integrating the prerequisite framework

- **Phase:** Background/preliminaries.
- **Central question:** How do modes, local phases, charge sectors, coalitions and graph probability describe one consistent resource problem?
- **Understanding target:** Trace a supplied edge state through physical local dephasing to a fixed-charge encoded resource, while keeping the cut, batch convention and charged inputs explicit.
- **Dependencies and story role:** M01–M13; integrates the phase before the graph-specific proof begins.
- **Conceptual connection:** The reference-frame foundation identifies the surviving quantum subspaces; orientation entropy and local graph structure will quantify their size.
- **Source pointers:** [Model](../science/model.md), [Science overview](../science/README.md) and [Anchor bridge](bridge.md); BRS §§II.B–II.C, III.A.1 and III.C.1–III.C.3.

## Narrative/innovation M15–M30

### M15 Deriving the orientation-charge dictionary

- **Phase:** Narrative/innovation.
- **Central question:** Which exact particle configurations correspond to an orientation, and which phase factors distinguish them?
- **Understanding target:** Derive the complementary color-side basis strings and verify that equal local charges are exactly the condition for an off-diagonal term to survive the twirl.
- **Dependencies and story role:** M04, M08 and M14; begins the argument with one matrix element and one charge vector.
- **Conceptual connection:** The quantum channel becomes a constraint on pairs of classical orientations.
- **Source pointers:** [Model: Orientations and charges](../science/model.md#orientations-and-charges), [Entropy identity: Orientation fibers](../science/entropy_identity.md#orientation-fibers) and [Bridge: every orientation of a four-cycle](bridge.md#work-through-every-orientation-of-a-four-cycle); BRS §§II.B–II.C for the twirling foundation.

### M16 A fiber becomes a maximally entangled sector

- **Phase:** Narrative/innovation.
- **Central question:** Why does one same-charge fiber have a flat Schmidt spectrum across the color cut?
- **Understanding target:** Explain its size $`f_{\mathbf d}`$, probability $`f_{\mathbf d}/2^m`$ and orthogonality of distinct orientation labels on both sides.
- **Dependencies and story role:** M09 and M15; identifies the elementary entanglement resource inside a single outcome sector.
- **Conceptual connection:** The combinatorial multiplicity of one charge record becomes the Schmidt rank of its conditional quantum state.
- **Source pointers:** [Entropy identity: Orientation fibers](../science/entropy_identity.md#orientation-fibers); BRS §III.C.3 for sector-based operational quantification.

### M17 The exact entropy identity

- **Phase:** Narrative/innovation.
- **Central question:** Why is the total surviving ideal entanglement exactly $`m-H(D)`$?
- **Understanding target:** Connect conditional orientation entropy, average logarithmic fiber size, locally flagged entanglement of formation and distillation of independent batches.
- **Dependencies and story role:** M10 and M16; assembles the central reduction used by both degree estimates.
- **Conceptual connection:** The environmental charge record removes precisely the part of the initial orientation information quantified by its entropy.
- **Source pointers:** [Entropy identity: Exact identity, Theorem 1](../science/entropy_identity.md#exact-identity); BRS §§III.C.2–III.C.3 for the imported distillation and quantification framework.

### M18 Integer Bell output from one batch

- **Phase:** Narrative/innovation.
- **Central question:** What exact integer resource can be extracted from a sector with non-power-of-two Schmidt rank?
- **Understanding target:** Explain the deterministic flat-rank conversion to $`\lfloor\log_2f_D\rfloor`$ Bell pairs and distinguish its expected yield from a fixed high-probability yield.
- **Dependencies and story role:** M07, M16 and M17; gives operational content to the entropy without hiding rounding or compilation costs.
- **Conceptual connection:** The asymptotic entropy rate has a one-batch encoded counterpart within one ebit of its expectation.
- **Source pointers:** [Entropy identity: Integer Bell yield from one batch](../science/entropy_identity.md#integer-bell-yield-from-one-batch); [Interpretation: Recovery operations and batch order](../science/interpretation.md#recovery-operations-and-batch-order).

### M19 Equal charges force cycle reversals

- **Phase:** Narrative/innovation.
- **Central question:** What can change between two orientations that produce the same charge vector?
- **Understanding target:** Reconstruct the balanced changed-edge subgraph, its directed-cycle decomposition and the bound on fiber size by the number of cycle-bearing edges.
- **Dependencies and story role:** M11, M15 and M17; identifies the local combinatorial mechanism that limits surviving coherence.
- **Conceptual connection:** Equal quantum charges impose a flow-balance condition on classical orientation differences.
- **Source pointers:** [Degree three: Equal indegrees require directed-cycle changes](../science/degree_three.md#equal-indegrees-require-directed-cycle-changes).

### M20 Forests and isolated loops

- **Phase:** Narrative/innovation.
- **Central question:** What do forests and single loops reveal about charge-fiber entanglement?
- **Understanding target:** Explain unique orientation reconstruction on a forest and the rare two-orientation GHZ sector on an even cycle, including its full probability.
- **Dependencies and story role:** M16–M19; checks the mechanism on complete examples before bounding large graph families.
- **Conceptual connection:** Loop activation produces a resource in a finite graph, while its probability can still vanish rapidly with loop length.
- **Source pointers:** [Examples: A forest loses the complete bond resource](../science/examples.md#a-forest-loses-the-complete-bond-resource), [A single loop leaves a rare coherent sector](../science/examples.md#a-single-loop-leaves-a-rare-coherent-sector) and [Bridge: the complete four-cycle](bridge.md#work-through-every-orientation-of-a-four-cycle); BRS §III.C.2 for the earlier activation foundation.

### M21 The critical directed-path bound

- **Phase:** Narrative/innovation.
- **Central question:** Why does degree three make long directed alternatives increasingly unlikely near a tree-like vertex?
- **Understanding target:** Follow the survival recurrence from $`q_0=1`$, establish its inverse-radius bound and account for the root's three candidate edges.
- **Dependencies and story role:** M13 and M19; turns the cycle constraint into a quantitative probability estimate.
- **Conceptual connection:** A critical branching process controls how often a vertex can participate in a coherent cycle alternative.
- **Source pointers:** [Degree three: The critical survival estimate, with indexing](../science/degree_three.md#the-critical-survival-estimate-with-indexing).

### M22 A finite local-tree entropy bound

- **Phase:** Narrative/innovation.
- **Central question:** How does a local path-survival estimate control the entanglement of a full finite graph?
- **Understanding target:** Combine the directed-cycle edge count, the good-vertex survival bound and the number $`b_L(G)`$ of bad radius balls into Theorem 2.
- **Dependencies and story role:** M17, M19 and M21; passes from a single neighborhood to the whole resource.
- **Conceptual connection:** Exceptional non-tree neighborhoods have an explicit cost, while the remaining vertices contribute a controlled radius-dependent term.
- **Source pointers:** [Degree three: A finite-graph local-tree bound, Theorem 2](../science/degree_three.md#a-finite-graph-local-tree-bound).

### M23 Zero density and the necessary local-tree condition

- **Phase:** Narrative/innovation.
- **Central question:** Under which order of limits does degree-three density vanish, and why is the graph-family assumption essential?
- **Understanding target:** Take graph size first at fixed radius, then increase the radius; connect high girth to that condition and explain the positive-density chain-of-squares counterexample.
- **Dependencies and story role:** M11, M20 and M22; completes the degree-three side and its scope.
- **Conceptual connection:** A local structural condition supports a global asymptotic conclusion, while persistent short loops can change it.
- **Source pointers:** [Degree three: Locally tree-like sequences, Corollary 2.1](../science/degree_three.md#locally-tree-like-sequences), [High girth as a concrete sufficient condition](../science/degree_three.md#high-girth-as-a-concrete-sufficient-condition) and [Examples: Why the short-cycle qualification is essential](../science/examples.md#why-the-short-cycle-qualification-is-essential).

### M24 The neighboring charge distribution at degree four

- **Phase:** Narrative/innovation.
- **Central question:** What information do two adjacent four-valent charge records share?
- **Understanding target:** Derive the binomial marginal and the joint distribution from one complementary shared-edge bit plus independent contributions from the other edges.
- **Dependencies and story role:** M08, M12 and M17; starts the lower-bound mechanism from one vertex pair.
- **Conceptual connection:** Independent bonds generate dependent local environmental records through their shared endpoint constraint.
- **Source pointers:** [Degree four: Exact vertex and adjacent-pair entropies](../science/degree_four.md#exact-vertex-and-adjacent-pair-entropies).

### M25 The spanning-tree correction makes four sufficient

- **Phase:** Narrative/innovation.
- **Central question:** Why does retaining adjacent-charge mutual information prove a positive density when separate charge entropies do not?
- **Understanding target:** Insert the actual pair mutual information in the tree entropy inequality, use the four-regular edge count and explain the positive coefficient $`\alpha_4`$ and finite correction.
- **Dependencies and story role:** M12, M17 and M24; completes the degree-four lower bound without exact global orientation counting.
- **Conceptual connection:** Correlations reduce the entropy of the environmental record enough to leave an extensive coherent resource.
- **Source pointers:** [Degree four: The lower bound](../science/degree_four.md#the-lower-bound) and [Completing the proof](../science/degree_four.md#completing-the-proof).

### M26 Integrating the valence comparison

- **Phase:** Narrative/innovation.
- **Central question:** What changes between locally tree-like degree-three and degree-four graph families?
- **Understanding target:** State both density conclusions with their assumptions, distinguish directed alternatives from undirected cycle rank and retain the different input bond counts.
- **Dependencies and story role:** M18, M23 and M25; integrates the ideal mechanism before adding errors.
- **Conceptual connection:** The transition concerns a surviving amount proportional to graph size, even when both families start with extensive entanglement and many undirected loops.
- **Source pointers:** [Interpretation: Survival of an amount, rather than existence of a loop](../science/interpretation.md#survival-of-an-amount-rather-than-existence-of-a-loop) and [Degree four: What this establishes](../science/degree_four.md#what-this-establishes).

### M27 Phase noise and maximally correlated distillation

- **Phase:** Narrative/innovation.
- **Central question:** Which part of the exact entanglement calculation survives independent edge phase errors?
- **Understanding target:** Identify the maximally correlated state, its uniform marginal and the matching hashing lower bound and separable-state relative-entropy upper bound.
- **Dependencies and story role:** M07, M09, M17 and M26; extends the operational calculation to a noisy mixed sector.
- **Conceptual connection:** The preserved orientation basis allows an exact noisy distillable-entanglement expression while ideal entanglement-of-formation equality has a narrower scope.
- **Source pointers:** [Robustness: Exact distillable-entanglement identity](../science/robustness.md#exact-distillable-entanglement-identity); BRS §§III.C.2–III.C.3 for the distillation framework; the project source identifies the required primary coding theorem.

### M28 A conservative nonzero phase-error margin

- **Phase:** Narrative/innovation.
- **Central question:** How can entropy growth bound the damage from edge phase errors without solving every noisy charge block?
- **Understanding target:** Explain the pinching entropy-gain bound, the binary-entropy cost per edge and the sufficient degree-four positivity condition.
- **Dependencies and story role:** M04, M25 and M27; converts exact structure into a usable analytical robustness certificate.
- **Conceptual connection:** The local charge law remains unchanged, while the independent phase-error entropy consumes part of the ideal surviving margin.
- **Source pointers:** [Robustness: Bounding the entropy after pinching](../science/robustness.md#bounding-the-entropy-after-pinching) and [A sufficient error margin](../science/robustness.md#a-sufficient-error-margin).

### M29 Supplied deletion flags and combined errors

- **Phase:** Narrative/innovation.
- **Central question:** What does a known whole-edge erasure cost, and what information must its flag supply?
- **Understanding target:** Derive the at-most-one-ebit deletion bound, average over supplied graph flags and distinguish that model from unobserved photon loss; combine deletion and phase costs.
- **Dependencies and story role:** M08, M17 and M28; completes the robustness account with its required classical resource.
- **Conceptual connection:** Deleting one fair orientation bit changes the charge-record entropy by at most one bit, producing a graph-wide damage bound with explicit flag assumptions.
- **Source pointers:** [Robustness: Externally heralded edge deletion](../science/robustness.md#externally-heralded-edge-deletion) and [Combined flagged deletion and phase errors](../science/robustness.md#combined-flagged-deletion-and-phase-errors).

### M30 The complete scoped physical conclusion

- **Phase:** Narrative/innovation.
- **Central question:** What does the surviving-entanglement density law establish once the state, operations, limits and errors are all stated together?
- **Understanding target:** Give a connected account of independent physical node dephasing, the charge-fiber identity, the degree boundary, conservative error margins, coalition recovery and unpriced implementation costs.
- **Dependencies and story role:** M14–M29; integrates the full narrative and reconciles it with the original physical question.
- **Conceptual connection:** A local symmetry-selected subspace structure becomes a global entanglement-density law through orientation ambiguity and record correlations, with every interpretation tied to the actual resource model.
- **Source pointers:** [Science overview](../science/README.md), [Interpretation](../science/interpretation.md), [Model: Which operations and entanglement are counted?](../science/model.md#which-operations-and-entanglement-are-counted) and [Related work](../references/related_work.md); BRS §§II.B–II.C and III.C.1–III.C.3 provide the foundation summarized in the [bridge](bridge.md).

Return to the [learning overview](README.md) or the [scientific account](../science/README.md).
