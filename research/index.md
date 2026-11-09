# ESCM research: curated notebook guide

This directory provides **eight entry-point research notebooks** organized by scientific question. Each entry point currently preserves the complete committed cells and recorded outputs of one representative notebook and adds a provenance/interpretation introduction. **It is a safe first-stage curation, not a claim that 31 experiments have been mathematically merged or re-executed.** All original `notebooks/01_...ipynb` through `notebooks/31_...ipynb` remain in place, including negative results and independent audits.

## Read these notebooks in order

| Curated entry point | Committed experiment preserved | Main role |
| --- | --- | --- |
| [01_legacy_and_parity.ipynb](01_legacy_and_parity.ipynb) | [03_legacy_vs_refactored](../notebooks/03_legacy_vs_refactored.ipynb) | Original ESCM parity |
| [02_original_mechanisms.ipynb](02_original_mechanisms.ipynb) | [06_mechanism_ablations](../notebooks/06_mechanism_ablations.ipynb) | Original-mechanism ablations |
| [03_mathematics_and_numerics.ipynb](03_mathematics_and_numerics.ipynb) | [16_mathematical_foundations_replacement](../notebooks/16_mathematical_foundations_replacement.ipynb) | Analytical foundations and numerical caveats |
| [04_frozen_escm20_benchmark.ipynb](04_frozen_escm20_benchmark.ipynb) | [22_original_vs_frozen_validation](../notebooks/22_original_vs_frozen_validation.ipynb) | Frozen original-versus-ESCM-2.0 comparison |
| [05_real_camera_validation.ipynb](05_real_camera_validation.ipynb) | [23_real_data_full_sensor_comparison](../notebooks/23_real_data_full_sensor_comparison.ipynb) | Full sensor and sensory-fading validation |
| [06_additive_synapses_and_std.ipynb](06_additive_synapses_and_std.ipynb) | [29_joint_std_ei_calibration](../notebooks/29_joint_std_ei_calibration.ipynb) | Additive STD and inhibition calibration |
| [07_three_factor_plasticity.ipynb](07_three_factor_plasticity.ipynb) | [30_three_factor_stdp_vs_sensory_resources](../notebooks/30_three_factor_stdp_vs_sensory_resources.ipynb) | Three-factor plasticity versus sensory resources |
| [08_sensory_replenished_synapses.ipynb](08_sensory_replenished_synapses.ipynb) | [31_sensory_resource_analytical_calibration](../notebooks/31_sensory_resource_analytical_calibration.ipynb) | Analytical sensory-resource calibration |

## Complete lineage of the numbered notebook series

The source number is historical and **does not imply compatibility of models, timings, or readout windows**. This list is exhaustive for the 31 numbered notebooks on `refactor/python-packaging` at the time of review.

### Original implementation and input fidelity

| Original notebook | Experiment | Curated entry point |
| --- | --- | --- |
| [01_building_escm.ipynb](../notebooks/01_building_escm.ipynb) | Rebuild legacy model from recorded DVS | [01_legacy_and_parity](./01_legacy_and_parity.ipynb) |
| [02_diagnose_event_coordinates.ipynb](../notebooks/02_diagnose_event_coordinates.ipynb) | Compare decoded coordinate distributions | [01_legacy_and_parity](./01_legacy_and_parity.ipynb) |
| [03_legacy_vs_refactored.ipynb](../notebooks/03_legacy_vs_refactored.ipynb) | Legacy/refactor parity with shared reset correction | [01_legacy_and_parity](./01_legacy_and_parity.ipynb) |
| [04_moving_edge_baseline.ipynb](../notebooks/04_moving_edge_baseline.ipynb) | Legacy moving-edge baseline | [02_original_mechanisms](./02_original_mechanisms.ipynb) |

### Legacy mechanism tests

| Original notebook | Experiment | Curated entry point |
| --- | --- | --- |
| [05_mechanism_baseline.ipynb](../notebooks/05_mechanism_baseline.ipynb) | Isolate baseline persistence/inhibition/persistence gate | [02_original_mechanisms](./02_original_mechanisms.ipynb) |
| [06_mechanism_ablations.ipynb](../notebooks/06_mechanism_ablations.ipynb) | Ablate original mechanisms and test counter-free inhibition | [02_original_mechanisms](./02_original_mechanisms.ipynb) |
| [07_inhibitory_history_comparison.ipynb](../notebooks/07_inhibitory_history_comparison.ipynb) | Counter-based versus additive inhibition on 11 microprotocols | [02_original_mechanisms](./02_original_mechanisms.ipynb) |
| [08_moving_edge_inhibition_comparison.ipynb](../notebooks/08_moving_edge_inhibition_comparison.ipynb) | Multi-pixel moving-edge inhibition comparison | [02_original_mechanisms](./02_original_mechanisms.ipynb) |
| [09_edge_retention_sensitivity.ipynb](../notebooks/09_edge_retention_sensitivity.ipynb) | Edge retention sensitivity to timing, inhibition and radius | [02_original_mechanisms](./02_original_mechanisms.ipynb) |
| [10_spatial_excitation_inhibition.ipynb](../notebooks/10_spatial_excitation_inhibition.ipynb) | Spatial E/I kernel exploration | [02_original_mechanisms](./02_original_mechanisms.ipynb) |

