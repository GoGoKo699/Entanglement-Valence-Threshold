# The resource and its operational meaning

The network resource consists of independently prepared single-particle links. A local phase disturbance acts collectively on all modes stored at one vertex. It destroys coherences between different local particle numbers but preserves coherences between distinct mode patterns with the same particle number. The question is how much bipartite entanglement survives this physical channel as the number of links incident on each vertex changes.

## Graph, modes and supplied links

Let $`G=(V,E)`$ be a finite simple bipartite graph with a specified color partition $`V=A\sqcup B`$. Write $`N=|V|`$, $`m=|E|`$ and $`d_v=\deg_G(v)`$. Isolated vertices are allowed unless a theorem explicitly assumes regularity or connectedness. Each edge $`e=\{a,b\}`$, with $`a\in A`$ and $`b\in B`$, has two labeled modes: one at each endpoint. Modes belonging to different edges remain distinct even when they occupy the same laboratory.

The supplied edge state and the full input are

```math
|\psi_e\rangle
 =\frac{|1\rangle_{a,e}|0\rangle_{b,e}
             +|0\rangle_{a,e}|1\rangle_{b,e}}{\sqrt2},
\qquad
|\Psi_G\rangle=\bigotimes_{e\in E}|\psi_e\rangle.
```

There is exactly one particle per edge and $`m`$ particles in total. The tensor factors here are labeled modes, rather than fictitious labels attached to identical particles. The discussion uses bosonic modes or distinguishable edge excitations with the stated tensor-product mode structure. A fermionic implementation would require its own algebra and parity conventions.

Order the edges once. For $`x\in\{0,1\}^{E}`$, set $`x_e=1`$ when edge $`e`$'s particle is at its $`A`$ endpoint. The corresponding occupation string at $`B`$ is the bitwise complement $`\bar x`$. Thus

```math
|\Psi_G\rangle
 =2^{-m/2}\sum_{x\in\{0,1\}^{E}}
       |x\rangle_A|\bar x\rangle_B.
```

Both displayed bases are orthonormal: a color coalition holds one labeled endpoint mode for every edge. This injective encoding of an edge orientation on both sides is why the exact entropy identity in [the next account](entropy_identity.md) uses the natural color cut. No formula for a general cut is assumed.

## Physical local number dephasing

At vertex $`v`$, let $`n_{v,e}`$ be the occupation operator for its mode on incident edge $`e`$, and let

```math
N_v=\sum_{e\ni v}n_{v,e},
\qquad
U(\boldsymbol\theta)
 =\bigotimes_{v\in V}e^{i\theta_vN_v}.
```

One batch undergoes the channel

```math
\mathcal T_G(\tau)
 =\int_{[0,2\pi)^V}
       U(\boldsymbol\theta)\tau U(\boldsymbol\theta)^\dagger
       \prod_{v\in V}\frac{d\theta_v}{2\pi},
\qquad
\rho_G=\mathcal T_G(|\Psi_G\rangle\langle\Psi_G|).
```

The angles are independent across vertices. At one vertex the same angle acts on every incident mode; independently dephasing every individual mode would erase the loop coherences studied here. The phase record is unavailable and the dephasing is a physical channel before any subsequent cooperation. A reference supplied afterward cannot reverse this lost record.

Equivalently, if $`\Pi_{\mathbf d}`$ projects onto the joint eigenspace with $`N_v=d_v'`$ for every vertex, then

```math
\mathcal T_G(\tau)
 =\sum_{\mathbf d}\Pi_{\mathbf d}\tau\Pi_{\mathbf d}.
```

Here $`\mathbf d`$ denotes an occupation vector, while $`d_v=\deg_G(v)`$ continues to denote graph degree. Measuring each laboratory's total number is nondestructive within these eigenspaces and leaves $`\rho_G`$ unchanged on average.

Repeated batches mean independently prepared and independently dephased copies $`\rho_G^{\otimes n}`$. This assumption matters. A stable unknown phase acting on several undephased inputs would instead give $`\mathcal T_G((|\Psi_G\rangle\langle\Psi_G|)^{\otimes n})`$, with a common phase per vertex. That is generally a different resource: two single-particle links between the same two laboratories already exhibit the familiar two-copy activation. The degree-three result is not a zero-capacity theorem for such stable-phase resources.

## Orientations and charges

Direct each edge toward the endpoint occupied by its particle. Its indegree vector is

```math
D_v(x)=
\begin{cases}
\displaystyle\sum_{e\ni v}x_e,&v\in A,\\[4pt]
\displaystyle\sum_{e\ni v}(1-x_e),&v\in B.
\end{cases}
```

For a uniform random orientation $`X`$, write $`D=D(X)`$. The notation $`D`$ is a classical random vector and $`N_v`$ is a quantum operator. They have the same occupation-number distribution in the input state. All entropies use base-two logarithms.

## Which operations and entanglement are counted?

The quantity $`E_D(\rho_G)`$ is ordinary asymptotic distillable entanglement across $`A|B`$: all laboratories in $`A`$ form one quantum coalition and all laboratories in $`B`$ form the other. Quantum processing within either coalition is allowed, with classical communication between coalitions. The companion quantity $`E_F(\rho_G)`$ is entanglement of formation across the same cut. These definitions concern the state after the physical dephasing.

The ideal-state extraction proof can first measure every local charge and then work entirely within the resulting fixed-charge subspaces. Such encoded operations do not require coherence between different particle numbers at any vertex. They can nevertheless require joint quantum gates between different laboratories in the same coalition. This account does not supply an extensive Bell-pair extraction protocol using only separate vertex operations and classical communication, nor an efficient circuit compiler for the coalition operations.

One use of the resource charges $`m`$ supplied single-particle edge states and $`2m`$ labeled endpoint modes. Graph preparation, storage, local charge measurements, internal phase control, classical messages and coalition quantum processing are ideal supplied operations; their hardware time, accuracy and synthesis costs are not evaluated here. The entanglement density is a statement about this resource state, rather than an end-to-end communication throughput or laboratory advantage.

## Relation to superselection and earlier activation

Local number twirling and fixed-number encoding are standard tools in the study of particle-number superselection. [Wiseman and Vaccaro](https://doi.org/10.1103/PhysRevLett.91.097902) distinguish mode entanglement from usable entanglement under particle-number restrictions; [Bartlett, Rudolph and Spekkens](https://doi.org/10.1103/RevModPhys.79.555) develop the reference-frame framework and activation examples. Loop activation itself is also established: [Abiuso and collaborators](https://doi.org/10.1103/PhysRevResearch.4.L012041) use three single-photon edge resources in a triangle to generate network-nonlocal correlations.

The results here concern the amount of surviving entanglement in whole sparse graph families after the specified physical local dephasing. Their density comparison requires the exact charge-sector entropy and the graph-degree estimates, beyond the existence of an activated triangle.

Continue with [the exact entropy identity](entropy_identity.md).
