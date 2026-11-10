# Additive ESCM: persistence, local inhibition, and spatial replacement

**Status:** theoretical candidate and independent numerical feasibility study, 10 November 2026.  
**Scope:** current-based additive LIF model with a membrane-potential floor. This is **not** a claim that the frozen ESCM 2.0 benchmark, the existing Brian2 notebooks, or the SRR model have been changed or validated against this candidate.

## Research question

Can a **single event-camera event** recruit a neuron that subsequently fires autonomously; can a new spatial population then suppress an established representation while remaining active itself; and how does the **inner exclusion** of the inhibitory kernel affect this competition?

The intended behavior is (i) activation from one sensory event, (ii) persistence without sensory support, (iii) replacement of obsolete *nearby* activity, and (iv) coexistence at sufficient spatial separation. Sensory-replenished resources (SRR) and eventual fading are separate future mechanisms.

## 1. Candidate neuronal dynamics

Use dimensionless membrane voltage with rest/reset/floor at zero and spike threshold at one. Time is in milliseconds:

\[
\begin{aligned}
10\dot v_i &=-v_i+I_{e,i}+I_{s,i}-I_{h,i},\qquad v_i\ge 0,\\
5\dot I_{e,i}&=-I_{e,i},\\
3\dot I_{s,i}&=-I_{s,i},\\
12\dot I_{h,i}&=-I_{h,i}.
\end{aligned}
\]

At the floor, negative voltage motion is suppressed:
\[
\dot v_i=\max\{0,(I_{e,i}+I_{s,i}-I_{h,i})/10\}\quad\text{when }v_i=0.
\]

At an **output spike**, reset \(v_i\gets0\), increase the additive autaptic current \(I_{e,i}\gets I_{e,i}+W\), and deliver lateral inhibitory increments to other neurons. Spike generation is blocked for an absolute refractory period \(r\), while synaptic currents keep decaying. At one **camera event**, \(I_{s,i}\gets I_{s,i}+\beta\).

The candidate operating point studied here is:

| Quantity | Value |
| --- | ---: |
| Membrane time constant \(\tau_m\) | 10 ms |
| Autaptic current decay \(\tau_e\) | 5 ms |
| Sensory current decay \(\tau_s\) | 3 ms |
| Inhibition decay \(\tau_h\) | 12 ms |
| Voltage floor / reset / threshold | \(0/0/1\) |
| Refractory period \(r\) | 2 ms |
| Output-spike autaptic increment \(W\) | 4.1 |
| Sensory-event amplitude in switching examples \(\beta\) | 8 |

These are **mathematical design choices**, not the parameter values of every existing repository implementation.

## 2. One-event recruitment and one-spike persistence

With \(v(0)=I_e(0)=I_h(0)=0\), one sensory event produces

\[
v(t)=\beta h_s(t),\qquad
h_s(t)=\frac37(e^{-t/10}-e^{-t/3}).
\]

The maximum occurs at \(t=(30/7)\ln(10/3)\approx5.16\) ms. Hence, in isolation, the limiting sensory amplitude is
\[
\boxed{\beta_{\rm crit}(0)=1/\max_{t>0}h_s(t)\approx5.584.}
\]
A **strictly larger** amplitude is required if spikes use the condition \(v>1\). During inhibition the threshold rises; a value just above 5.584 offers little recruitment margin.

Following a *single output spike*, with no further sensory input or inhibition,
\[
v(t)=W h_e(t),\qquad h_e(t)=e^{-t/10}-e^{-t/5}.
\]
Since \(\max h_e=1/4\) at \(10\ln 2\approx6.93\) ms, the choice \(r=2\) ms and
\[
\boxed{W>4}
\]
guarantees another spike, and by repetition autonomous firing in **isolation**. The lower voltage floor does not affect this positive trajectory.

When a neuron fires at the refractory limit, its post-spike autaptic current satisfies
\[
J_{n+1}=J_n e^{-r/5}+W,\qquad
\boxed{J^*=\frac{W}{1-e^{-r/5}}\approx12.4363.}
\]
The locked rate is \(1/r=500\) Hz. This is the specified candidate operating point, **not** a required rate for every inhibited neuron.

## 3. Spatial inhibitory kernel: two variants

For neurons at Euclidean pixel distance \(d_{ij}\), use current increments \(K(d_{ij})\) upon a presynaptic output spike.

Original inner exclusion:
\[
K_{\rm excl}(d)=
0.1 e^{-d^2/12.5}\,\mathbf 1\{1.5<d\le5.5\}.
\]

Proposed ablation, with exclusion removed:
\[
K_{\rm full}(d)=
0.1 e^{-d^2/12.5}\,\mathbf 1\{0<d\le5.5\}.
\]

**Self-inhibition is absent in both**. In the original kernel, cardinal neighbors (\(d=1\)) and diagonal neighbors (\(d=\sqrt2\)) do not inhibit one another; inhibition begins at \(d=2\). Both variants have the same outer cutoff.

