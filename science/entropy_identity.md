# Charge-sector entropy equals surviving entanglement

For the bipartite resource and physical dephasing defined in [the model](model.md), the full entanglement calculation reduces to a classical question: how many orientations have the same vertex indegrees? This reduction keeps all number outcomes. It does not select only a rare favorable sector.

## Orientation fibers

For an attainable occupation vector $`\mathbf d`$, define its fiber and multiplicity by

```math
\mathcal F_{\mathbf d}
 =\{x\in\{0,1\}^{E}:D(x)=\mathbf d\},
\qquad
f_{\mathbf d}=|\mathcal F_{\mathbf d}|,
\qquad
p_{\mathbf d}=\frac{f_{\mathbf d}}{2^m}.
```

Vectors with $`f_{\mathbf d}=0`$ are omitted from sums. Independent integration of the vertex phases retains a matrix element between orientations $`x,y`$ exactly when $`D(x)=D(y)`$. Consequently,

```math
\rho_G
 =\sum_{\mathbf d}p_{\mathbf d}
       |\phi_{\mathbf d}\rangle\langle\phi_{\mathbf d}|,
\qquad
|\phi_{\mathbf d}\rangle
 =\frac{1}{\sqrt{f_{\mathbf d}}}
      \sum_{x\in\mathcal F_{\mathbf d}}
         |x\rangle_A|\bar x\rangle_B.
```

Distinct orientations label orthogonal states on both sides of the color cut. Thus the displayed sum for $`|\phi_{\mathbf d}\rangle`$ is already a Schmidt decomposition, with $`f_{\mathbf d}`$ equal Schmidt coefficients. Its entanglement entropy is $`\log_2 f_{\mathbf d}`$.

The full vector $`\mathbf d`$ is available by measuring all local particle numbers and exchanging the classical results. A side alone need not know the other side's charges. The required instrument is still local across the color cut, and its outcomes leave pure conditional states as displayed above.

## Exact identity

**Theorem 1.** For every finite simple bipartite graph in the stated model,

```math
\boxed{
E_D(\rho_G)=E_F(\rho_G)
 =\sum_{\mathbf d}p_{\mathbf d}\log_2f_{\mathbf d}
 =m-H(D).
}
```

Here $`E_D`$ is an asymptotic rate for independent copies of the already dephased state, with coalition operations as specified in the model. It is not a claim that one batch always produces $`m-H(D)`$ integer Bell pairs.

**Proof of the classical equality.** Since the orientation is uniform, conditioning on $`D=\mathbf d`$ is uniform on $`\mathcal F_{\mathbf d}`$. Therefore

```math
H(X\mid D)
 =\sum_{\mathbf d}p_{\mathbf d}\log_2f_{\mathbf d}
 =H(X)-H(D)=m-H(D),
```

because $`D`$ is a deterministic function of $`X`$ and $`H(X)=m`$.

**Proof for entanglement of formation.** The displayed pure-state decomposition gives

```math
E_F(\rho_G)
 \le\sum_{\mathbf d}p_{\mathbf d}\log_2f_{\mathbf d}.
```

Conversely, local charge measurement followed by classical communication produces exactly that ensemble. Average entanglement of formation cannot increase under this local instrument, giving the reverse inequality. This uses the standard convex-roof entanglement monotonicity developed in [Bennett, DiVincenzo, Smolin and Wootters](https://doi.org/10.1103/PhysRevA.54.3824), rather than a new monotonicity principle.

**Proof for distillable entanglement.** First measure the charges separately in every one of $`n`$ independent copies. Copies with label $`\mathbf d`$ can be grouped inside each coalition. If $`n_{\mathbf d}`$ copies have that label, their joint conditional state is maximally entangled with Schmidt rank $`f_{\mathbf d}^{n_{\mathbf d}}`$. It can be converted deterministically to

```math
\left\lfloor n_{\mathbf d}\log_2f_{\mathbf d}\right\rfloor
```

Bell pairs. For each fixed graph there are finitely many labels, so the total rounding loss is bounded independently of $`n`$. The law of large numbers gives $`n_{\mathbf d}/n\to p_{\mathbf d}`$, and hence the achievable rate is the asserted average. The usual entanglement-of-formation upper bound on distillable entanglement then proves equality. All conditional quantum operations stay inside fixed local charge sectors. ∎

The deterministic conversion just used is a standard consequence of [Nielsen's pure-state conversion theorem](https://doi.org/10.1103/PhysRevLett.83.436). The following explicit construction also proves the particular flat-spectrum case needed here.

## Integer Bell yield from one batch

Suppose a sector has Schmidt rank $`f`$, and set $`k=\lfloor\log_2f\rfloor`$ and $`M=2^k`$. Label its Schmidt basis by $`1,\ldots,f`$. For every $`M`$-element subset $`S`$ of that set, let $`P_S`$ be the corresponding projector on coalition $`A`$ and use the measurement operator

```math
A_S=\binom{f-1}{M-1}^{-1/2}P_S.
```

Every basis index occurs in exactly $`\binom{f-1}{M-1}`$ subsets, so $`\sum_S A_S^\dagger A_S=I`$. For every outcome, the normalized conditional state is maximally entangled on the $`M`$ matching basis elements in $`S`$. Communicating $`S`$ and relabeling those elements on both sides gives $`|\Phi_M\rangle`$, which encodes exactly $`k`$ Bell pairs. Every outcome succeeds; no favorable measurement outcome is discarded. All projectors act within the same fixed-charge sector.

Thus one independently dephased ideal batch permits the random integer output

```math
K(D)=\left\lfloor\log_2 f_D\right\rfloor,
\qquad
E_G-1<\mathbb E[K(D)]\le E_G,
\qquad E_G:=m-H(D).
```

The strict lower inequality follows from $`\lfloor t\rfloor>t-1`$ for every real $`t`$. When $`E_G<1`$ it is only a weak bound; the output remains nonnegative. The subset measurement can have a very large outcome alphabet, and constructing the fiber basis can be computationally costly. This proof establishes existence under the ideal coalition model. It does not establish an efficient measurement circuit or a fixed output yield in every charge sector.

## Basic checks

For an empty graph, $`m=0`$ and the only fiber has size one, so $`E_G=0`$. For a forest, leaf removal reconstructs the orientation uniquely from its indegrees: a leaf's charge fixes its incident edge, after which one removes that edge and adjusts its neighbor's charge. Every fiber again has size one and the twirled state is a mixture of occupation-basis product states.

For a simple even cycle of length $`\ell`$, the all-one indegree vector has two orientations, the two consistent circulations. Every other indegree vector has a unique orientation. The two-element sector has probability $`2^{1-\ell}`$ and is an encoded GHZ state, while all other sectors are product. Therefore $`E_G=2^{1-\ell}`$ across the color cut. This check illustrates why the existence of loops alone does not imply a nonzero entanglement density as cycle lengths grow.

The quantitative question for sparse networks is how often random orientations admit large same-indegree fibers. Continue with [the degree-three upper bound](degree_three.md).
