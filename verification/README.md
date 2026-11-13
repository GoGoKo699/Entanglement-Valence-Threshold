# Reproduce the finite scientific checks

Use Python 3.12, with the NumPy version pinned in [requirements.txt](requirements.txt):

```bash
python -m pip install -r verification/requirements.txt
python verification/verify.py
```

The command prints a JSON report and exits nonzero if a checked assertion fails. [results.json](results.json) records the reference run with Python 3.12 and NumPy 2.3.5. There is no randomized seed: all listed graph orientations and sector matrices are deterministic.

## What is checked

- Every orientation is enumerated for paths, even cycles of lengths four, six and eight, two four-cycles joined by a bridge, and the complete bipartite graphs $`K_{3,3}`$ and $`K_{4,4}`$.
- Equal-indegree fibers yield the same average logarithmic rank as $`m-H(D)`$. Forest zero entanglement, the exact cycle value and the short-cycle counterexample are asserted.
- The exact adjacent-charge matrix recovers $`H_4`$, $`I_4`$ and $`\alpha_4`$. Integer and rational arithmetic verify the certificates $`\alpha_4>617/30952>0.0199`$.
- The critical branching recurrence is evaluated for 10,000 steps and compared with its analytical upper bound. This tests indexing and implementation; the proof holds for all steps independently.
- For selected small graphs with extra phase-error probability $`q=0.001`$, the exact charge-block coefficient matrices are diagonalized. Positivity, trace one and the noisy coherent-information lower bound are checked.
- Deleting each of the nine edges of $`K_{3,3}`$ is enumerated separately to test the one-ebit deletion bound. This calculation assumes known deleted-edge identity.

## Numerical and analytical boundaries

Orientation multiplicities and the positivity certificates use exact integers. Entropies and sector spectra use double precision, with explicit tolerances in [verify.py](verify.py). This is not an interval-arithmetic certificate for printed decimal entropies or for the approximate additional-noise threshold.

The arbitrary-size claims follow from the written [degree-three](../science/degree_three.md), [degree-four](../science/degree_four.md) and [robustness](../science/robustness.md) proofs. Small graph enumeration cannot establish a thermodynamic limit, an efficient distillation circuit, a separated-node network rate or a physical implementation. The finite complete bipartite examples have short cycles and are not evidence for local tree likeness.

## Hosted mathematical review

The [hosted mathematics workflow](../.github/workflows/hosted-math.yml) runs only for same-repository pull requests, with read-only contents permission and the exact proposed commit checked out without persisted credentials. Its pinned Playwright and MathJax runtime first probes the README, then compares every tracked Markdown page at widths 1440 and 760 once the learning route is present.

The utilities in [hosted_math](hosted_math/) inventory the pinned source, compare the actual hosted MathML with compiled source structure, and retain HTML, screenshots and a report as workflow artifacts. A passing structural report still requires inspection of the actual screenshots and scientific wording. It does not certify future renderer behavior or establish scientific correctness. Workflow artifacts have limited retention; they are reproducible review evidence rather than the scientific source.
