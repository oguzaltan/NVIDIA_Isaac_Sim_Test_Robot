# Isaac Sim and Isaac Lab Roadmap for Thesis-to-Drone MARL

## Purpose

This roadmap turns your master's thesis, [Masters_Thesis_Oguz_Altan.pdf](Masters_Thesis_Oguz_Altan.pdf), into a staged NVIDIA Isaac Sim and Isaac Lab learning plan. The target is not to "learn all of Isaac"; it is to rebuild your thesis ideas in a physics-based, publishable robot-learning workflow.

Your thesis, *Tracking and Evasion using Co-Training with Context Knowledge*, already gives you the research core:

- co-training between a tracking UAV observer and an evading ground target
- PPO-based multi-agent reinforcement learning
- urban maps with buildings and roads
- procedural map generation, including Voronoi-based layouts
- context knowledge encoded as map-like observations
- CNN plus actor-critic policy architecture
- occlusion, building collision, boundary logic, adaptive target speed, and scenario-based evaluation

The Isaac version should preserve those ideas, but introduce 3D scenes, physics, sensors, and reproducible robot-learning experiments gradually.

## Version Baseline

As of 2026-05-30, use these rules:

- Use Isaac Sim 5.1.0 or the current GA release for real work. The `latest` Isaac Sim docs currently expose Isaac Sim 6.0 Early Developer Release pages, which NVIDIA marks as incomplete.
- Use Isaac Lab stable 2.3.x documentation/source unless you intentionally decide to test Isaac Lab 3.0 beta or `develop`.
- Match the Isaac Lab docs, source branch/tag, Python version, and Isaac Sim version. Isaac Sim 5.x uses Python 3.11; Isaac Sim 4.x used Python 3.10.
- For your Windows machine, prefer native Windows Isaac Sim/Isaac Lab setup first. Use WSL for shell habits and notes, not for mixing Python environments with the Windows GUI install.
- Record the exact Isaac Sim version, Isaac Lab commit/tag, GPU driver, Python version, RL backend, and task name for every serious experiment.

Key setup sources:

- Isaac Sim 5.1 docs: https://docs.isaacsim.omniverse.nvidia.com/5.1.0/index.html
- Isaac Sim download page: https://docs.isaacsim.omniverse.nvidia.com/5.1.0/installation/download.html
- Isaac Lab installation: https://isaac-sim.github.io/IsaacLab/v2.3.0/source/setup/installation/index.html
- Isaac Lab quickstart: https://isaac-sim.github.io/IsaacLab/v2.3.0/source/setup/quickstart.html

## Technical Direction

Use Isaac Sim for scenes, USD assets, rendering, sensors, physics inspection, and robot setup.

Use Isaac Lab for RL task code, vectorized environments, reset/reward/observation logic, training scripts, wrappers, logging, and curriculum/randomization.

Use a direct workflow first:

- `DirectRLEnv` for single-agent bridge tasks
- `DirectMARLEnv` once the evading target becomes a learned agent

Why: Isaac Lab's direct workflow keeps rewards, observations, resets, dones, and action logic in one environment class. That matches your thesis-style custom environment better than the manager workflow at the beginning.

Start with the built-in Crazyflie/quadcopter task as your aerial reference. Do not start with a custom drone asset, raw RGB cameras, or raw motor control unless they are required by a research question.

## Research Bridge

Build the thesis-to-Isaac migration in this order:

1. single drone hover/navigation baseline
2. drone observer versus scripted ground target
3. drone observer versus learned ground target
4. drone observer versus learned drone target
5. larger MARL variants only after the two-agent case is stable

Your first serious milestone should be:

> A single observer drone in Isaac Lab learns to maintain line of sight to a scripted ground target in a simple urban obstacle scene, using state observations plus one compact context signal.

That milestone is close to the thesis, uses Isaac meaningfully, and avoids early multi-agent instability.

## Phase Overview

Each phase has a detailed guide in [phase_guides](phase_guides).

| Phase | Goal | Main Sources | Exit Gate |
| --- | --- | --- | --- |
| 0. Setup and orientation | Install correctly and understand the Isaac stack | Isaac Sim docs, Isaac Lab installation, quickstart, project structure | Isaac Sim launches, one Isaac Lab task trains, and you can explain Sim vs Lab vs RL backend |
| 1. Isaac Sim fundamentals | Learn USD stages, prims, physics, assets, and scene scripting | Isaac Sim Python scripting, robot setup, import/export, USD primer | You can create, save, inspect, and script a simple scene |
| 2. Isaac Lab environment anatomy | Learn direct task lifecycle | Task workflows, direct RL tutorial, registration, training | You modify a stock direct task and map its methods to thesis environment logic |
| 3. Aerial baseline | Learn from the built-in quadcopter task | Quadcopter source, environments list, IMU, ray caster, training guide | You know the first action and observation abstraction for your research task |
| 4. Thesis bridge task | Build observer drone versus scripted ground target | Direct RL tutorial, modify direct env, sensors, markers, video, wrappers | Custom task runs, visibility logic works, observer learns in a simple scene |
| 5. True MARL | Replace scripted target with learned target | `DirectMARLEnv`, multi-agent examples, RL framework comparison | Two-agent training runs without obvious environment bugs or immediate collapse |
| 6. Context knowledge | Reintroduce map/context observations | Ray caster, camera/sensors, tiled rendering, training guide | State-only and context-aware policies are compared cleanly |
| 7. Drone target | Convert target from ground agent to drone | add robot, import assets, articulation config, performance, curriculum | First drone-vs-drone task exists and is stable enough for controlled research |

## Eight-Week Skeleton

