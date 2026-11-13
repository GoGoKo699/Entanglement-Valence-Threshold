# Extensive entanglement at degree four

After the physical node dephasing specified in [the model](model.md), every connected simple four-regular bipartite graph retains a positive amount of entanglement per vertex. No assumption on its girth is needed for this lower bound.

Let $`N=|V|`$ and $`m=|E|`$. All edges cross the two color coalitions $`A:B`$. Write $`D=(D_v)_{v\in V}`$ for the indegree vector of independent fair edge orientations, and use base-two entropies. The [orientation entropy identity](entropy_identity.md) gives

```math
E_D(\rho_G)=E_F(\rho_G)=m-H(D).
```

Here $`E_D`$ is distillable entanglement of independently and physically dephased batches, with collective quantum processing allowed within each color coalition. The identity also describes the average logarithmic Schmidt rank returned by the locally readable charge sectors of one ideal batch.

## The lower bound

**Theorem 3.** If $`G`$ is connected, simple, four-regular and bipartite, then

```math
E_D(\rho_G)=E_F(\rho_G)
\geq \alpha_4N-I_4,
```

where

```math
\begin{aligned}
I_4&=-\frac{39}{64}+\frac{3}{16}\log_2 3
                         +\frac{5}{32}\log_2 5
      =0.050606733711\ldots,\\
\alpha_4&=-\frac{79}{64}+\frac{9}{16}\log_2 3
                              +\frac{5}{32}\log_2 5
      =0.019967671482\ldots>0.0199.
\end{aligned}
```

In particular, for any such graph sequence with $`N\to\infty`$,

```math
\liminf_{N\to\infty}\frac{E_D(\rho_G)}{N}\geq\alpha_4>0.
```

The coefficient is a certified lower bound, rather than a claim about the exact limiting density.

## A spanning-tree entropy inequality

For any jointly distributed finite random variables $`(Y_v)_{v\in V}`$ and any spanning tree $`T`$,

```math
H(Y_V)\leq\sum_{v\in V}H(Y_v)
               -\sum_{uv\in E(T)}I(Y_u:Y_v).
```

To prove this, root $`T`$ at $`r`$ and order the other vertices so that every parent precedes its child. If $`\pi(v)`$ is the parent of $`v`$, the chain rule and conditioning give

```math
\begin{aligned}
H(Y_V)
&=H(Y_r)+\sum_{v\ne r}H(Y_v\mid Y_{\text{earlier vertices}})\\
&\leq H(Y_r)+\sum_{v\ne r}H(Y_v\mid Y_{\pi(v)})\\
&=\sum_v H(Y_v)-\sum_{v\ne r}I(Y_v:Y_{\pi(v)}).
\end{aligned}
```

This inequality does not assume that the variables form a tree Markov chain. The spanning tree only selects conditioning variables from their actual joint distribution.

## Exact vertex and adjacent-pair entropies

At a four-valent vertex, the four incident orientation bits are independent and fair. Therefore

```math
D_v\sim\mathrm{Bin}(4,1/2),\qquad
H_4:=H(D_v)=\frac{21}{8}-\frac{3}{8}\log_2 3
                  =2.030639062230\ldots.
```

For adjacent vertices $`u,v`$, their only common incident edge is $`uv`$, because the graph is simple. Let $`X`$ indicate that this edge points toward $`u`$. The other three incident edges at each endpoint contribute independent variables $`A_0,B_0\sim\mathrm{Bin}(3,1/2)`$, independent also of $`X\sim\mathrm{Bernoulli}(1/2)`$. Thus

```math
(D_u,D_v)=(A_0+X,\ B_0+1-X).
```

Their joint distribution, with rows and columns indexed by $`0,1,2,3,4`$, is

```math
P_4=\frac1{128}
\begin{pmatrix}
0&1&3&3&1\\
1&6&12&10&3\\
3&12&18&12&3\\
3&10&12&6&1\\
1&3&3&1&0
\end{pmatrix}.
```

Its row and column marginals are $`(1,4,6,4,1)/16`$. Direct evaluation gives

```math
\begin{aligned}
H(P_4)&=\frac{375}{64}-\frac{15}{16}\log_2 3
                              -\frac{5}{32}\log_2 5,\\
I(D_u:D_v)&=2H_4-H(P_4)=I_4.
\end{aligned}
```

Other edges elsewhere in the graph do not change this pair distribution. All underlying edge orientations are independent, including distinct edges that meet a common third vertex.

## Completing the proof

The tree inequality has $`N`$ vertex terms and $`N-1`$ adjacent-pair terms. Also $`m=2N`$ by four-regularity. Hence

```math
\begin{aligned}
H(D)&\leq NH_4-(N-1)I_4,\\
E_D(\rho_G)&=2N-H(D)\\
&\geq(2-H_4+I_4)N-I_4
 =\alpha_4N-I_4.
\end{aligned}
```

Positivity can be checked without relying on rounded decimal values. The exact integer inequalities $`3^{53}>2^{84}`$ and $`5^{146}>2^{339}`$ imply

```math
\alpha_4>
-\frac{79}{64}+\frac9{16}\frac{84}{53}
                  +\frac5{32}\frac{339}{146}
=\frac{617}{30952}>\frac{199}{10000}.
```

For a four-regular graph with $`c`$ connected components, applying the proof separately gives $`E_D\geq\alpha_4N-I_4c`$. Thus connectedness controls the finite component correction; it is not a claim that disconnected components destroy one another's entanglement.

## What this establishes

The [degree-three upper bound](degree_three.md) applies to locally tree-like graph sequences and gives vanishing entanglement per vertex. The lower bound here applies to every connected simple four-regular bipartite graph, including locally tree-like sequences. Both input families contain an extensive number of ideal bond ebits: $`3N/2`$ for three-regular graphs and $`2N`$ for four-regular graphs.

The result concerns the surviving entanglement of an actual mixed state across the color cut. It permits collective operations within each coalition and does not provide a rate or cost for transporting that entanglement between individually controlled network sites. Its tolerance to additional edge errors is quantified in [robustness](robustness.md).
