# run_demo.py
#
# Clean-room synthetic demonstration of preference stability.
# This script simulates agents making repeated binary decisions
# and measures how consistently they respond to identical scenarios.

import numpy as np


def simulate_agents(
    n_agents=200,
    n_scenarios=50,
    n_repeated=10,
    flip_prob_stable=0.05,
    flip_prob_unstable=0.35,
    seed=0
):
    """
    Simulate agents making binary decisions on repeated scenarios.

    Each agent is assigned an abstract 'stability type' that controls
    how likely they are to change their decision when the same scenario
    is shown again.

    Returns:
        scores (np.ndarray): stability score per agent in [0, 1]
        agent_type (np.ndarray): abstract agent type (0 = more stable, 1 = less stable)
    """

    # Reproducible randomness
    rng = np.random.default_rng(seed)

    # Assign agents to abstract stability types.
    # These types have no real-world semantics and exist only to
    # control how often agents flip their decisions.
    agent_type = rng.integers(0, 2, size=n_agents)  # 0 = more stable, 1 = less stable

    # Create a pool of scenario identifiers
    scenarios = np.arange(n_scenarios)

    # Select a subset of scenarios that will be repeated
    repeated = rng.choice(scenarios, size=n_repeated, replace=False)

    stability_scores = []

    # Simulate decisions for each agent
    for a in range(n_agents):
        # More stable agents flip less often on repeated exposure
        flip_prob = (
            flip_prob_stable
            if agent_type[a] == 0
            else flip_prob_unstable
        )

        consistent = 0
        total = 0

        # Evaluate consistency on repeated scenarios
        for s in repeated:
            # Initial decision: Option A (0) or Option B (1)
            base_choice = rng.integers(0, 2)

            # On the second exposure, the agent may flip
            flipped = rng.random() < flip_prob
            second_choice = base_choice if not flipped else 1 - base_choice

            # Count whether the decision stayed the same
            if base_choice == second_choice:
                consistent += 1
            total += 1

        # Stability = fraction of repeated scenarios with consistent decisions
        stability_scores.append(consistent / total)

    # Convert to NumPy array once all agents are processed
    scores = np.array(stability_scores)

    return scores, agent_type


if __name__ == "__main__":
    # Run the synthetic experiment
    scores, agent_type = simulate_agents()

    # Overall summary statistics
    print("Synthetic Stability Demo")
    print("------------------------")
    print(f"Overall mean stability: {scores.mean():.3f}")
    print(f"Overall std stability:  {scores.std():.3f}")
    print(f"Min / Max:              {scores.min():.3f} / {scores.max():.3f}")

    # Breakdown by abstract agent type
    stable_scores = scores[agent_type == 0]
    unstable_scores = scores[agent_type == 1]

    print("\nBy agent type (abstract):")
    print(f"  Type 0 (more stable)   mean={stable_scores.mean():.3f}  n={len(stable_scores)}")
    print(f"  Type 1 (less stable)   mean={unstable_scores.mean():.3f}  n={len(unstable_scores)}")
