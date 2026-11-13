# Entanglement Valence Threshold

**How many links must meet at a node for a macroscopic amount of entanglement to survive complete local number dephasing?**

Each edge of a simple bipartite graph supplies one single-excitation Bell state. All endpoint modes stored at one node acquire the same forgotten random phase, independently of other nodes. This physical noise removes coherence between different local particle numbers. Entanglement is measured between the two complete vertex-color classes, allowing collective quantum processing within each class.

The surviving resource has a sharp distinction between locally tree-like degree-three networks and degree-four networks. Both can start with extensive entanglement and extensively many independent undirected cycles. The existence of those cycles alone does not determine how much entanglement survives.

## Principal results

Let $`N`$ be the number of vertices and $`m`$ the number of edges. Orient each edge independently and fairly, and let $`D`$ be the full vertex-indegree vector. All entropies use base-two logarithms.

```math
E_D(\rho_G)=E_F(\rho_G)=m-H(D).
```

Here $`\rho_G`$ is the already dephased graph state. The identity follows from locally readable charge sectors, each of which is a maximally entangled state whose rank counts compatible orientations.

| Network family or error model | Established conclusion | Authoritative account |
| --- | --- | --- |
| Maximum degree three; locally tree-like as size grows | Entanglement per vertex tends to zero. For radius $`L`$, the finite bound is $`E_G\le 3b_L/2+9N/(L+3)`$, where $`b_L`$ counts non-tree neighborhoods. | [Degree-three bound](science/degree_three.md) |
| Every connected simple four-regular bipartite graph | $`E_G\ge\alpha_4N-I_4`$, with $`\alpha_4=0.019967671482\ldots`$ and $`I_4=0.050606733711\ldots`$. | [Degree-four bound](science/degree_four.md) |
| Additional independent edge phase-flip probability $`q`$ | $`E_D\ge[\alpha_4-2h_2(q)]N-I_4`$. The fixed example $`q=1/2000`$ has asymptotic density strictly above $`0.0074`$. | [Phase errors](science/robustness.md) |
| Externally flagged whole-edge deletion probability $`p`$ | Combined with phase errors, $`E_D\ge[\alpha_4-2p-2(1-p)h_2(q)]N-I_4`$. | [Flagged deletion](science/robustness.md#externally-heralded-edge-deletion) |

The four-link coefficient is a universal lower bound, not the exact optimal density. The low-degree conclusion requires local tree likeness: short-cycle networks can retain positive density even below degree four. The [examples](science/examples.md) show both the mechanism and this boundary.

## Why the distinction occurs

Local dephasing reveals the particle number at every vertex to an inaccessible environment. Two edge-occupation patterns can remain coherent only if they give exactly the same numbers. Such alternatives differ along directed cycles of the occupied-edge orientation.

At degree three, extending a directed path on a tree has two fresh candidate edges, each pointing forward with probability one half. Critical branching makes long coherent alternatives sparse. At degree four, correlations between neighboring revealed charges leave a provably extensive orientation uncertainty; a spanning-tree entropy bound certifies that it is positive. The quantum sector calculation turns this classical uncertainty into surviving entanglement.

## Read the science

Start with the [scientific overview](science/README.md), or use a direct route.

| Question | Read |
| --- | --- |
| What is supplied, physically dephased, and allowed during recovery? | [Model and resources](science/model.md) |
| Why does a classical orientation entropy equal entanglement? | [Exact charge-sector identity](science/entropy_identity.md) |
| Why does degree three lose density on locally tree-like graphs? | [Critical branching converse](science/degree_three.md) |
| Why does every connected four-regular bipartite graph retain density? | [Spanning-tree entropy lower bound](science/degree_four.md) |
| Which additional errors are covered? | [Robustness](science/robustness.md) |
| What happens on a tree, a cycle, and complete bipartite examples? | [Examples and finite checks](science/examples.md) |
| What does the threshold mean operationally? | [Interpretation](science/interpretation.md) |
| Which ingredients and close mechanisms are prior work? | [Related work](references/related_work.md) and [bibliography](references/references.bib) |

[The LLM reading guide](llms.txt) maps questions to the same authoritative sources.

## Reproduce the finite checks

From the repository root, with Python 3.12:

```bash
python -m pip install -r verification/requirements.txt
python verification/verify.py
```

The suite enumerates orientation fibers on small graphs, checks exact arithmetic certificates and evaluates small noisy sector spectra. The [verification guide](verification/README.md) identifies the coverage and numerical limits. Finite calculations support the examples; the arbitrary-size bounds are proved in the scientific pages.

## Scope

The shared random phase at a node acts on all its incident modes. Independent complete dephasing of every individual mode would destroy the resource. Repeated batches are independently dephased; a stable unknown phase reused coherently across batches is a different model.

Distillation allows collective quantum operations inside each color coalition. An efficient circuit, a separated-node extraction rate, and laboratory implementation costs are not established. The edge-loss result assumes a supplied classical record of whole-edge deletions; it does not provide a free nondestructive detector for generic photon loss. No entanglement-of-formation equality is claimed for the phase-error extension.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
