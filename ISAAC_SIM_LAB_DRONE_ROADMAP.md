# Isaac Sim and Isaac Lab Roadmap for Thesis-to-Drone MARL

## Purpose

This document gives you a concrete path from your master's thesis to a working NVIDIA Isaac Sim and Isaac Lab research workflow for multi-agent reinforcement learning with drones.

It is based on your thesis, [Masters_Thesis_Oguz_Altan.pdf](Masters_Thesis_Oguz_Altan.pdf), which already contains a strong RL foundation:

- zero-sum co-training of an observer and an evading target
- PPO-based training in RLlib
- urban map generation with Voronoi-based structure and roads
- context knowledge encoded as map channels
- CNN + actor-critic integration
- occlusion, collision, boundary logic, and target speed adaptation

The key point is this: you do not need to "learn Isaac" in the abstract. You need to learn the parts of Isaac that replace the abstractions you already built in Python.

## Executive Summary

Your best path is:

1. Learn Isaac Sim as a scene, asset, and physics tool.
2. Learn Isaac Lab as the RL task and training layer.
3. Use the direct workflow, not the manager workflow, for your first custom thesis-style environment.
4. Start with a single quadcopter task before touching multi-agent training.
5. Rebuild your thesis in stages: scripted target first, learned target second, full drone-vs-drone last.
6. Start with state observations and simple geometric context first; only later add rich visual perception.

If you try to jump directly to full drone-vs-drone MARL with image observations, custom assets, and complex urban scenes, you will burn time on platform issues instead of research.

## Detailed Phase Guides

The roadmap below stays useful as the high-level map. The detailed working manuals for each phase are here:

1. [phase_guides/phase_0_setup_and_orientation.md](phase_guides/phase_0_setup_and_orientation.md)
2. [phase_guides/phase_1_isaac_sim_fundamentals.md](phase_guides/phase_1_isaac_sim_fundamentals.md)
3. [phase_guides/phase_2_isaac_lab_environment_anatomy.md](phase_guides/phase_2_isaac_lab_environment_anatomy.md)
4. [phase_guides/phase_3_aerial_baseline_before_marl.md](phase_guides/phase_3_aerial_baseline_before_marl.md)
5. [phase_guides/phase_4_rebuild_thesis_in_isaac.md](phase_guides/phase_4_rebuild_thesis_in_isaac.md)
6. [phase_guides/phase_5_convert_to_true_multi_agent_training.md](phase_guides/phase_5_convert_to_true_multi_agent_training.md)
7. [phase_guides/phase_6_reintroduce_context_knowledge.md](phase_guides/phase_6_reintroduce_context_knowledge.md)
8. [phase_guides/phase_7_move_from_ground_target_to_drone_target.md](phase_guides/phase_7_move_from_ground_target_to_drone_target.md)

If you want to work phase-by-phase, open the matching guide and treat its exit criteria as the gate to the next phase.

## What Your Thesis Already Gives You

Your thesis is not a blank starting point. It already defines a research template that maps well into Isaac Lab.

### Thesis Core Structure

- Observer agent and target agent are trained in opposition.
- PPO is the baseline optimizer.
- Reward logic is tightly coupled to task logic.
- Context enters the policy as structured map-like inputs.
- Urban structure matters because of occlusion, roads, and buildings.
- Evaluation is scenario-based, not just reward-based.

### What Changes in Isaac

Your original setup is mostly a 2D task with fixed-altitude assumptions and custom environment logic. Isaac changes the substrate:

- 2D map world becomes a 3D USD scene.
- custom Python kinematics become simulated physics and sensors
- image-like context channels can come from maps, ray casting, or cameras
- one custom RLlib environment becomes a vectorized Isaac Lab task
- scripted world constraints become USD assets plus environment logic

### What You Should Keep

- the co-training idea
- the competitive reward structure
- the scenario-driven evaluation mindset
- the use of structured context, not only raw state
- the procedural environment variation idea

