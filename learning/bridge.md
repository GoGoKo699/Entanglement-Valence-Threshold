# From phase references to entanglement on a sparse graph

The educational anchor is Stephen D. Bartlett, Terry Rudolph, and Robert W. Spekkens, *Reference frames, superselection rules, and quantum information*, Reviews of Modern Physics **79**, 555–609 (2007), specifically [arXiv:quant-ph/0610030v3](https://arxiv.org/abs/quant-ph/0610030v3). This is the version dated 10 April 2007. The [versioned PDF](https://arxiv.org/pdf/quant-ph/0610030v3) and [HTML transcription](https://arxiv.org/html/quant-ph/0610030v3) provide the same source in different layouts.

The source supplies phase averaging, charge sectors, invariant encodings, and activation. The graph-density theorems below are supplied by this project's scientific account. The [30 milestones](milestones.md) follow the same route in smaller steps.

## A precise reading map

The labels in the second column are the PDF's canonical section labels. The HTML transcription replaces subsection letters with numbers and renumbers equations continuously; for example, PDF §III.C.2 appears as HTML §III.3.2. Equation numbers below refer to the PDF.

| Purpose | PDF locator | HTML locator | Project destination |
| --- | --- | --- | --- |
| Average an unknown phase and identify number blocks | [§II.B, p. 5, Eqs. (2.7)–(2.9)](https://arxiv.org/pdf/quant-ph/0610030v3#page=5) | §II.2 | [Physical dephasing](../science/model.md#physical-local-number-dephasing) |
| Organize symmetry sectors and their degeneracies | [§II.C, pp. 6–8, Eqs. (2.14), (2.25)](https://arxiv.org/pdf/quant-ph/0610030v3#page=6) | §II.3 | [Orientation fibers](../science/entropy_identity.md#orientation-fibers) |
| Store a qubit in two modes at fixed number | [§III.A.1, p. 10, Eq. (3.1)](https://arxiv.org/pdf/quant-ph/0610030v3#page=10) | §III.1.1 | The loop encoding worked below |
| Separate operational uses of single-particle entanglement | [§III.C.1, pp. 15–16](https://arxiv.org/pdf/quant-ph/0610030v3#page=15) | §III.3.1 | [Resource and operations](../science/model.md#which-operations-and-entanglement-are-counted) |
| Understand activation and two-copy number projection | [§III.C.2, pp. 16–17, Eqs. (3.31), (3.32)](https://arxiv.org/pdf/quant-ph/0610030v3#page=16) | §III.3.2 | [Independent batches](../science/model.md#physical-local-number-dephasing) |
| Relate operational entanglement to the locally twirled state | [§III.C.3, pp. 17–18, Eq. (3.33)](https://arxiv.org/pdf/quant-ph/0610030v3#page=17) | §III.3.3 | [Exact entanglement identity](../science/entropy_identity.md#exact-identity) |

Read these sections as one chain: a phase action determines sectors; coherent information can remain within a sector; number projection can expose it; entanglement must then be evaluated under a stated operational task.

## Translate the notation before extending the argument

| Anchor notation | Graph notation | Meaning here |
| --- | --- | --- |
| $`\hat N_{\rm tot}`$ | $`N_v`$ | Total occupation of the modes at vertex $`v`$ |
| $`U(\phi)`$ | $`e^{i\theta_vN_v}`$ | One common phase acting on that vertex's modes |
| $`\Pi_n`$ | $`\Pi_{\mathbf d}`$ | A projector onto specified occupation numbers |
| $`\mathcal U`$ or $`\mathcal G`$ | $`\mathcal T_G`$ | The relevant averaging channel |
| A degeneracy within a charge sector | $`\mathcal F_{\mathbf d}`$ | Different edge orientations with the same charges |

The graph uses one independent phase for every vertex, so its symmetry is $`U(1)^V`$. Each occupied endpoint mode has only the values zero and one in the supplied resource. Consequently, all calculations take place in a finite occupation space even though the notation comes from optical modes.

For an orientation $`x`$, the phase factor is

```math
U(\boldsymbol\theta)|x\rangle_A|\bar x\rangle_B
 =e^{i\sum_v\theta_vD_v(x)}|x\rangle_A|\bar x\rangle_B.
```

A matrix element between $`x`$ and $`y`$ therefore acquires the factor

```math
\prod_{v\in V}\int_0^{2\pi}\frac{d\theta_v}{2\pi}
        e^{i\theta_v[D_v(x)-D_v(y)]}
 =\begin{cases}
  1,&D(x)=D(y),\\
  0,&D(x)\ne D(y).
 \end{cases}
```

This calculation supplies the central question: after every local occupation is fixed, how many distinct orientations remain possible?

## A reference problem and an irreversible channel are different tasks

In this project the phases are randomized and their records are lost **before** the two color coalitions cooperate. The supplied state is already $`\rho_G=\mathcal T_G(|\Psi_G\rangle\langle\Psi_G|)`$. Later access to a phase standard cannot recreate a discarded matrix element. It can still help implement gates, but that is a different resource.

The distinction is especially visible with repeated batches. Independently refreshed disturbances supply

```math
\left[\mathcal T_G(|\Psi_G\rangle\langle\Psi_G|)\right]^{\otimes n}.
```

One phase per vertex, stable across all $`n`$ preparations, instead supplies

```math
\mathcal T_G^{\rm common}
 \left[(|\Psi_G\rangle\langle\Psi_G|)^{\otimes n}\right],
```

where each phase acts on the sum of that vertex's occupations across the preparations. Equal *total* charges can then preserve alternatives that independent batch dephasing removes. This is why two-copy activation is a useful foundation but does not overturn the theorem about independently dephased graph states. The exact access and cost conventions are in the [model](../science/model.md).

## Work through every orientation of a four-cycle

Take the cycle with vertices $`1,2,3,4`$ in that order and color classes $`A=\{1,3\}`$, $`B=\{2,4\}`$. Order its edges as

```math
e_1=\{1,2\},\quad e_2=\{2,3\},\quad
 e_3=\{3,4\},\quad e_4=\{4,1\}.
```

As in the scientific model, $`x_e=1`$ places the particle at its $`A`$ endpoint. The four indegrees are therefore

```math
D(x)=\bigl(x_1+x_4,\ 2-x_1-x_2,\ x_2+x_3,\ 2-x_3-x_4\bigr).
```

The input is the equal superposition of the following sixteen orthogonal orientation terms. Each has probability $`1/16`$ in an occupation measurement.

| Orientation $`x_1x_2x_3x_4`$ | Charges $`(D_1,D_2,D_3,D_4)`$ | Fiber size |
| --- | --- | ---: |
| 0000 | (0,2,0,2) | 1 |
| 0001 | (1,2,0,1) | 1 |
| 0010 | (0,2,1,1) | 1 |
| 0011 | (1,2,1,0) | 1 |
| 0100 | (0,1,1,2) | 1 |
| **0101** | **(1,1,1,1)** | **2** |
| 0110 | (0,1,2,1) | 1 |
| 0111 | (1,1,2,0) | 1 |
| 1000 | (1,1,0,2) | 1 |
| 1001 | (2,1,0,1) | 1 |
| **1010** | **(1,1,1,1)** | **2** |
| 1011 | (2,1,1,0) | 1 |
| 1100 | (1,0,1,2) | 1 |
| 1101 | (2,0,1,1) | 1 |
| 1110 | (1,0,2,1) | 1 |
| 1111 | (2,0,2,0) | 1 |

There are fourteen singleton fibers and one two-element fiber. The latter consists of the two consistent circulations around the loop. Its probability is $`2/16=1/8`$, and its normalized conditional state is

```math
|\phi_{1111}\rangle
 =\frac{|0101\rangle_A|1010\rangle_B
              +|1010\rangle_A|0101\rangle_B}{\sqrt2}.
```

Every vertex has one particle in this sector. At each vertex, call the local two-mode pattern in the first term $`|0_L\rangle_v`$ and the pattern in the second $`|1_L\rangle_v`$. These are $`|10\rangle`$ and $`|01\rangle`$ in one order or the other, so both receive the same local phase. In this encoding the state is

```math
|\phi_{1111}\rangle
 =\frac{|0_L0_L0_L0_L\rangle
             +|1_L1_L1_L1_L\rangle}{\sqrt2}.
```

Across the complete color cut this has two equal Schmidt coefficients, hence one ebit. Each singleton fiber has a single product occupation pattern and contributes zero. Charge measurement consequently gives one encoded Bell pair with probability $`1/8`$ and zero otherwise, under the permitted coalition processing. The average is $`1/8`$ ebit per ideal batch.

The same answer follows from entropy. The charge distribution has fourteen outcomes of probability $`1/16`$ and one of probability $`1/8`$, so

```math
\begin{aligned}
H(D)&=14\left(\frac1{16}\right)4
       +\left(\frac18\right)3
       =\frac{31}{8},\\
H(X\mid D)&=4-H(D)=\frac18.
\end{aligned}
```

Thus the rare loop protocol and the all-sector calculation agree exactly. A rare favorable sector has not been counted as a deterministic Bell pair. Longer even cycles give $`E_{C_\ell}=2^{1-\ell}`$; their shrinking contribution is the first indication that a large cycle rank alone cannot decide an entanglement density. See [examples](../science/examples.md).

## From the loop to the density theorem

For a general graph, group all orientations with the same charges. Their conditional coherent state has Schmidt rank $`f_D`$, and the charge measurement is local across the color cut. The [entropy proof](../science/entropy_identity.md) keeps every outcome and establishes

```math
E_D(\rho_G)=E_F(\rho_G)
 =\mathbb E[\log_2 f_D]
 =H(X\mid D)=m-H(D).
```

This formula concerns independent copies of a fixed, already dephased graph state. It also gives the average logarithmic Schmidt rank in one batch. Integer one-batch Bell yields and their rounding loss are treated separately in the same proof.

The remaining steps are specific additions of the graph account:

| Step | Mathematical question | Where it is proved |
| --- | --- | --- |
| Identify the coherent alternatives | Which orientation changes preserve every indegree? | [Cycle decomposition](../science/degree_three.md#equal-indegrees-require-directed-cycle-changes) |
| Bound degree-three fibers | How likely is a long directed continuation in a tree neighborhood? | [Critical survival recursion](../science/degree_three.md#the-critical-survival-estimate-with-indexing) |
| Take the sparse-graph limit | How many vertices have a nontree neighborhood at each fixed radius? | [Local-tree theorem and order of limits](../science/degree_three.md#locally-tree-like-sequences) |
| Certify degree-four density | How much joint charge entropy can a spanning tree remove? | [Exact neighboring-charge distribution and entropy bound](../science/degree_four.md) |
| Add independent phase errors | What entropy is introduced before charge pinching? | [Maximally correlated distillation and the error bound](../science/robustness.md#independent-edge-phase-flips) |

At maximum degree three, the nonroot continuation has offspring law $`\operatorname{Bin}(2,1/2)`$. Its critical survival probability decays to zero. This makes the fraction of edges that can participate in coherent cycle changes vanish on locally tree-like sequences. The proof takes graph size to infinity at fixed neighborhood radius, then increases that radius.

At degree four, the project uses an exact two-vertex charge law and an entropy inequality to obtain

```math
E_D(\rho_G)\ge\alpha_4N-I_4,
\qquad
\alpha_4=0.019967671482\ldots>0.
```

This lower bound holds for every connected simple four-regular bipartite graph; its proof needs no high-girth assumption. Comparing the two results on locally tree-like graph sequences gives the valence distinction. A degree-three family with many short loops can have positive density, as the [bridged-cycle counterexample](../science/examples.md#why-the-short-cycle-qualification-is-essential) demonstrates.

For independent extra edge phase errors, the [robustness account](../science/robustness.md) establishes

```math
E_D(\rho_{G,q})\ge
 [\alpha_4-2h_2(q)]N-I_4.
```

This certifies a small, nonzero interval of constant error rates. The noisy formula uses established maximally correlated distillation theory; it does not assert equality of noisy entanglement of formation with distillable entanglement.

The anchor explains why number sectors can preserve quantum information. The project's additional graph estimates determine whether the preserved information is extensive. Primary attribution for the ingredients and close network/gauge comparisons is collected in [related work](../references/related_work.md).

Continue through the [milestones](milestones.md), or return to the [scientific route](../science/README.md).
