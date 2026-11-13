# Related work and attribution

The contribution is a distinction in the **density of entanglement surviving complete local particle-number dephasing**. For locally tree-like bipartite graph sequences of maximum degree three, the surviving entanglement per vertex vanishes ([degree-three theorem](../science/degree_three.md)). Every connected simple four-regular bipartite graph instead satisfies an explicit linear lower bound with positive asymptotic density ([degree-four theorem](../science/degree_four.md)). Both sides can start with an extensive number of Bell links and an extensive cycle rank. The distinction concerns the ability of cycles to support coherent alternatives after dephasing, rather than the mere existence of cycles.

The bipartition is between the two complete vertex-color classes. The distillation task permits collective quantum processing within each class. Its value is an entanglement measure of the supplied state; it does not specify a protocol with only node-local quantum operations or a communication rate between distant individual vertices. The local phases are physically averaged and forgotten before that processing. Independently dephased batches are therefore distinct from repeated uses sharing one stable, unknown phase; see the [model](../science/model.md) and [interpretation](../science/interpretation.md).

## Number sectors and entanglement distillation

Local-number sectors, relational encodings, and activation of single-particle entanglement are established ideas. Wiseman and Vaccaro [WV03] give an operational number-sector treatment of shared-particle entanglement. Schuch, Verstraete, and Cirac [SVC04] develop entanglement theory under superselection rules; Bartlett, Rudolph, and Spekkens [BRS07] explain the relation to reference frames and repeated-copy activation. The present physical dephasing channel has the same charge-block structure, without requiring a restriction on all later operations.

For the all-edge coalition cut, each charge sector is a locally flagged maximally entangled state whose Schmidt rank is the number of compatible edge orientations. This yields

```math
E_D(\rho_G)=E_F(\rho_G)=H(X\mid D)=|E|-H(D).
```

The sector-entanglement principle is inherited; expressing it through graph orientation fibers makes the density question accessible. The [entropy identity](../science/entropy_identity.md) is derived directly, and the main graph theorems require additional estimates on those fibers.

The noisy extension uses another established result. Rains [R01, Theorem 6.2] evaluates the PPT-distillable entanglement of maximally correlated states. Combined with the LOCC hashing inequality of Devetak and Winter [DW05], it gives the ordinary distillable-entanglement formula used here. The [phase-error robustness bound](../science/robustness.md) applies this inherited formula to the dephased graph state. Equality with entanglement of formation is asserted for the ideal flagged-sector state, not for the phase-error extension in general.

## Close network and gauge-theory precedents

| Prior work | Established mechanism or task | Relation to the present result |
| --- | --- | --- |
| Abiuso et al. [A22] | Three independent single-photon entangled links on a triangle, measured with local beamsplitters and photodetectors, reveal network nonlocality. | A close physical predecessor for exploiting loop alternatives in single-photon networks. Loop-based access to their coherence is thus an established mechanism. The present quantity is mixed-state coalition entanglement over growing graph families, rather than triangle measurement correlations. |
| Chin, Kim, and Lee [CKL21] | A perfect-matching graph description of linear quantum networks; criteria for genuine entanglement of postselected one-particle-per-detector states and constructions of GHZ, W, and Dicke states. | Their cycle-based GHZ constructions are a direct precedent for the illustrative loop protocol. Here all charge sectors of a dephased Bell-link resource are retained and weighted, and the target is their aggregate entanglement density. |
| Bianchi, Donà, and Vilensky [BDV19] | Bell-link states projected into local SU(2)-invariant intertwiner spaces; entanglement bounds on arbitrary finite graphs in a large-spin regime. | The shared bond-and-local-symmetry structure is substantial. Their operation is a pure gauge-invariant projection, whereas the present operation is a density-matrix U(1) twirl over all local-number sectors. Their large-spin bounds do not give the bounded-degree, locally tree-like density contrast considered here. |
| Van Acoleyen et al. [VA16] | Separation of gauge-sector contributions from operationally distillable entanglement in lattice gauge theories. | Establishes the importance of distinguishing classical sector information from usable entanglement. The present state lives in the ordinary tensor product of labelled endpoint modes and undergoes actual local dephasing; it is not a claim about distillation under a gauge-theory observable algebra. |

The persistence of selected coherences under dephasing is also established more broadly. Perez-Leija et al. [PL18] study single- and two-particle hopping networks and identify surviving exchange coherences. That dynamical problem differs from a static resource with one excitation on every labelled edge and a subsequent independent phase twirl at every vertex. Survival of coherence alone is not identified here with a coalition entanglement rate.

## Classical ingredients and what they do not imply alone

The correspondence between prescribed indegrees and directed-cycle reversal classes is classical; Gioan [G07] develops this structure and its Tutte-polynomial enumerations. The relevant quantity here is the orientation-weighted average logarithm of a fiber size. Counting the number of distinct indegree sequences or cycle-reversal classes does not determine that average.