### What You Should Redesign

- action space: do not start with raw motor commands
- sensing: do not start with full RGB vision
- map representation: do not assume 2D image maps must remain the final observation format
- hyperparameters: do not copy RLlib PPO settings directly into Isaac Lab and expect them to transfer

## Recommended Technical Direction

### Primary Platform Choice

Use Isaac Sim plus Isaac Lab, with Isaac Lab as the actual training framework.

- Isaac Sim is where USD scenes, robot assets, sensors, and physics live.
- Isaac Lab is where RL environments, vectorization, wrappers, and training scripts live.

### Environment Design Choice

For your first real custom task, prefer `DirectMARLEnv`.

Why:

- your thesis logic is tightly coupled across observations, rewards, dones, and reset logic
- direct-style tasks are closer to the custom Python environments you already understand
- official Isaac Lab docs explicitly position `DirectRLEnv` and `DirectMARLEnv` as the most familiar path for users coming from traditional custom RL environment code

You can learn manager-based environments later, but they are not the shortest path from your thesis.

### Robot Choice

Use the built-in Crazyflie quadcopter task and asset first.

Why:

- Isaac Lab already includes a quadcopter environment based on Crazyflie
- this gives you a working aerial baseline before you fight custom asset or controller problems
- it lets you learn Isaac Lab around a drone, not around cartpole forever

### RL Library Choice

Start with PPO using an Isaac Lab-supported training path. Then branch later if your MARL needs outgrow the default setup.

Practical recommendation:

- start with the built-in PPO-friendly training flow used by Isaac Lab examples
- keep your first custom task compatible with standard Isaac Lab wrappers
- only later decide whether you need more specialized multi-agent algorithms or a custom training library integration

Reason:

- your thesis already uses PPO successfully
- the biggest early risk is environment design, not optimizer novelty
- specialized MARL algorithms are useful later, but not necessary to prove the Isaac migration

## The Best Research Bridge

Do not jump straight from your thesis to drone-vs-drone 6-DoF pursuit-evasion.

Instead, use this bridge:

1. single drone hover and navigation
2. drone observer versus scripted ground target in urban scene
3. drone observer versus learned ground target
4. drone observer versus learned drone target

This preserves your thesis structure while increasing Isaac complexity in a controlled way.

That middle bridge step is important. Your thesis target is a ground platform affected by buildings and roads. That is a clean first transfer because it preserves most of the logic you already validated.

## Phased Roadmap

### Phase 0: Setup and Orientation

#### Goal

Get Isaac Sim and Isaac Lab running cleanly and understand the ecosystem at a high level.

#### Time

2 to 4 days

#### Read

- Isaac Sim overview and quick install
- Isaac Sim basic usage tutorial
- Isaac Lab homepage and quickstart
- Isaac Lab ecosystem and project structure pages

#### Do

- install a stable Isaac Sim workstation build, not the bleeding-edge developer version
- clone Isaac Lab separately in a clean workspace for active development
- run one stock Isaac Lab training example end-to-end
- open your existing [test_robot_nvidia.usd](test_robot_nvidia.usd) in Isaac Sim only to inspect the stage tree, physics prims, and USD structure

#### Deliverables

- one working Isaac Sim GUI launch
- one working Isaac Lab training command
- one short personal note answering: what belongs to Isaac Sim, what belongs to Isaac Lab, what belongs to the RL library

#### Stop Condition

Do not move on until you can explain, in your own words, the difference between USD scene authoring and Isaac Lab task code.

### Phase 1: Learn Isaac Sim Fundamentals

#### Goal

Become comfortable with scene construction, USD concepts, and physics/sensor inspection.

#### Time

4 to 7 days

#### Read

- Isaac Sim Python scripting overview
- USD basics and NVIDIA USD primer
- Isaac Sim robot setup and importer/exporter pages

#### Do

