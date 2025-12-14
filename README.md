# Preference Stability – Clean-Room Demonstration

This repository provides a clean-room, self-contained demonstration of the **stability-level preference modeling** concept introduced in our NeurIPS 2023 AI Ethics workshop paper, *“Towards Stable Preferences for Stakeholder-aligned Machine Learning.”*

## Overview
The original study applied the stability-level model to real participant decision data collected in a kidney allocation context, which cannot be shared due to data sensitivity and research agreements.  

This demo abstracts away domain-specific features and instead uses **synthetic binary decision scenarios** to illustrate how preference stability is defined and measured.

## Stability Definition
An participants preferences are considered **stable** if, when presented with the *same decision scenario at different times*, they make the same choice.  
Stability is measured as the fraction of repeated scenarios in which the participant’s decision remains consistent.

## Synthetic Experiment
- Synthetic participants make binary decisions (Option A vs Option B).
- A subset of scenarios is repeated to test consistency.
- participants differ in their intrinsic consistency.
- Stability scores are computed per participant.

In this demo, “participants” refer to simulated decision-makers and do not correspond to real individuals.

## How to run

This demo has no external dependencies beyond NumPy.

```bash
python run_demo.py
```

## Results (Synthetic Demonstration)

The table below summarizes per-participant stability scores under two abstract participant types.

| Participant Type | Mean Stability | Std Dev | Count |
|-----------|----------------|---------|-------|
| Type 0 (more stable) | 0.954 | — | 89 |
| Type 1 (less stable) | 0.647 | — | 111 |
| **Overall** | **0.783** | **0.195** | **200** |

Stability is defined as the fraction of repeated scenarios for which a participant made the same decision.

<details>
<summary>Raw console output</summary>

```text
Synthetic Stability Demo
------------------------
Overall mean stability: 0.783
Overall std stability:  0.195
Min / Max:              0.200 / 1.000

By participant type:
  Type 0 (more stable)   mean=0.954  n=89
  Type 1 (less stable)   mean=0.647  n=111
 ```
 </details>

This confirms that the stability metric responds predictably to controlled inconsistency in repeated identical scenarios.


## Reference

This demo is based on the methodology introduced in the following paper:

*Haleema Sheraz* et al.,  
*Towards Stable Preferences for Stakeholder-aligned Machine Learning*  
(NeurIPS 2023 Workshop on AI Ethics)

Paper: https://neurips.cc/virtual/2023/77051

The code in this repository is **not** a reproduction of the paper’s experiments.  
Instead, it provides a clean-room, synthetic demonstration of the core stability concept, without using real participant data or domain-specific features.



