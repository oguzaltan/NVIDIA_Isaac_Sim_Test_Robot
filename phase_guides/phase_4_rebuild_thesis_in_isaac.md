# Phase 4: Rebuild the Thesis in Isaac, but Keep It Simple

## Goal

Build the first real thesis bridge: one observer drone tracks one scripted ground target in a simple obstacle/urban scene.

Estimated time: 1 to 2 weeks.

## Sources

- Direct RL environment tutorial: https://isaac-sim.github.io/IsaacLab/v2.3.0/source/tutorials/03_envs/create_direct_rl_env.html
- Modify direct environment: https://isaac-sim.github.io/IsaacLab/v2.3.0/source/tutorials/03_envs/modify_direct_rl_env.html
- Add sensors on a robot: https://isaac-sim.github.io/IsaacLab/main/source/tutorials/04_sensors/add_sensors_on_robot.html
- Visualization markers: https://isaac-sim.github.io/IsaacLab/main/source/how-to/draw_markers.html
- Recording video: https://isaac-sim.github.io/IsaacLab/main/source/how-to/record_video.html
- Wrapping environments: https://isaac-sim.github.io/IsaacLab/main/source/how-to/wrap_rl_env.html

## Build

- observer drone
- scripted ground target
- simple buildings or block obstacles
- boundary conditions
- collision checks
- line-of-sight or occlusion logic
- tracking reward
- rollout visualization

Do not add learned target, full procedural city generation, or RGB cameras yet.

## Task Spec

Write this before coding:

- state variables
- action definition
- observation definition
- reward terms
- termination conditions
- reset distribution
- target script
- evaluation scenarios

## First Observation Set

Use privileged state plus one compact context signal:

- relative target position or estimated relative target position
- relative velocity
- observer pose/speed
- line-of-sight boolean or visibility score
- obstacle distance, ray summary, or local occupancy patch

## Reward Start Point

Keep it explainable:

- reward for maintaining visibility or reducing tracking/localization error
- penalty for losing line of sight
- penalty for collision or invalid state
- small action smoothness penalty only if needed

## Do

- Build scene and scripted target before training.
- Add debug markers for observer, target, line of sight, and failure states.
- Run scripted and random-action rollouts.
- Verify rewards, dones, and resets visually.
- Train the observer only after the no-learning rollouts make sense.

## Thesis Link

This phase preserves the thesis ideas of tracking, occlusion, urban context, and scenario evaluation while removing the learned opponent and rich context stack.

## Exit Gate

You can move on when:

- The custom task runs reliably.
- Visibility/occlusion logic is visibly correct.
- Rewards and termination reasons match rollouts.
- The observer learns a nontrivial behavior in at least one simple scenario.

## Avoid

- Adding a learned target too early.
- Writing complex reward logic before watching rollouts.
- Treating map context and camera perception as the same problem.