- create a simple scene with ground, lights, and a few rigid obstacles
- load a robot asset and inspect articulation and physics properties
- move objects, set transforms, and save a USD stage
- learn how prim paths, references, and scene hierarchy work
- inspect collision meshes versus visual meshes

#### Minimum Experiments

- spawn a cube wall procedurally
- save and reload the stage
- script a moving object and observe collisions
- add one sensor or debug visualization element

#### Why This Matters for Your Thesis

Your thesis used generated maps as the environmental substrate. In Isaac, the substrate becomes a USD scene. If you do not understand how the scene is built, every later RL bug becomes harder to diagnose.

### Phase 2: Learn Isaac Lab Environment Anatomy

#### Goal

Understand how Isaac Lab tasks are structured, stepped, reset, and trained.

#### Time

5 to 7 days

#### Read

- Isaac Lab task design workflows
- direct RL environment tutorial
- environment registration tutorial
- RL training tutorial
- debugging and training guide

#### Do

- reproduce the direct cartpole tutorial
- identify where scene setup, rewards, observations, resets, dones, and actions are implemented
- change one reward term and confirm the learning curve changes
- change one observation term and confirm the environment still trains

#### Deliverables

- a tiny modified stock task that you changed yourself
- a one-page note mapping these Isaac Lab methods to your thesis environment functions:
  - `_setup_scene`
  - `_get_observations`
  - `_get_rewards`
  - `_get_dones`
  - `_reset_idx`
  - `_pre_physics_step`
  - `_apply_action`

#### What You Are Really Learning

You are learning how to rewrite your thesis environment into Isaac Lab's control loop.

### Phase 3: Aerial Baseline Before MARL

#### Goal

Gain confidence with a drone task in Isaac Lab before introducing multi-agent complexity.

#### Time

1 to 2 weeks

#### Read

- Isaac Lab environment list for the quadcopter task
- IMU sensor docs
- ray caster docs
- RL framework comparison page

#### Do

- run the built-in quadcopter or Crazyflie-style task
- inspect the action space and observation space
- identify whether the task uses low-level thrust or a more abstract control interface
- log what sensor-like signals are already available

#### Minimum Experiments

- hover at a fixed point
- move to a waypoint
- perturb the initial pose and recover
- add mild observation noise or action noise
- run headless and compare training speed with GUI mode

#### Deliverables

- one stable single-agent hover or waypoint result
- one short note on which action abstraction you want for research stage 1:
  - high-level velocity commands
  - attitude-rate commands
  - raw motor thrusts

#### Recommendation

For your first custom thesis-style transfer, use high-level or mid-level control, not raw motor control.

Reason:

- your thesis is about tracking, evasion, and context-aware decision making
- raw motor commands add low-level flight stabilization difficulty that will hide the real research signal

### Phase 4: Rebuild the Thesis in Isaac, but Keep It Simple

#### Goal

Create a simplified custom environment that preserves your thesis logic while minimizing unnecessary new variables.

#### Time

1 to 2 weeks

#### Task Definition

Start with:

- one aerial observer
- one scripted target on the ground
- simple urban obstacles in USD
- no learned target yet
- no RGB camera yet

#### What to Implement

- observer movement in a simplified action space
- target motion with a scripted evasive or road-following policy
- episode reset logic
- boundary conditions
- building occlusion logic
- line-of-sight or ray-based visibility check
- reward shaped around tracking quality

#### Thesis Components to Port First

- estimation-based observer objective
- target visibility and occlusion
- context dependence due to buildings
- scenario-based evaluation

#### Thesis Components to Delay

- full map-channel CNN stack
- learned target policy
- full procedural city generator inside Isaac
- camera-based perception

#### Important Design Choice

Use privileged state and simple geometric context first.

Examples:

- relative position and velocity
- target estimate and uncertainty
- line-of-sight status
- distance to nearest obstacle
- local occupancy sample or ray-cast summary

This is the fastest way to prove the environment logic before adding heavy perception.

