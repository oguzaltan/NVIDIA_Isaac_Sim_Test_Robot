# Phase 6: Reintroduce Context Knowledge Properly

## Goal

Bring back the strongest thesis contribution: structured context knowledge. Compare state-only policies against context-aware policies cleanly.

Estimated time: 2 to 4 weeks.

## Sources

- Ray caster: https://isaac-sim.github.io/IsaacLab/main/source/overview/core-concepts/sensors/ray_caster.html
- Sensor overview: https://isaac-sim.github.io/IsaacLab/main/source/overview/core-concepts/sensors/index.html
- Camera and tiled rendering: https://isaac-sim.github.io/IsaacLab/main/source/overview/core-concepts/sensors/camera.html
- Add sensors on a robot: https://isaac-sim.github.io/IsaacLab/main/source/tutorials/04_sensors/add_sensors_on_robot.html
- Debugging/training guide: https://isaac-sim.github.io/IsaacLab/main/source/overview/reinforcement-learning/training_guide.html

## Representation Options

### A. Thesis-style context

Use map-like channels:

- building map
- road map
- observer/target position map
- rotation or agent-centered map
- estimated target map if useful

This gives the cleanest continuity with the thesis.

### B. Isaac-native context

Use embodied sensing:

- ray-cast hit summaries
- local occupancy tensors
- depth-like geometric observations
- RGB/depth cameras later

This gives the stronger embodied-robotics story, but costs more engineering and compute.

## Recommended Order

1. Lock a state-only baseline.
2. Add the smallest useful thesis-style context signal.
3. Add or compare ray/occupancy context.
4. Add camera/depth only when the rest is stable.

## Do

- Freeze rewards and reset logic before adding context.
- Start with one compact context signal.
- Decide whether context is a vector, small tensor, or CNN input.
- Run state-only versus state-plus-context ablations.
- Track behavior metrics, not only reward.

## Metrics

- tracking/localization error
- visibility or occlusion rate
- collision rate
- time-to-loss-of-track
- target evasion distance
- performance on unseen layouts

## Thesis Link

Your thesis found that context and state observations together can outperform context-only setups. Preserve that lesson: compare state-only, context-only if useful, and state-plus-context instead of jumping straight to a large CNN.

## Exit Gate

You can move on when:

- A state-only baseline is stable.
- At least one context-aware variant is stable.
- You have an ablation table or comparison note.
- You can explain exactly what the context representation adds.

## Avoid

- Adding every context channel at once.
- Using a CNN before the representation justifies spatial processing.
- Changing reward, policy architecture, and observations in the same ablation.
