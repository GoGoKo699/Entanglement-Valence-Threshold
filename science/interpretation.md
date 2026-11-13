# What the valence threshold means

The resource is a collection of entangled bonds before physical phase noise. Every node has several labeled endpoint modes; one forgotten phase acts on all of them. States with the same total occupation at each node remain coherent. The graph determines how many distinct bond configurations can share those occupations.

## Survival of an amount, rather than existence of a loop

A forest has no surviving entanglement: its vertex occupations determine every edge orientation. A single even cycle has a two-configuration coherent sector, but that sector occurs with probability $`2^{1-\ell}`$ for cycle length $`\ell`$. Long loops can therefore leave a very small resource even when they provide a positive-probability activation mechanism.

The main distinction concerns an amount proportional to the number of nodes. For a connected three-regular graph, the undirected cycle-space dimension is

```math
m-N+1=\frac N2+1.
```

It is extensive. Nevertheless, when the family is locally tree-like, its surviving entanglement satisfies $`E_G/N\to0`$. The directed alternatives selected by independent edge orientations are too sparse at critical branching. Extensive undirected cycle rank therefore does not by itself protect extensive entanglement.

Connected four-regular bipartite graphs instead satisfy

```math
\liminf_{N\to\infty}\frac{E_G}{N}\ge\alpha_4,
\qquad \alpha_4=0.019967671482\ldots>0.
```

This holds even for locally tree-like sequences. It gives an integer coordination boundary between vanishing and nonvanishing density in this graph class. It is not a statement about a continuously tuned critical exponent or a universal transition on ordinary lattices with a fixed density of short cycles.

Both regular families begin with extensive ideal bond entanglement, but their resource counts differ: three-regular graphs have $`3N/2`$ bonds and four-regular graphs have $`2N`$. No equal-edge-count comparison is asserted.

## Why correlations in the environmental record matter

The inaccessible environment effectively receives the vector of vertex occupations $`D`$. The initial orientation label contains $`m`$ fair bits; the surviving ideal entanglement is the uncertainty $`m-H(D)`$ left after that record.

Adding the separate entropies of vertex charges is too coarse to prove the four-link result: $`H(\mathrm{Bin}(4,1/2))>2`$. Neighboring charges are correlated because they share one edge, which contributes to exactly one endpoint. The spanning-tree mutual-information correction lowers the record-entropy bound enough to prove positive density. At degree five and above, a simpler marginal-entropy estimate can already be informative; reaching four is the relevant boundary here.

## Recovery operations and batch order

The entanglement cut groups all vertices of one color into one party. Quantum processing within either group is allowed. In the ideal case, locally reading the charge sectors gives a maximally entangled state of random rank $`f_D`$. One batch has an expected integer encoded Bell yield between $`E_G-1`$ and $`E_G`$. This is an expected yield, with every sector retained. A high-probability fixed yield from each growing graph is not established.

The construction may need complicated joint gates, many classical outcome bits and a costly description of the charge fiber. An extensive extraction protocol with only separate vertex operations is not provided. These costs are part of a different network implementation task.

For each finite graph, $`E_D`$ is the usual asymptotic distillation rate of independent copies of its already physically dephased state. Only then is graph size varied to discuss density. On the degree-three side, the proof first takes graph size to infinity at a fixed neighborhood radius and then increases that radius. Neither limit authorizes sharing one stable hidden phase across undephased input copies.

## Which errors preserve the conclusion?

The [robustness bound](robustness.md) gives a conservative nonzero margin against additional independent bond phase flips. At $`q=1/2000`$, the four-link asymptotic density remains strictly above $`0.0074`$. This is a sufficient analytical certificate, not an optimized experimental tolerance.

An externally supplied flag identifying deleted whole bonds permits a separate average loss bound. Generic unobserved photon loss need not provide that flag without revealing the occupied endpoint; the proof does not supply such a detector.

The vertex-shared structure of the original dephasing remains essential. Fresh independent random phases for individual endpoint modes erase all occupation-basis off-diagonals and leave a separable mixture. A phase reference arriving after irreversible dephasing does not restore a discarded environmental record.

The result is a structural law for surviving quantum entanglement in a specified noisy resource. It supplies neither a communication speedup nor an implementation-cost advantage by itself.
