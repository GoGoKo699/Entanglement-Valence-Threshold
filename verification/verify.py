import json
import math
from fractions import Fraction
from collections import Counter, defaultdict
from itertools import product

import numpy as np


def entropy(probs):
    return -sum(float(p) * math.log2(float(p)) for p in probs if p > 0)


def fibers(n, edges):
    by_charge = defaultdict(list)
    for x in range(1 << len(edges)):
        d = [0] * n
        for i, (a, b) in enumerate(edges):
            d[b if (x >> i) & 1 else a] += 1
        by_charge[tuple(d)].append(x)
    return by_charge


def graph_record(name, n, edges, phase_error=None):
    fs = fibers(n, edges)
    m = len(edges)
    p = [len(f) / (1 << m) for f in fs.values()]
    e_flags = sum(len(f) * math.log2(len(f)) for f in fs.values()) / (1 << m)
    e_entropy = m - entropy(p)
    assert abs(e_flags - e_entropy) < 1e-10
    record = dict(name=name, vertices=n, edges=m, charge_sectors=len(fs),
                  entanglement_ebits=e_flags, entropy_identity_residual=e_flags - e_entropy)
    if phase_error is not None:
        eigenvalues = []
        for f in fs.values():
            mat = np.array([[(1 - 2 * phase_error)**((x ^ y).bit_count()) / (1 << m)
                             for y in f] for x in f])
            ev = np.linalg.eigvalsh(mat)
            assert min(ev) > -1e-12
            eigenvalues.extend(max(0., float(z)) for z in ev)
        assert abs(sum(eigenvalues) - 1) < 1e-10
        e_noisy = m - entropy(eigenvalues)
        lower = e_flags - m * entropy([phase_error, 1-phase_error])
        assert e_noisy + 1e-10 >= max(0., lower)
        record.update(phase_error=phase_error, noisy_mc_entanglement=e_noisy,
                      noisy_entropy_lower=lower)
    return record


def cut_spectrum_check(name, n, edges, sides, expected_cut, expected_entropy):
    sectors = fibers(n, edges)
    comparisons = 0
    largest_residual = 0.0
    tested_entropy = None
    for side in sides:
        incident_left = 0
        incident_right = 0
        for index, (a, b) in enumerate(edges):
            side_a = (side >> a) & 1
            side_b = (side >> b) & 1
            if side_a or side_b:
                incident_left |= 1 << index
            if not side_a or not side_b:
                incident_right |= 1 << index
        crossing = incident_left & incident_right
        entropy_weight = 0.0
        for patterns in sectors.values():
            # Restricted orientations index the orthogonal local occupations.
            rows = {p: i for i, p in enumerate(sorted({x & incident_left for x in patterns}))}
            cols = {p: i for i, p in enumerate(sorted({x & incident_right for x in patterns}))}
            coefficient = np.zeros((len(rows), len(cols)))
            amplitude = 1 / math.sqrt(len(patterns))
            for x in patterns:
                coefficient[rows[x & incident_left], cols[x & incident_right]] = amplitude
            singular = np.linalg.svd(coefficient, compute_uv=False)
            actual = sorted(value**2 for value in singular if value > 1e-12)
            multiplicities = Counter(x & crossing for x in patterns)
            expected = sorted(count / len(patterns) for count in multiplicities.values())
            assert len(actual) == len(expected)
            residual = max(abs(a - b) for a, b in zip(actual, expected))
            assert residual < 1e-12
            largest_residual = max(largest_residual, residual)
            entropy_weight += len(patterns) * entropy(actual)
            comparisons += 1
        if side == expected_cut:
            tested_entropy = entropy_weight / (1 << len(edges))
    assert tested_entropy is not None and abs(tested_entropy - expected_entropy) < 1e-10
    return dict(graph=name, cuts=len(sides), charge_cut_comparisons=comparisons,
                max_squared_singular_value_residual=largest_residual,
                selected_cut=expected_cut, selected_cut_entropy_ebits=tested_entropy)