The degree-four lower bound combines the exact neighboring-charge distribution with a spanning-tree entropy bound. This is the elementary chain-rule inequality underlying dependence-tree methods such as Chow and Liu [CL68]. The degree-three upper bound uses critical branching with offspring distribution $`\mathrm{Bin}(2,1/2)`$. Its survival recursion is proved directly; critical branching theory is classical [AN72]. Neither the entropy inequality nor critical branching is claimed as a new mathematical tool.

Salez [S11] establishes cavity-method free-entropy limits for locally constrained subgraphs on locally tree-like graphs. On a bipartite graph, the orientation fibers here can be written as exact degree-constrained subgraphs. However, exact-degree indicator weights fail the positive-empty-set and strict size-increase conditions of the cavity-monotone measures used in that theorem. Applying its finite-activity result to the required exact-factor entropy would need an additional limiting argument. The proofs here use direct finite-graph bounds and do not assume such a transfer.

The resulting addition is thus the graph-wide density conclusion for this physical dephasing model, including the degree-three critical case and a degree-four lower bound uniform over connected simple bipartite graphs. The locally tree-like qualification matters: a family containing linearly many short disjoint cycles can retain an extensive amount of entanglement even at lower degree.

## References

The keys below match [references.bib](references.bib).

- **[WV03]** H. M. Wiseman and J. A. Vaccaro, *Entanglement of Indistinguishable Particles Shared between Two Parties*, Physical Review Letters **91**, 097902 (2003). [DOI](https://doi.org/10.1103/PhysRevLett.91.097902).
- **[SVC04]** N. Schuch, F. Verstraete, and J. I. Cirac, *Quantum entanglement theory in the presence of superselection rules*, Physical Review A **70**, 042310 (2004). [DOI](https://doi.org/10.1103/PhysRevA.70.042310).
- **[BRS07]** S. D. Bartlett, T. Rudolph, and R. W. Spekkens, *Reference frames, superselection rules, and quantum information*, Reviews of Modern Physics **79**, 555–609 (2007). [DOI](https://doi.org/10.1103/RevModPhys.79.555).
- **[R01]** E. M. Rains, *A semidefinite program for distillable entanglement*, IEEE Transactions on Information Theory **47**, 2921–2933 (2001). [DOI](https://doi.org/10.1109/18.959270).
- **[DW05]** I. Devetak and A. Winter, *Distillation of secret key and entanglement from quantum states*, Proceedings of the Royal Society A **461**, 207–235 (2005). [DOI](https://doi.org/10.1098/rspa.2004.1372).
- **[A22]** P. Abiuso, T. Kriváchy, E.-C. Boghiu, M.-O. Renou, A. Pozas-Kerstjens, and A. Acín, *Single-photon nonlocality in quantum networks*, Physical Review Research **4**, L012041 (2022). [DOI](https://doi.org/10.1103/PhysRevResearch.4.L012041).
- **[CKL21]** S. Chin, Y.-S. Kim, and S. Lee, *Graph picture of linear quantum networks and entanglement*, Quantum **5**, 611 (2021). [DOI](https://doi.org/10.22331/q-2021-12-23-611).
- **[BDV19]** E. Bianchi, P. Donà, and I. Vilensky, *Entanglement entropy of Bell-network states in loop quantum gravity: Analytical and numerical results*, Physical Review D **99**, 086013 (2019). [DOI](https://doi.org/10.1103/PhysRevD.99.086013).
- **[VA16]** K. Van Acoleyen, N. Bultinck, J. Haegeman, M. Marien, V. B. Scholz, and F. Verstraete, *Entanglement of Distillation for Lattice Gauge Theories*, Physical Review Letters **117**, 131602 (2016). [DOI](https://doi.org/10.1103/PhysRevLett.117.131602).
- **[PL18]** A. Perez-Leija et al., *Endurance of quantum coherence due to particle indistinguishability in noisy quantum networks*, npj Quantum Information **4**, 45 (2018). [DOI](https://doi.org/10.1038/s41534-018-0094-y).
- **[G07]** E. Gioan, *Enumerating degree sequences in digraphs and a cycle–cocycle reversing system*, European Journal of Combinatorics **28**, 1351–1366 (2007). [DOI](https://doi.org/10.1016/j.ejc.2005.11.006).
- **[CL68]** C. K. Chow and C. N. Liu, *Approximating Discrete Probability Distributions with Dependence Trees*, IEEE Transactions on Information Theory **14**, 462–467 (1968). [DOI](https://doi.org/10.1109/TIT.1968.1054142).
- **[AN72]** K. B. Athreya and P. E. Ney, *Branching Processes*, Springer (1972). [DOI](https://doi.org/10.1007/978-3-642-65371-1).
- **[S11]** J. Salez, *The cavity method for counting spanning subgraphs subject to local constraints*, arXiv:1103.3281 (2011). [arXiv](https://arxiv.org/abs/1103.3281).