### Phase 5: Convert to True Multi-Agent Training

#### Goal

Turn the scripted target into a learned agent and recover the co-training spirit of the thesis.

#### Time

2 to 3 weeks

#### Environment Form

Use `DirectMARLEnv` with two agents:

- observer
- evader

#### First Multi-Agent Version

Keep these simplifications:

- planar or quasi-planar movement if needed
- same city scene family as in Phase 4
- no image observations yet
- stable high-level control interface

#### Reward Strategy

Start close to the thesis:

- observer reward increases with tracking quality or reduced uncertainty
- target reward is the negative of observer reward or a structured evasion reward

Then test whether pure zero-sum is stable enough in physics-based simulation.

#### Evaluation

Create fixed scenario suites, not just random rollouts.

At minimum evaluate:

- open map
- sparse obstacles
- dense obstacles
- road-constrained target
- unseen procedural layouts

#### Deliverables

- two-agent training run that does not diverge
- plots of reward, visibility rate, episode length, and failure causes
- 10 to 20 saved rollout videos or trajectories for qualitative inspection

### Phase 6: Reintroduce Context Knowledge Properly

#### Goal

Bring back the strongest part of your thesis: structured environment awareness.

#### Time

2 to 4 weeks

#### Two Good Options

##### Option A: Preserve the Thesis Representation Style

Keep map-like channels such as:

- building map
- road map
- position map
- rotation map

Then process them with a CNN, just as in the thesis.

This is the most faithful transfer of your previous work.

##### Option B: Replace Map Channels with Isaac-Native Perception

Use:

- ray caster summaries
- depth-like geometric sensing
- occupancy-like local tensors
- eventually camera observations

This is less faithful to the thesis, but more aligned with how a drone might actually perceive the environment.

#### Recommendation

Do both, but in order:

1. preserve the thesis map-channel approach first
2. use it as a controlled baseline in Isaac Lab
3. then build a more realistic sensor-driven variant

That gives you a clean research story:

- thesis-style structured context in Isaac
- then realism upgrade through embodied sensing

### Phase 7: Move from Ground Target to Drone Target

#### Goal

Reach your actual long-term objective: drone-focused multi-agent RL.

#### Time

3 to 6 weeks

#### Migration Path

First version:

- observer drone
- target drone
- same reward logic as pursuit-evasion
- simplify altitude or flight corridor if needed

Second version:

- full 3D tracking and evasion
- obstacle-aware aerial maneuvering
- asymmetric sensing or communication assumptions

Third version:

- multiple observers and one evader, or multiple evaders
- communication constraints
- decentralized actors with centralized critic if needed

#### Important Warning

Do not move to full 3D multi-drone MARL until your two-agent observer-versus-ground-target task is stable and reproducible.

That earlier stage is where you debug reward design, reset logic, and scene interaction without compounding all failure modes.

## What to Learn, in Order

### Tier 1: Must Learn Immediately

- USD basics
- Isaac Sim scene graph and assets
- Isaac Lab task structure
- vectorized training and headless execution
- PPO training loop and Isaac Lab wrappers
- basic aerial task control interfaces

### Tier 2: Must Learn Before Serious Research Runs

- sensor setup: IMU and ray caster
- domain randomization in Isaac Lab
- performance tuning and memory limits
- logging, checkpoints, and rollout inspection
- task registration and project structure

### Tier 3: Learn Once the Core Pipeline Works

- camera observations and tiled rendering
- custom drone asset import
- ROS 2 interfaces
- multi-GPU or multi-node training
- sim-to-real considerations

## Concrete 8-Week Plan

### Week 1

- install Isaac Sim and Isaac Lab
- run one stock example end-to-end
- read ecosystem, quickstart, and task workflow docs
- inspect [test_robot_nvidia.usd](test_robot_nvidia.usd) in the GUI to understand USD staging

### Week 2

- complete direct RL environment tutorial
- modify a stock task's reward and observation function
- document how Isaac Lab's environment loop maps to your thesis code structure

