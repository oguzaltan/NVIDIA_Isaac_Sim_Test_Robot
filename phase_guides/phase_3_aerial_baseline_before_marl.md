# Phase 3: Aerial Baseline Before MARL

## Goal

Learn from a working aerial task before building your thesis task. The decision you need from this phase is the first action and observation abstraction for your research.

Estimated time: 1 to 2 weeks.

## Sources

- Isaac Lab environments list: https://isaac-sim.github.io/IsaacLab/v2.3.0/source/overview/environments.html
- Quadcopter task source: https://github.com/isaac-sim/IsaacLab/blob/v2.3.0/source/isaaclab_tasks/isaaclab_tasks/direct/quadcopter/quadcopter_env.py
- IMU sensor: https://isaac-sim.github.io/IsaacLab/main/source/overview/core-concepts/sensors/imu.html
- Ray caster: https://isaac-sim.github.io/IsaacLab/main/source/overview/core-concepts/sensors/ray_caster.html
- RL framework comparison: https://isaac-sim.github.io/IsaacLab/main/source/overview/reinforcement-learning/rl_frameworks.html
- Debugging/training guide: https://isaac-sim.github.io/IsaacLab/main/source/overview/reinforcement-learning/training_guide.html

## Learn

- How the built-in quadcopter task applies actions.
- Which observations are state-like, sensor-like, or privileged.
- How reset validity affects aerial stability.
- Why rendering and cameras change training speed.

## Do

- Run `Isaac-Quadcopter-Direct-v0` or the current equivalent task.
- Inspect its action space, observation space, reward, and reset logic.
- Run it interactively and headless.
- Test a few initial pose perturbations.
- Add or simulate mild action/observation noise if easy.

## Decide

Choose your first thesis-task control abstraction:

- preferred: horizontal velocity plus yaw/heading command, or waypoint delta
- acceptable: attitude-rate/body-rate command
- postpone: raw motor thrust, unless low-level control is part of the paper

Choose your first observation abstraction:

- state: relative position/velocity, observer pose, target estimate
- compact context: line-of-sight flag, ray summary, local occupancy patch
- postpone: RGB/depth camera observations

## Write

- A one-page baseline memo: action interface, observation interface, what to postpone, stability issues noticed.

## Thesis Link

Your thesis is about pursuit, evasion, localization, and context. Low-level motor stabilization can hide that signal. Keep the first aerial task high-level enough to study the thesis question.

## Exit Gate

You can move on when:

- The stock aerial task runs.
- You know what actions and observations it uses.
- You have chosen the first control and sensing abstraction for Phase 4.

## Avoid

- Treating a stock task as your research baseline.
- Starting with cameras.
- Switching control level and task logic at the same time.