def constants():
    d = 4
    binomial = [math.comb(d, k) / 2**d for k in range(d+1)]
    joint = np.zeros((d+1, d+1))
    for x, a, b in product(range(2), range(d), range(d)):
        joint[a+x, b+1-x] += .5 * math.comb(d-1,a) * math.comb(d-1,b) / 2**(2*(d-1))
    h = entropy(binomial)
    i = 2*h - entropy(joint.ravel())
    alpha = 2-h+i
    assert alpha > .0199
    rational = -Fraction(79, 64) + Fraction(9, 16)*Fraction(84, 53) + Fraction(5, 32)*Fraction(339, 146)
    assert 3**53 > 2**84 and 5**146 > 2**339
    assert rational == Fraction(617, 30952) and rational > Fraction(199, 10000)
    exact_positive = 3**36 * 5**10 > 2**79
    assert exact_positive
    noisy_coefficient = alpha - 2*entropy([1/2000,1999/2000])
    assert noisy_coefficient > .0074
    q = 1.
    for t in range(10000):
        assert q <= 4/(t+4) + 1e-12
        q -= q*q/4
    return dict(H_binomial_4=h, I_adjacent_4=i, alpha_4=alpha,
                alpha_exact_rational_lower=str(rational), alpha_exact_positive=exact_positive,
                q_1_over_2000_density_lower=noisy_coefficient,
                critical_branching_recurrence_checked_steps=10000)


def deletion_check(n, edges):
    m = len(edges)
    def E(es):
        f = fibers(n, es)
        return sum(len(v)*math.log2(len(v)) for v in f.values()) / 2**len(es)
    e = E(edges)
    drops = [e-E(edges[:k]+edges[k+1:]) for k in range(m)]
    assert all(-1e-10 <= z <= 1+1e-10 for z in drops)
    return dict(graph='K3,3', deletion_entanglement_drops=drops)


def main():
    rows = []
    for length in [4,6,8]:
        r = graph_record('cycle_'+str(length), length,
                         [(i, (i+1)%length) for i in range(length)], .001)
        assert abs(r['entanglement_ebits'] - 2**(1-length)) < 1e-10
        rows.append(r)
    r = graph_record('path_7', 7, [(i,i+1) for i in range(6)])
    assert r['entanglement_ebits'] == 0
    rows.append(r)
    short_cycles = [(i, (i//4)*4 + (i+1)%4) for i in range(8)] + [(0,5)]
    r = graph_record('two_C4_with_bridge', 8, short_cycles, .001)
    assert abs(r['entanglement_ebits'] - .25) < 1e-10
    rows.append(r)
    k33 = [(a,3+b) for a in range(3) for b in range(3)]
    rows.append(graph_record('K3,3', 6, k33, .001))
    k44 = [(a,4+b) for a in range(4) for b in range(4)]
    r = graph_record('K4,4', 8, k44)
    c = constants()
    assert r['entanglement_ebits'] >= 8*c['alpha_4'] - c['I_adjacent_4']
    rows.append(r)
    cycle_four = [(v, (v + 1) % 4) for v in range(4)]
    arbitrary_cuts = [
        cut_spectrum_check('cycle_4', 4, cycle_four, range(1, (1 << 4) - 1, 2),
                           0b0101, rows[0]['entanglement_ebits']),
        cut_spectrum_check('K3,3', 6, k33, range(1, (1 << 6) - 1, 2),
                           0b000111, rows[-2]['entanglement_ebits']),
        cut_spectrum_check('two_C4_with_bridge', 8, short_cycles, [0b00001111],
                           0b00001111, 0.0),
    ]
    print(json.dumps(dict(passed=True, constants=c, graphs=rows,
                         arbitrary_cuts=arbitrary_cuts,
                         deletion=deletion_check(6,k33),
                         scope='Finite orientation enumeration and double-precision sector spectra; universal bounds require the analytical proofs. No network-local distillation or physical implementation verified.'), indent=2))


if __name__ == '__main__':
    main()