### Numerical validity and mechanism derivations

| Original notebook | Experiment | Curated entry point |
| --- | --- | --- |
| [11_scheduler_independence_audit.ipynb](../notebooks/11_scheduler_independence_audit.ipynb) | Scheduler-independent Brian2 and NumPy audit; early run corrected after NaNs | [03_mathematics_and_numerics](./03_mathematics_and_numerics.ipynb) |
| [12_microcircuit_reference_audit.ipynb](../notebooks/12_microcircuit_reference_audit.ipynb) | Independent microcircuit reference and symbol-name fix | [03_mathematics_and_numerics](./03_mathematics_and_numerics.ipynb) |
| [13_self_excitation_convergence.ipynb](../notebooks/13_self_excitation_convergence.ipynb) | Autaptic assignment/addition/refractoriness convergence | [03_mathematics_and_numerics](./03_mathematics_and_numerics.ipynb) |
| [14_mechanism_comparison.ipynb](../notebooks/14_mechanism_comparison.ipynb) | Natural synaptic mechanisms against engineered persistence | [03_mathematics_and_numerics](./03_mathematics_and_numerics.ipynb) |
| [15_replacement_controls.ipynb](../notebooks/15_replacement_controls.ipynb) | Matched fading-versus-suppression controls | [03_mathematics_and_numerics](./03_mathematics_and_numerics.ipynb) |
| [16_mathematical_foundations_replacement.ipynb](../notebooks/16_mathematical_foundations_replacement.ipynb) | Exact membrane response and inhibition-driven termination | [03_mathematics_and_numerics](./03_mathematics_and_numerics.ipynb) |

### Spatial competition and frozen model

| Original notebook | Experiment | Curated entry point |
| --- | --- | --- |
| [17_five_pixel_competitive_replacement.ipynb](../notebooks/17_five_pixel_competitive_replacement.ipynb) | Five-neuron edge competition with label-aware construction | [04_frozen_escm20_benchmark](./04_frozen_escm20_benchmark.ipynb) |
| [18_unlabelled_spatial_competition.ipynb](../notebooks/18_unlabelled_spatial_competition.ipynb) | Homogeneous, unlabeled spatial grid | [04_frozen_escm20_benchmark](./04_frozen_escm20_benchmark.ipynb) |
| [19_spatial_generalization.ipynb](../notebooks/19_spatial_generalization.ipynb) | Held-out shapes and asynchronous timing | [04_frozen_escm20_benchmark](./04_frozen_escm20_benchmark.ipynb) |
| [20_spatial_inhibition_diagnostic.ipynb](../notebooks/20_spatial_inhibition_diagnostic.ipynb) | Measure geometric inhibition and extend outer radius | [04_frozen_escm20_benchmark](./04_frozen_escm20_benchmark.ipynb) |
| [21_transient_spatial_disinhibition.ipynb](../notebooks/21_transient_spatial_disinhibition.ipynb) | Experimental disinhibition (not approved baseline) | [04_frozen_escm20_benchmark](./04_frozen_escm20_benchmark.ipynb) |
| [22_original_vs_frozen_validation.ipynb](../notebooks/22_original_vs_frozen_validation.ipynb) | Legacy model vs frozen non-fading ESCM 2.0 | [04_frozen_escm20_benchmark](./04_frozen_escm20_benchmark.ipynb) |
| [23_real_data_full_sensor_comparison.ipynb](../notebooks/23_real_data_full_sensor_comparison.ipynb) | Recorded events; full sensor, sensory-fading reference | [05_real_camera_validation](./05_real_camera_validation.ipynb) |

### Additive autapses and short-term depression