Use this as a pacing estimate, not as a rigid schedule.

| Week | Focus | Output |
| --- | --- | --- |
| 1 | setup, stack, first stock task | verified install notes and one training run |
| 2 | Isaac Sim scene/asset basics | simple USD scene plus obstacle-spawning script |
| 3 | Isaac Lab direct task anatomy | modified stock task and lifecycle mapping |
| 4 | quadcopter baseline | action/observation decision memo |
| 5 | scripted-target thesis bridge | custom rollout with visibility/reward/debug markers |
| 6 | observer training | first learning result against scripted ground target |
| 7 | `DirectMARLEnv` learned target | small two-agent experiment and failure-mode log |
| 8 | context ablation plan | state-only vs context-aware experiment design |

The drone-vs-drone phase may take longer than this skeleton. Treat it as the start of research iteration, not the end of learning.

## Thesis-to-Isaac Mapping

| Thesis Concept | Isaac Equivalent | Recommendation |
| --- | --- | --- |
| 2D generated maps | USD scenes with obstacles, roads, and semantic metadata | start with simple geometry, procedural generation later |
| observer UAV | Crazyflie/quadcopter-like observer | use high-level or mid-level control first |
| ground target | scripted then learned ground agent | keep this as the first bridge before drone target |
| co-training | `DirectMARLEnv` plus supported MARL backend | only after scripted-target task is stable |
| map context channels | map tensors, ray-cast summaries, occupancy tensors, or camera/depth | preserve thesis-style context first, then compare Isaac-native sensing |
| CNN context branch | custom policy/network input branch | add after state-only baseline works |
| occlusion | ray tests, line-of-sight checks, or geometry queries | implement explicitly and visualize before training |
| road/building rules | task logic plus USD scene structure | keep rules debuggable and logged |
| PPO in RLlib | Isaac Lab supported PPO flow, likely `rl_games` or `skrl` first | do not copy hyperparameters blindly |

## Experiment Ladder

Do not skip steps.

1. Stock Isaac Lab task trains.
2. Modified stock task still trains.
3. Stock quadcopter task runs and is understood.
4. Scripted observer-target rollout works without learning.
5. Observer learns against scripted target in open space.
6. Same task works with buildings and line-of-sight logic.
7. Same task works over multiple layouts.
8. Learned target is added through `DirectMARLEnv`.
9. State-only policy is compared against state-plus-context.
10. Thesis-style map context is compared against ray/occupancy context.
11. Ground target becomes drone target.
12. More agents, communication, partial observability, or sim-to-real constraints are added.

## Metrics for Paper-Ready Work

Track more than reward:

- tracking error or localization error
- visibility rate and occlusion rate
- time-to-loss-of-track
- collision count and collision rate
- boundary violations and invalid resets
- episode length and termination reason
- target distance traveled or evasion quality
- success on seen versus unseen map layouts
- qualitative rollout videos or trajectory plots

For a paper, your central claim should not be "I ported the thesis to Isaac." A stronger claim is:

- context-aware pursuit-evasion policies transfer from abstract 2D MARL into physics-based embodied simulation
- structured map context can be compared against Isaac-native sensing
- staged co-training prevents early collapse while preserving adversarial behavior
- urban scene variation improves generalization across held-out layouts

## Main Learning Sources

Official NVIDIA and Isaac sources:

- Isaac Sim 5.1 documentation: https://docs.isaacsim.omniverse.nvidia.com/5.1.0/index.html
- Isaac Sim Python scripting: https://docs.isaacsim.omniverse.nvidia.com/5.1.0/python_scripting/index.html
- Isaac Sim robot setup: https://docs.isaacsim.omniverse.nvidia.com/5.1.0/robot_setup/index.html
- Isaac Lab documentation: https://isaac-sim.github.io/IsaacLab/v2.3.0/index.html
- Isaac Lab task workflows: https://isaac-sim.github.io/IsaacLab/v2.3.0/source/overview/core-concepts/task_workflows.html
- Direct RL environment tutorial: https://isaac-sim.github.io/IsaacLab/v2.3.0/source/tutorials/03_envs/create_direct_rl_env.html
- Isaac Lab environments list: https://isaac-sim.github.io/IsaacLab/v2.3.0/source/overview/environments.html
- Isaac Lab RL framework comparison: https://isaac-sim.github.io/IsaacLab/main/source/overview/reinforcement-learning/rl_frameworks.html
- Isaac Lab debugging/training guide: https://isaac-sim.github.io/IsaacLab/main/source/overview/reinforcement-learning/training_guide.html

Useful but secondary references:

- OpenUSD: https://openusd.org/release/index.html
- NVIDIA USD overview: https://developer.nvidia.com/usd
- Isaac Lab GitHub: https://github.com/isaac-sim/IsaacLab
- OmniDrones: https://github.com/btx0424/OmniDrones
- Aerial Gym Simulator: https://github.com/ntnu-arl/aerial_gym_simulator

Use community drone projects for ideas, not as your base implementation. Isaac version compatibility can consume time quickly.

## What Not To Do First

- do not start with custom drone import
- do not start with raw RGB cameras
- do not start with raw motor thrust unless low-level flight control is your research topic
- do not start with full drone-vs-drone MARL
- do not trust reward curves before visual rollout checks
- do not mix custom asset, custom perception, and multi-agent training in one first experiment

## Immediate Next Actions

1. Install Isaac Sim and Isaac Lab using version-matched docs.
2. Run one stock Isaac Lab training command.
3. Complete the direct RL environment tutorial.
4. Run and inspect the stock quadcopter task.
5. Write the task spec for observer drone versus scripted ground target.
6. Build that task with state observations and one compact context signal.
