# Phase 2: Isaac Lab Environment Anatomy

## Goal

Understand how Isaac Lab turns simulation into an RL task: scene setup, actions, physics stepping, observations, rewards, dones, resets, registration, wrappers, and training scripts.

Estimated time: 5 to 7 days.

## Sources

- Task workflows: https://isaac-sim.github.io/IsaacLab/v2.3.0/source/overview/core-concepts/task_workflows.html
- Direct RL environment tutorial: https://isaac-sim.github.io/IsaacLab/v2.3.0/source/tutorials/03_envs/create_direct_rl_env.html
- Registering an environment: https://isaac-sim.github.io/IsaacLab/v2.3.0/source/tutorials/03_envs/register_rl_env_gym.html
- Training with an RL agent: https://isaac-sim.github.io/IsaacLab/v2.3.0/source/tutorials/03_envs/run_rl_training.html
- Modifying a direct environment: https://isaac-sim.github.io/IsaacLab/v2.3.0/source/tutorials/03_envs/modify_direct_rl_env.html
- Project structure: https://isaac-sim.github.io/IsaacLab/v2.3.0/source/overview/own-project/project_structure.html

## Learn

- `DirectRLEnv` and `DirectRLEnvCfg`
- `@configclass`
- `_setup_scene`
- `_pre_physics_step` and `_apply_action`
- `_get_observations`
- `_get_rewards`
- `_get_dones`
- `_reset_idx`
- `gym.register()` and training config entry points

## Do

- Run the direct cartpole tutorial.
- Modify one reward term and confirm training behavior changes.
- Modify one observation term and confirm the task still runs.
- Trace one task from task name to `gym.register()` to environment class to training config.
- Run one task interactively, headless, and headless with video if practical.

## Thesis Mapping

| Thesis Environment Piece | Isaac Lab Location |
| --- | --- |
| initialization | config class plus `_setup_scene` |
| action interpretation | `_pre_physics_step`, `_apply_action` |
| observation space | `_get_observations` |
| reward function | `_get_rewards` |
| termination criteria | `_get_dones` |
| scenario reset | `_reset_idx` |
| trainer setup | RL backend config and wrapper |

## Write

- A one-page mapping from your thesis environment functions to the Isaac Lab lifecycle.
- A short note explaining why direct workflow is the first fit for your thesis.

## Exit Gate

You can move on when:

- You have modified and run a direct task.
- You can explain the full action -> physics -> observation/reward/done/reset loop.
- You can trace task registration without guessing.

## Avoid

- Reading tutorials without running them.
- Moving to MARL before you understand single-agent lifecycle.
- Treating task registration as magic.