For any active set \(B\), define its geometric coupling into neuron \(i\):
\[
\boxed{C_i(B)=\sum_{j\in B}K(d_{ij}).}
\]
The time-dependent inhibitory current is
\[
\boxed{
I_{h,i}(t)=
\sum_j K(d_{ij})\sum_{k:t_{j,k}\le t}
e^{-(t-t_{j,k})/12},
}
\]
plus any residual inhibitory current from before the chosen time origin. Hence geometry and presynaptic timing both matter.

**Provenance:** the annular Gaussian choice was inspected in [Notebook 32: additive ESCM 2.0 parity](../notebooks/32_additive_escm20_parity.ipynb). The mathematical candidate here must not be conflated with the historical model families distinguished in [the research notebook guide](index.md).

## 4. Phase-independent bounds for periodic firing

Suppose every neuron in \(B\) fires periodically at interval \(r=2\) ms, but with arbitrary relative phases, and its inhibitory currents have reached their periodic regime. For a postsynaptic neuron \(i\),
\[
\frac{C_i(B)e^{-r/12}}{1-e^{-r/12}}
\ \le I_{h,i}(t)\le\
\frac{C_i(B)}{1-e^{-r/12}}.
\]
These are conservative bounds: the upper extremes from different presynaptic neurons need not occur simultaneously.

### 4.1 Persistence of an already-established population

Immediately after a neuron fires with \(I_e=J^*\), bound its inhibitory current by the maximum above. The voltage floor can only raise voltage relative to the unconstrained comparison solution. Thus a sufficient condition to spike again on refractory release is
\[
J^*h_e(r)-
\frac{C_i(B)}{1-e^{-r/12}}
(1-e^{-r/10})>1.
\]

Solving yields
\[
\boxed{
C_i(B)< C_{\rm lock}
=\frac{[J^*h_e(r)-1](1-e^{-r/12})}{1-e^{-r/10}}
\approx0.716213.
}
\]
If this holds for every neuron in an already locked active population (with no further external inhibition), then refractory-locked firing is maintained for arbitrary fixed phase offsets. This is **sufficient, not necessary**, and does not by itself prove initial recruitment.

For a newly activated set \(B\), the corresponding internal-coupling criterion is \(\max_{i\in B}C_i(B)<C_{\rm lock}\).

### 4.2 An obstruction when cross-coupling is too weak

Let \(A\) be an established single neuron, initially firing at the locked rate, and let new population \(B\) be the **only** new source of inhibition. If the initial inhibitory current does not exceed the periodic upper bound and \(B\) cannot fire faster than once per \(r\), then
\[
\boxed{C_A(B)<0.716213}
\]
prevents \(B\) from interrupting \(A\)'s locked firing, whatever the relative B spike phases. The argument is inductive: at each A spike the autaptic state remains \(J^*\) and voltage must cross threshold by refractory release. This obstruction applies to the stated initial conditions, **not** to arbitrary pre-inhibited or externally perturbed neurons.

### 4.3 Strong sustained inhibition can guarantee termination

If \(B\) *already maintains* its periodic firing, the inhibitory current into \(A\) is always at least
\[
H_{\min}=\frac{C_A(B)e^{-r/12}}{1-e^{-r/12}}.
\]
After an A spike, compare with constant inhibition \(H_{\min}\). Preventing any further spike from the maximal locked autaptic state \(J^*\) is ensured by
\[
H_{\min}>
\sup_{t\ge r}
\frac{J^*h_e(t)-1}{1-e^{-t/10}}
\approx5.383275.
\]
Consequently,
\[
\boxed{
C_A(B)>C_{\rm kill}
=5.383275(e^{r/12}-1)
\approx0.976313
}
\]
is a sufficient condition for termination after a reset once B's periodic inhibitory regime is present. It is **not** a necessary condition and cannot alone establish one-event recruitment of B.

A convenient **feasibility regime with sufficiently sustained sensory support for recruitment** is therefore
\[
\boxed{
C_A(B)>0.976313,\qquad
\max_{i\in B}C_i(B)<0.716213.
}
\]
The first inequality suppresses A; the second protects the locked B population after inhibition from A dissipates. A transient support protocol must still bring B into the requisite state. These inequalities do **not** guarantee that one single sensory event will accomplish that transition.

## 5. Exact handling of the voltage floor

For an old neuron reset at \(t=0\), with a prescribed inhibitory spike train and no further input to that neuron, set
\[
D(t)=J e^{-t/5}-I_h(t),\qquad
F(t)=\frac1{10}\int_0^t e^{s/10}D(s)\,ds.
\]
The bounded-voltage solution until the next spike is
\[
\boxed{
v(t)=e^{-t/10}
\left[F(t)-\min\left(0,\min_{0\le u\le t}F(u)\right)\right].
}
\]
This formula is the reflected solution of the membrane ODE at the floor; threshold crossings are eligible only after refractoriness. It allows precise trajectory-based termination tests for arbitrary *specified* inhibitory spike times, without pretending that those times are known in advance in the fully coupled network.

