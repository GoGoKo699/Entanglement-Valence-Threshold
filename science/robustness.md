# Additional edge errors and supplied erasure flags

The degree-four density lower bound has a nonzero tolerance to independent edge phase errors. A separate deletion bound applies when the identity of every erased edge is supplied in a trustworthy classical record. These statements use the physical, independently refreshed node dephasing and the color-coalition access model in [the model](model.md).

Throughout, $`G`$ is a finite simple bipartite graph, $`N=|V|`$, $`m=|E|`$, and all edges cross the coalition cut. Entropies and entanglement are measured in bits. The state of each independently dephased full graph is one batch; conventional distillation uses independent copies of that mixed batch state.

## Independent edge phase flips

Before node dephasing, let each edge acquire a phase flip with probability $`q\in[0,1/2]`$, independently. It is enough to apply $`Z`$ to one endpoint occupation qubit of the edge. The one-edge state becomes

```math
\sigma_q=(1-q)|\psi^+\rangle\langle\psi^+|
             +q|\psi^-\rangle\langle\psi^-|,
\qquad
|\psi^\pm\rangle=\frac{|10\rangle\pm|01\rangle}{\sqrt2}.
```

Write $`\rho_{G,q}=\mathcal T_G(\sigma_q^{\otimes m})`$, where $`\mathcal T_G`$ is the independent node-number twirl. The edge phase flips commute with this twirl. They preserve both the uniform occupation diagonal and the classical charge distribution $`D`$.

**Proposition.** For every such bipartite graph,

```math
E_D^{\to}(\rho_{G,q})=E_D^{\leftrightarrow}(\rho_{G,q})
 =m-S(\rho_{G,q})
 \geq m-H(D)-m h_2(q),
```

where $`h_2(q)=-q\log_2q-(1-q)\log_2(1-q)`$, with the usual continuous endpoint convention. For an ideal connected four-regular graph this yields

```math
E_D(\rho_{G,q})
\geq[\alpha_4-2h_2(q)]N-I_4.
```

### Exact distillable-entanglement identity

Choose the edge occupation basis so that every input configuration is $`|x\rangle_A|\bar x\rangle_B`$, with $`x\in\{0,1\}^m`$. Diagonal phase errors and node dephasing preserve the maximally correlated form

```math
\rho_{G,q}=\sum_{x,y}c_{xy}
 |x\rangle\langle y|_A\otimes
 |\bar x\rangle\langle\bar y|_B,
\qquad c_{xx}=2^{-m}.
```

