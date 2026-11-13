# Examples, counterexamples and finite values

These examples use the [physical node-dephasing model](model.md) and measure entanglement across the graph's complete bipartite color cut. They illustrate the analytical formulas and delimit the density theorem. The [verification suite](../verification/README.md) enumerates every orientation of each listed finite graph.

## A forest loses the complete bond resource

The indegree vector of a forest determines its orientation uniquely. At a leaf, occupation zero or one fixes the only incident edge; remove it and subtract its contribution from the neighboring charge. Repeating recovers all edge directions. Every charge fiber has size one, so

```math
E_G=m-H(D)=0.
```

The resulting state is a mixture of product occupation patterns. This is complete separability of that finite resource, stronger than the vanishing-density statement for general sparse graphs.

## A single loop leaves a rare coherent sector

For an even cycle of length $`\ell`$, the two consistently directed circulations have the same all-one indegree vector. No other orientation has a partner with the same indegrees. The corresponding sector has probability $`2^{1-\ell}`$ and contains one ebit across the color cut. Hence

```math
E_{C_\ell}=2^{1-\ell}.
```

This sector is a dual-rail GHZ state at the separate vertices, so intermediate logical $`X`$ measurements can localize a Bell pair between two selected vertices. The existence of this loop protocol is consistent with, and builds on, earlier photonic loop activation; see [related work](../references/related_work.md). Its probability must remain part of the accounting.

| Cycle length | Ideal entanglement, ebits |
| --- | ---: |
| Four | 0.125 |
| Six | 0.03125 |
| Eight | 0.0078125 |

Taking longer cycles gives zero density, even though every finite cycle has a coherent sector.

## Why the short-cycle qualification is essential

Join $`r`$ vertex-disjoint four-cycles by $`r-1`$ bridges, choosing different incoming and outgoing cycle vertices so that the maximum degree is three and the graph stays bipartite. The result is connected and has $`N=4r`$ vertices.

A bridge orientation is fixed by the full charge vector. Sum the occupations on one side of the bridge: each internal edge contributes exactly one particle, and the remainder determines which side contains the bridge excitation. Removing the bridge contributions leaves the charge vectors of the component cycles. Conversely, those cycle charge vectors and bridge orientations reconstruct the full charge vector. Therefore the orientation fibers factor over the cycles, and their logarithmic sizes add. Independent bond orientations give

```math
E_G=\sum_{j=1}^{r}E_{C_4}=\frac r8=\frac N{32}.
```

This is a positive-density maximum-degree-three family. It does not satisfy local tree likeness: every vertex belongs to a four-cycle. Thus no valid reading of the [degree-three theorem](degree_three.md) may omit its local-tree assumption.

## Complete bipartite finite examples

The reference run gives:

| Graph | Vertices | Edges | Ideal entanglement, ebits |
| --- | ---: | ---: | ---: |
| Path on seven vertices | 7 | 6 | 0 |
| Two four-cycles with one bridge | 8 | 9 | 0.25 |
| $`K_{3,3}`$ | 6 | 9 | 0.902559333204 |
| $`K_{4,4}`$ | 8 | 16 | 2.896176543856 |

The last two values are floating-point evaluations of exact orientation multiplicities, not symbolic entropy evaluations. Both graphs have short cycles. In particular, positive entanglement on $`K_{3,3}`$ does not contradict zero asymptotic density for locally tree-like degree-three sequences.

The universal four-regular bound is deliberately conservative. At $`N=8`$ it gives

```math
E_G\ge8\alpha_4-I_4=0.109134638143\ldots,
```

well below the enumerated $`K_{4,4}`$ value. The lower bound certifies a nonzero density without requiring exact orientation counting; it is not a prediction of the exact finite entanglement.

## Additional edge phase errors

For a charge fiber, the coefficient matrix after independent phase errors has entries

```math
M_{xy}=2^{-m}(1-2q)^{d_H(x,y)},
\qquad D(x)=D(y),
```

where $`d_H`$ is Hamming distance. All other matrix elements vanish. These small blocks suffice to calculate $`S(\rho_{G,q})`$ without constructing the exponentially larger full endpoint-mode density matrix.

At $`q=0.001`$, the reference run finds approximately $`0.120309132304`$ ebits on the four-cycle and $`0.872304853322`$ on $`K_{3,3}`$. The [robustness theorem](robustness.md) bounds these quantities through maximally correlated distillation. They are small-state calculations, distinct from the rigorous four-regular fixed-error certificate at $`q=1/2000`$.