## 6. Numerical witness: coupled recruitment and replacement

An independent fixed-step numerical experiment studied one established central neuron \(A\) at \((0,0)\), surrounded by a new square-ring population \(B\) at lattice locations with \(\max(|x|,|y|)=R\).

At \(t=0\): A has the steady 2 ms autaptic state and has just spiked; B is silent but carries steady inhibition from A's prior spikes. **Every B neuron receives exactly one sensory event of amplitude \(\beta=8\)**; there is no additional input. The simulation integrates the linear subthreshold membrane response over each 0.005 ms step, applies the voltage floor, then applies threshold/reset/inhibitory events. It runs for 250 ms.

The user independently ran the same standalone script and reproduced:

| Inner exclusion | Ring radius \(R\) | \(|B|\) | \(C_A(B)\) | Max. internal \(C_i(B)\) | A's last spike | B neurons active late | Replaced? |
| --- | ---: | ---: | ---: | ---: | --- | ---: | --- |
| 1.5 | 2 | 16 | 1.03763 | 0.57496 | 22.72 ms | 16/16 | Yes |
| 0 | 2 | 16 | 1.03763 | 0.75958 | Still spikes at 250 ms | 12/16 | No |
| 1.5 | 3 | 24 | 0.93170 | 0.47759 | 28.89 ms | 24/24 | Yes |
| 0 | 3 | 24 | 0.93170 | 0.66221 | 28.80 ms | 24/24 | Yes |

Here “active late” means at least 45 spikes in the interval 150–250 ms (the numerical script's actual readout), and “replaced” means A stops while the full B population persists. These results are **numerical examples**, not Brian2 replication, a proof for arbitrary event patterns, or a convergence theorem for all timesteps. The standalone witness script was supplied in the research discussion; **it is not yet committed in this repository**.

The radius-2 original-exclusion geometry satisfies both strict analytical feasibility inequalities. Radius-3 geometries can succeed even though their cross-coupling \(0.93170\) is below the conservative \(0.976313\) sufficient termination threshold.

## 7. Mechanism behind progressive termination

The autaptic state after successive output spikes obeys
\[
\boxed{J_{n+1}=J_n e^{-T_n/5}+W},
\]
where \(T_n\) is the actual interspike interval. If inhibition delays an old neuron's spike beyond 2 ms, then its autaptic current decays for longer before the next increment. Consequently, subsequent spikes can become progressively easier to delay and eventually cease.

This supplies an explanation for a successful switching trajectory even when the **one-step** sufficient termination bound is not satisfied. It does not convert the timing-dependent intermediate regime into a universal termination guarantee.

Removing the inner exclusion increases inhibition **within** a close-packed new population as well as inhibition between populations. In the radius-2 ring it disrupts full B persistence; in the radius-3 ring it does not. More inhibition is therefore not monotonically better for replacement.

## 8. Conclusions and limitations

**Established within this candidate model:**

- A sensory event above the isolated recruitment threshold can produce an initial spike; \(W>4\) then sustains spiking in isolation.
- The lower voltage floor prevents negative membrane accumulation but **does not erase inhibitory current** or guarantee recruitment under inhibition.
- Kernel geometry yields exact coupling sums and conservative phase-independent persistence / termination tests.
- A fully coupled numerical witness achieves **one-event-per-new-neuron replacement** for specific ring geometries, including with and without the inner exclusion.
- The original inner exclusion performs better than removing it for the tested radius-2 ring; neither variant wins universally.

**Not yet established:**

- One-event replacement for arbitrary shapes, old/new overlap, sparse irregular event timing, heterogeneous firing rates, or noisy camera inputs.
- General stability of asynchronous representations and a quantitative guarantee of distant coexistence in the presence of intermediate populations.
- Timestep-independent numerical convergence or equivalence to Brian2's scheduling and update semantics.
- The influence of SRR-mediated fading (not included here).

**Next research step:** test the *same candidate equations* against geometries and asynchronous event sequences drawn from the repository's spatial-competition benchmarks, with matched old-only and new-only persistence controls, and compare both kernel variants before introducing SRR. Preserve failed configurations and do not call inactivity “replacement” without confirming the old-only control persists.

## Related repository sources

- [Research notebook guide](index.md) — distinguishes legacy, frozen, fading, additive, and SRR model families.
- [Mathematical foundations of replacement](../notebooks/16_mathematical_foundations_replacement.ipynb).
- [Spatial generalization](../notebooks/19_spatial_generalization.ipynb).
- [Additive autapse validation](../notebooks/24_additive_autapse_validation.ipynb).
- [Additive ESCM 2.0 parity](../notebooks/32_additive_escm20_parity.ipynb).