### Week 3

- run the quadcopter baseline
- inspect observations, actions, and training logs
- test headless training and small perturbation robustness

### Week 4

- create a custom single-agent or scripted-target scene with obstacles
- implement reset, dones, reward, and visibility logic
- verify rollouts visually before long training runs

### Week 5

- convert the scripted target to a learned target in `DirectMARLEnv`
- run small two-agent experiments on simple maps
- record failure modes and reward pathologies

### Week 6

- add structured context channels or ray-cast summaries
- compare state-only versus state-plus-context policies
- reproduce one clear thesis-like result inside Isaac

### Week 7

- expand to more urban scene variation
- add randomization, noise, and robustness tests
- evaluate on held-out maps or layouts

### Week 8

- plan the transition to drone-vs-drone pursuit-evasion
- lock down baseline metrics
- decide whether to stay with PPO or extend the training stack for richer MARL methods

## Thesis-to-Isaac Mapping Table

| Thesis Concept | Isaac Equivalent | Recommendation |
| --- | --- | --- |
| 2D generated maps | USD scenes with buildings and roads | start with simple authored geometry, procedural generation later |
| context map channels | map tensors, ray-cast tensors, or camera/depth tensors | keep map tensors first, then compare to sensor-driven inputs |
| custom RLlib env | Isaac Lab `DirectMARLEnv` | best first migration path |
| PPO in RLlib | PPO through an Isaac Lab-supported training pipeline | keep PPO first |
| observer UAV fixed altitude | drone in simplified control regime | keep simplifications early |
| target ground vehicle | scripted then learned ground agent | best bridge step |
| occlusion through map logic | ray tests, line-of-sight logic, or geometry queries | implement explicitly first |
| building collision / road slowdown | scene interaction + task logic | keep as environment logic, not policy magic |
| CNN over context maps | CNN branch in policy network | add only after state-only baseline works |

## Recommended Experiment Ladder

Run these in order. Do not skip ahead.

1. Stock cartpole or stock tutorial task trains successfully.
2. Modified stock task still trains after your reward edit.
3. Stock quadcopter hover or waypoint task trains successfully.
4. Custom observer drone scene runs with resets and rewards but no learning yet.
5. Observer drone learns against a scripted target in a simple open scene.
6. Same task with buildings and explicit occlusion.
7. Same task with multiple map layouts.
8. Two-agent learned observer and learned ground target.
9. State-only policy versus state-plus-context policy comparison.
10. Thesis-style map channels versus Isaac-native sensing comparison.
11. Drone observer versus drone target in simplified 3D setting.
12. Multi-agent scaling beyond two agents.

## What You Should Read Online

### Official NVIDIA Resources

Read these in roughly this order:

1. Isaac Sim overview: https://docs.isaacsim.omniverse.nvidia.com/latest/index.html
2. Isaac Sim basic usage tutorial: https://docs.isaacsim.omniverse.nvidia.com/latest/introduction/quickstart_isaacsim.html
3. Isaac Lab homepage: https://isaac-sim.github.io/IsaacLab/main/index.html
4. Isaac Lab task workflows: https://isaac-sim.github.io/IsaacLab/main/source/overview/core-concepts/task_workflows.html
5. Direct RL environment tutorial: https://isaac-sim.github.io/IsaacLab/main/source/tutorials/03_envs/create_direct_rl_env.html
6. Isaac Lab RL overview: https://isaac-sim.github.io/IsaacLab/main/source/overview/reinforcement-learning/index.html
7. RL framework comparison: https://isaac-sim.github.io/IsaacLab/main/source/overview/reinforcement-learning/rl_frameworks.html
8. Debugging and training guide: https://isaac-sim.github.io/IsaacLab/main/source/overview/reinforcement-learning/training_guide.html
9. IMU sensor docs: https://isaac-sim.github.io/IsaacLab/main/source/overview/core-concepts/sensors/imu.html
10. Ray caster docs: https://isaac-sim.github.io/IsaacLab/main/source/overview/core-concepts/sensors/ray_caster.html

