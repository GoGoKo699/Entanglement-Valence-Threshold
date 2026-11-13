# Why locally tree-like degree-three networks have zero density

A long undirected cycle can retain coherence only when the random edge orientation supports a directed circulation. At degree three, exploring a directed path has two fresh candidate edges per nonroot vertex, each pointing forward with probability one half. The resulting branching process is critical. Its survival bound controls the entropy left after all local particle numbers have been revealed.

This account proves a finite-graph bound first. The limit theorem then follows in a specified order and does not assume a finite-size critical exponent.

## Equal indegrees require directed-cycle changes

Fix an orientation $`x`$. Let $`C(x)`$ be the set of edges that lie on at least one directed cycle in $`x`$, and let $`Z(x)`$ be the set of vertices on such cycles. If another orientation $`y`$ has $`D(y)=D(x)`$, consider precisely the edges whose directions differ. At each vertex, the number of those edges pointing in under $`x`$ equals the number pointing out: reversing the changed edges preserves indegree only under this balance condition.

Every finite balanced directed graph decomposes into directed cycles. To see this directly, start at an edge and continue along outgoing edges. Balance prevents a trail from becoming stuck before revisiting a vertex. A repeated vertex gives a directed cycle; remove its edges and repeat on the remaining balanced graph. Consequently every changed edge lies in $`C(x)`$. All orientations in the fiber of $`D(x)`$ therefore agree with $`x`$ outside $`C(x)`$, and

```math
f_{D(x)}\le 2^{|C(x)|},
\qquad
\log_2 f_{D(x)}\le |C(x)|.
```

If the maximum degree is at most three, every edge in $`C(x)`$ has both endpoints in $`Z(x)`$ and the sum of degrees within this edge set is at most $`3|Z(x)|`$. Hence

```math
|C(x)|\le\frac32|Z(x)|.
```

Using the [entropy identity](entropy_identity.md) and averaging over independent fair edge orientations gives

```math
E_G=\mathbb E[\log_2f_D]
 \le\frac32\sum_{v\in V}\Pr(v\in Z(X)).
```

The cycle decomposition and the forthcoming branching calculation are elementary graph and probability tools. Their role is to bound this particular charge-fiber entanglement, rather than to introduce a new cycle decomposition or branching theorem.

## The critical survival estimate, with indexing

Let $`q_t`$ be the probability that a rooted binary tree with independent forward edge probability $`1/2`$ contains a directed path of length $`t`$ from its root. A path of length zero always exists, so $`q_0=1`$. For the root to have no length-$`t+1`$ path, both candidate children must fail; each child succeeds with probability $`q_t/2`$. Thus

```math
q_{t+1}=1-\left(1-\frac{q_t}{2}\right)^2
       =q_t-\frac{q_t^2}{4}.
```

For every integer $`t\ge0`$,

```math
q_t\le\frac{4}{t+4}.
```

Indeed, equality holds at $`t=0`$. The map $`z\mapsto z-z^2/4`$ is increasing on $`[0,1]`$. If the estimate holds at $`t`$, its next value is at most

```math
\frac{4}{t+4}-\frac{4}{(t+4)^2}
 =\frac{4(t+3)}{(t+4)^2}
 \le\frac{4}{t+5},
```

where the last inequality is equivalent to $`(t+3)(t+5)\le(t+4)^2`$.

Now let $`L\ge1`$. A degree-at-most-three root has at most three first edges and at most two fresh edges at every later step. If its radius-$`L`$ ball is a tree, the relevant edge orientations are independent, and its probability of having a directed nonbacktracking path of length $`L`$ is at most

```math
1-\left(1-\frac{q_{L-1}}2\right)^3
 \le\frac32q_{L-1}
 \le\frac{6}{L+3}.
```

The first inequality may be a strict domination when some vertices have degree below three. The displayed bound can exceed one for small $`L`$; it remains valid, and may be replaced by its minimum with one.

## A finite-graph local-tree bound

For a graph $`G`$, define its radius-$`L`$ ball to be the subgraph induced by all vertices of graph distance at most $`L`$ from the root. Let

```math
b_L(G)=\bigl|\{v\in V:
            B_G(v,L)\text{ is not a tree}\}\bigr|.
```

**Theorem 2.** Let $`G`$ be a finite simple bipartite graph of maximum degree at most three, and let $`L\ge1`$. Then

```math
\boxed{
0\le E_G\le
   \frac32 b_L(G)+\frac{9N}{L+3}.
}
```

**Proof.** If $`B_G(v,L)`$ is a tree and $`v`$ lies on a directed cycle, following that cycle from $`v`$ provides a directed nonbacktracking path of length $`L`$. A cycle of length at most $`L`$ would already lie inside the ball and contradict its being a tree, so this path has distinct vertices. The previous survival calculation bounds its probability by $`6/(L+3)`$.

For each of the $`b_L(G)`$ bad vertices use the trivial bound one. Substitution in the cycle-entropy estimate gives the slightly sharper expression

```math
E_G\le\frac32 b_L(G)
        +\frac{9\bigl(N-b_L(G)\bigr)}{L+3},
```

and dropping the negative term proves the stated bound. Nonnegativity follows either from entanglement or from $`H(D)\le H(X)=m`$. ∎

## Locally tree-like sequences

**Corollary 2.1.** Let $`(G_n)`$ be any sequence of finite simple bipartite graphs, with $`N_n\to\infty`$ and maximum degree at most three. Suppose that for every fixed integer $`L\ge1`$,

```math
\frac{b_L(G_n)}{N_n}\longrightarrow0.
```

Then

```math
\frac{E_{G_n}}{N_n}\longrightarrow0.
```

**Proof.** For fixed $`L`$, divide Theorem 2 by $`N_n`$ and let $`n\to\infty`$. This gives a limit superior at most $`9/(L+3)`$. Letting $`L\to\infty`$ makes that upper bound zero. The order is graph size first at each fixed neighborhood radius, then radius. ∎

The assumption is local tree likeness; expansion, connectedness and exact three-regularity are unnecessary. In particular, for uniformly sampled simple three-regular bipartite graphs, fixed-radius neighborhood exposure has a collision probability tending to zero. Thus the same statement holds in probability for that ensemble. This use of the standard configuration-model neighborhood argument asserts no sharp finite-size rate.

## High girth as a concrete sufficient condition

Let $`g(G)`$ be the length of the shortest undirected cycle, with $`g(G)=\infty`$ for a forest. A safe radius choice for finite girth $`g\ge4`$ is

```math
L=\left\lfloor\frac{g-2}{2}\right\rfloor.
```

Then $`2L+1\lt g`$, so every induced radius-$`L`$ ball is a tree: any extra edge between breadth-first-tree branches inside the ball would create a cycle of length at most $`2L+1`$. Theorem 2 gives

```math
E_G\le\frac{9N}{L+3}
     =O\!\left(\frac{N}{g}\right).
```

For the bipartite graphs considered here, finite girth is even, so the alternative expression $`L=g/2-1`$ is equivalent. Forests have $`E_G=0`$ exactly by orientation reconstruction, independently of this radius estimate.

The conclusion is that the surviving entanglement per vertex vanishes for increasingly tree-like degree-three networks. It does not say that each finite graph is separable, or that every cycle has zero usable entanglement. The comparison with degree four therefore concerns an extensive density, rather than the first appearance of any entanglement.