| Original notebook | Experiment | Curated entry point |
| --- | --- | --- |
| [24_additive_autapse_validation.ipynb](../notebooks/24_additive_autapse_validation.ipynb) | Additive/refractory validation with sensory support controls | [06_additive_synapses_and_std](./06_additive_synapses_and_std.ipynb) |
| [25_escm20_additive_calibration.ipynb](../notebooks/25_escm20_additive_calibration.ipynb) | Calibrate additive autapse against approved fading reference | [06_additive_synapses_and_std](./06_additive_synapses_and_std.ipynb) |
| [26_escm20_current_balance_diagnostic.ipynb](../notebooks/26_escm20_current_balance_diagnostic.ipynb) | Measured current balance behind failed replacement | [06_additive_synapses_and_std](./06_additive_synapses_and_std.ipynb) |
| [27_std_replaces_sensory_support.ipynb](../notebooks/27_std_replaces_sensory_support.ipynb) | Conventional STD as a replacement for sensory support | [06_additive_synapses_and_std](./06_additive_synapses_and_std.ipynb) |
| [28_std_operating_point_generalization.ipynb](../notebooks/28_std_operating_point_generalization.ipynb) | STD operating point and held-out generalization | [06_additive_synapses_and_std](./06_additive_synapses_and_std.ipynb) |
| [29_joint_std_ei_calibration.ipynb](../notebooks/29_joint_std_ei_calibration.ipynb) | Joint STD and inhibition calibration | [06_additive_synapses_and_std](./06_additive_synapses_and_std.ipynb) |

### Modulated plasticity and sensory replenishment

| Original notebook | Experiment | Curated entry point |
| --- | --- | --- |
| [30_three_factor_stdp_vs_sensory_resources.ipynb](../notebooks/30_three_factor_stdp_vs_sensory_resources.ipynb) | Three-factor STDP versus sensory-replenished resources | [07_three_factor_plasticity](./07_three_factor_plasticity.ipynb) |
| [31_sensory_resource_analytical_calibration.ipynb](../notebooks/31_sensory_resource_analytical_calibration.ipynb) | Analytically guided SRR calibration and Brian2 comparison | [08_sensory_replenished_synapses](./08_sensory_replenished_synapses.ipynb) |

## Benchmark identities that must not be conflated

1. **Historical original ESCM:** fast legacy LIF, custom persistence gate `P`, counter-based inhibitory assignment, original event preprocessing and timestep. Several early notebook headings incorrectly call this “ESCM 2.0”; treat the equations, not the title, as authoritative.
2. **Frozen ESCM 2.0 (non-fading):** standard LIF, autaptic *current assignment*, homogeneous distance-dependent surround inhibition; experiments 18–22. This is **not** a sensory-depression or additive-autapse model.
3. **Approved ESCM 2.0 + sensory fading:** a later camera-driven decaying `support` variable modulates refreshed self-excitation. The real-data notebook 23 and calibration notebooks 24–31 use this benchmark in various forms. Preserve the exact source configuration and test windows before comparing scores across generations.
4. **Candidate families:** additive recurrence with support; conventional STD without support; three-factor weight plasticity; sensory-replenished synaptic resources. None is an interchangeable implementation of the frozen benchmark.

## Evidence handling

- **Keep successful and failed simulations.** The working geometry, temporal and timestep diagnostics in notebooks 17–23 and 25–31 are evidence. A failed held-out geometry is not a missing result.
- **Use matching baselines.** Compare models using the same camera events, stimulus onset, old-only/new-only controls, active-pixel threshold, readout windows, and numerical timestep. A score on five shapes is not directly comparable with a score on eight shapes without examining overlap.
- **Do not mistake inactivity for replacement.** The old representation must remain active in a matched old-only control, while the new-only control must persist; otherwise a replacement outcome is ineligible.
- **Respect experimental history.** In notebooks 11–12, corrected runs supersede earlier invalid Brian2–NumPy comparisons. Follow the actual corrections and warnings documented in those notebooks.
- **Preserve resource-update semantics.** The sensory-replenished mechanism adds excitation using resource availability before depletion and then consumes that resource. Brian2 scheduling/order warnings should be audited explicitly before using quantitative comparisons as independent verification.
- **No runs during restructuring.** The original outputs were copied, not recomputed. Notebook copies remain subject to dependencies, recorded-data availability, backend and environment requirements of their originating experiments.

## Legacy notebooks outside the numbered sequence

The root-level `ESCM_W.ipynb`, `SingleNeuronSim*.ipynb` and `utils/*.ipynb` are separate legacy interactive, camera-processing, EROS and quantitative evaluation workflows. They have **not** been deleted, migrated, or silently folded into the eight research entry points. Their absolute paths and original `ERO-SNN` working-directory assumptions require explicit cleanup in a separate migration.

## Preservation and next safe reduction

The present `research/` notebooks are **provenance-labelled, source-preserving entry points**. For a true cell-level consolidation, compare each original's numerical contract and outputs, move only compatible experimental cells into a common notebook, and rerun the resulting notebooks against the originals. Such merging must not happen by concatenating all code cells, because variable scope and Brian2 scheduling may change the computation. The original notebooks are the durable archive until that verification is complete.