### Optional Community References

Use these for ideas, not as your main implementation target.

1. OmniDrones: https://github.com/btx0424/OmniDrones
   - useful because it is explicitly built for RL research on multi-rotor drones in Isaac Sim
   - caution: the maintainer notes that the project is hard to maintain and version compatibility can be a problem
2. Aerial Gym Simulator: https://github.com/ntnu-arl/aerial_gym_simulator
   - useful for aerial RL ideas, sensors, and large-scale aerial simulation design
   - caution: its current foundation is Isaac Gym, and its Isaac Lab / Isaac Sim support is described as under development

## Concrete Design Advice for Your Research Topic

### Start with the Right Observation Philosophy

Use three layers of observation complexity:

Layer 1:

- privileged state only

Layer 2:

- privileged state plus structured context tensors

Layer 3:

- embodied perception such as ray-based or camera-based observations

This gives you clean ablations and clear scientific conclusions.

### Start with the Right Action Philosophy

Use three layers of action complexity:

Layer 1:

- high-level velocity or heading commands

Layer 2:

- body-rate or attitude-rate commands

Layer 3:

- low-level motor thrusts

Only move downward if your research specifically requires it.

### Keep Evaluation Scientific

You already did this well in the thesis. Keep it.

Always compare:

- open versus cluttered maps
- seen versus unseen layouts
- state-only versus context-aware policies
- scripted opponent versus learned opponent
- ground target versus aerial target

Do not rely only on average reward curves.

Track:

- tracking error
- visibility rate
- uncertainty or estimate quality
- collision count
- time-to-loss-of-track
- episode length
- success or failure mode labels

## Common Failure Modes You Should Expect

1. Physics instability causes NaNs long before the RL logic is truly wrong.
2. Too many parallel environments can hide logic bugs behind out-of-memory or throughput issues.
3. Camera observations can dominate compute and make iteration painfully slow.
4. A badly scaled reward in physics-based simulation becomes much more destructive than in simple 2D environments.
5. If resets place drones into invalid states, training will look like an RL problem but is really an environment problem.
6. Custom drone assets can absorb weeks. Avoid that until the baseline pipeline works.

## What Not to Do

- do not start with a custom imported drone if the built-in quadcopter can answer the first research questions
- do not start with raw RGB images
- do not start with raw motor thrust control unless low-level control is itself your research problem
- do not assume your thesis PPO hyperparameters will transfer directly
- do not try to debug long training runs before you can visually verify short scripted rollouts
- do not mix three new problems at once: custom asset, custom sensor stack, and multi-agent learning

## First Deliverable I Would Personally Target

If I were executing this roadmap for you, my first serious milestone would be:

"A single observer drone in Isaac Lab learns to maintain line-of-sight to a scripted ground target in a simple urban obstacle scene, using state observations plus one compact context signal."

Why this milestone matters:

- it is close to your thesis
- it uses Isaac for what Isaac is good at
- it avoids premature MARL instability
- it gives you a working bridge from your old code ideas to the new platform

Once that works, converting the target into a learned agent becomes a tractable next step instead of a blind leap.

## Final Recommendation

Treat this as a three-stage journey, not one jump:

1. learn the Isaac toolchain
2. rebuild the thesis logic inside Isaac Lab with minimal realism
3. grow that system into full drone MARL

That path is slower than a reckless direct jump for the first two weeks, but much faster over the full project.

## Immediate Next Actions

Do these next, in order:

1. install and launch a stable Isaac Sim build
2. clone Isaac Lab separately and run one stock training job
3. complete the direct RL environment tutorial
4. run the built-in quadcopter task
5. create a one-page mapping from your thesis environment functions to Isaac Lab task methods
6. define your first bridge milestone: observer drone versus scripted ground target