Consequently $`\rho_A=\rho_B=2^{-m}I`$ on the endpoint occupation registers. The [Devetak–Winter hashing inequality](https://arxiv.org/abs/quant-ph/0306078) gives the one-way lower bound

```math
E_D^{\to}(\rho_{G,q})\geq S(\rho_B)-S(\rho_{G,q})
 =m-S(\rho_{G,q}).
```

For the converse, use the separable state

```math
\omega_G=2^{-m}\sum_x
 |x\rangle\langle x|_A\otimes
 |\bar x\rangle\langle\bar x|_B.
```

It is proportional to the identity on the correlated support, so its quantum relative entropy satisfies

```math
E_D^{\leftrightarrow}(\rho_{G,q})
\leq E_R(\rho_{G,q})
\leq D(\rho_{G,q}\Vert\omega_G)
=m-S(\rho_{G,q}).
```

The usual relative-entropy upper bound on distillation and hashing therefore coincide. This is a specialization of established maximally-correlated-state distillation theory; see also [Rains, Theorem 6.2](https://arxiv.org/abs/quant-ph/0008047v2).

The charge sectors remain locally readable. If number-conserving implementations are required, first measure the full vertex-charge flags. Within each flagged sector, the coefficient matrix is a maximally correlated state on fixed-charge logical spaces. Hashing acts on these logical matrix algebras. Averaging their coherent informations returns $`m-S(\rho_{G,q})`$, because the Shannon entropy of the flags cancels between the marginal and joint entropies. Thus this implementation can keep the local charge values fixed. Its collective quantum processing within each coalition has no efficiency or network-routing guarantee here.

### Bounding the entropy after pinching

The two eigenstates of $`\sigma_q`$ are orthogonal, hence

```math
S(\sigma_q^{\otimes m})=m h_2(q).
```

The node twirl is the projective pinching $`\mathcal T_G(\sigma)=\sum_dP_d\sigma P_d`$. An isometry that coherently copies its charge label to a record preserves the input entropy, while the record entropy is $`H(D)`$. The Araki–Lieb inequality therefore gives

```math
S(\mathcal T_G(\sigma))\leq S(\sigma)+H(D).
```

Applying this to $`\sigma_q^{\otimes m}`$ proves the stated lower bound. This entropy-gain argument needs only the diagonal charge law; it does not assume orthogonality of the noisy states inside a sector.

### A sufficient error margin

The bound certifies positive asymptotic density whenever

```math
h_2(q)<\frac{\alpha_4}{2}.
```

Numerically, the equality occurs at $`q=0.0008586201\ldots`$. This is a sufficient threshold from the entropy estimate, not an optimal noise threshold. An elementary certified example avoids that numerical root: for $`q=1/2000`$,

```math
h_2(q)\leq q\log_2(1/q)+\frac q{\ln2}
       <\frac{11+3/2}{2000}=0.00625.
```

Here $`2000<2^{11}`$ and $`\ln2>2/3`$. Together with $`\alpha_4>0.0199`$, this gives a density lower bound strictly larger than $`0.0074`$ in the large-$`N`$ limit.

The ideal identity $`E_F=m-H(D)`$ from [the entropy calculation](entropy_identity.md) applies at $`q=0`$. The noisy calculation above establishes the distillable-entanglement identity; it makes no equality claim for noisy entanglement of formation. Since phase flips are local channels, the ideal degree-three upper bound on $`E_F`$ remains an upper bound after these additional errors.

## Externally heralded edge deletion

Suppose an external record identifies a set of deleted edges, leaving a known subgraph $`H\subseteq G`$. A surviving edge still supplies its ideal one-excitation Bell state. The record must be supplied without measuring which endpoint contains its excitation. This is a flagged erasure model: the entropy bound does not provide such a herald for unobserved particle loss.

Let $`\mathcal E(G)=m-H(D_G)`$ be the ideal entanglement across the color cut, including disconnected graphs. Deleting any one edge costs at most one ebit:

```math
0\leq\mathcal E(G)-\mathcal E(G-e)\leq1.
```

For a direct proof, embed both indegree vectors in the same vertex set and write

```math
D_G=D_{G-e}+Z_e,
```

where $`Z_e`$ is an independent fair choice of the two endpoint incidence vectors. A mixture of translations has entropy at least that of the original distribution, by concavity. Its entropy is at most the original entropy plus the one-bit mixing entropy. Hence

```math
0\leq H(D_G)-H(D_{G-e})\leq1,
```

which gives the deletion bound after subtracting the edge counts. Iterating, $`k`$ specified deletions cost at most $`k`$ ebits.

If edges are deleted independently with probability $`p`$, and $`F`$ is the supplied deletion record, the flagged average ideal entanglement satisfies

```math
E_D(\rho_{G,\mathrm{flag}})
 =\mathbb E_F\mathcal E(G-F)
 \geq\mathcal E(G)-pm.
```

The equality uses the shared classical flag: protocols can condition on it, while the ideal sector decomposition gives a matching average entanglement-of-formation upper bound.

For a connected four-regular graph,

```math
E_D(\rho_{G,\mathrm{flag}})
 \geq(\alpha_4-2p)N-I_4.
```

This is an average over supplied flags and independently dephased batches; it is not a guarantee for every deletion pattern.

## Combined flagged deletion and phase errors

Condition on the surviving subgraph $`H=G-F`$ and give its remaining edges independent phase-flip probability $`q`$. The preceding arguments imply

```math
\begin{aligned}
E_D(\rho_{G,p,q,\mathrm{flag}})
&\geq\mathbb E_F\mathcal E(H)
      -\mathbb E_F|E(H)|\,h_2(q)\\
&\geq\mathcal E(G)-pm-(1-p)m h_2(q).
\end{aligned}
```

For an ideal connected four-regular parent graph, a sufficient positive-density region is therefore

```math
\alpha_4-2p-2(1-p)h_2(q)>0.
```

The edge flags, one excitation per supplied bond, and collective within-coalition processing remain explicit resources. The statement does not establish the cost of producing the flags, correcting unknown particle loss, or implementing the distillation in a spatial network.
