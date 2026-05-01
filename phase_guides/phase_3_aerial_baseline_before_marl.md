# Phase 3: Aerial Baseline Before MARL

## Purpose

This phase is where you stop learning Isaac through cartpole-like examples and start learning it through an aerial task that resembles your real direction.

Do not skip this phase. Your goal is not merely to run a quadcopter demo. Your goal is to choose the right control abstraction, the right observation abstraction, and the right debugging habits before you build your custom thesis-derived environment.

## What You Should Know By The End

By the end of this phase, you should be able to answer:

- what action abstraction you want for your first research task
- what observations you can get easily in Isaac Lab
- what sensors are worth using early and which ones should wait
- how aerial tasks differ from simple benchmark tasks in stability and performance demands

You should also have run at least one stock aerial task successfully.

## Resource Stack

Work through these in order.

### 1. Built-in Quadcopter Task Reference

Resource:

- https://github.com/isaac-sim/IsaacLab/blob/main/source/isaaclab_tasks/isaaclab_tasks/direct/quadcopter/quadcopter_env.py

What to learn from it:

- how an aerial task is structured in real task code
- what actions are applied
- what observations are exposed
- what reward terms are used

Read the source slowly. This is one of the most relevant pieces of reference code for your path.

### 2. Isaac Lab Environments Overview

Resource:

- https://isaac-sim.github.io/IsaacLab/main/source/overview/environments.html

What to learn from it:

- where quadcopter tasks sit among other provided tasks
- how official tasks are named and organized

### 3. IMU Sensor Docs

Resource:

- https://isaac-sim.github.io/IsaacLab/main/source/overview/core-concepts/sensors/imu.html

What to learn from it:

- what IMU signals are available
- how linear and angular measurements are exposed
- what caveats exist around acceleration interpretation and bias

### 4. Ray Caster Docs

Resource:

- https://isaac-sim.github.io/IsaacLab/main/source/overview/core-concepts/sensors/ray_caster.html

What to learn from it:

- how geometric sensing can be built without full rendering
- how ray-based sensing can serve as a compact context signal
- why static mesh assumptions matter

### 5. RL Library Comparison

Resource:

- https://isaac-sim.github.io/IsaacLab/main/source/overview/reinforcement-learning/rl_frameworks.html

What to learn from it:

- which libraries are supported
- what their tradeoffs are
- why PPO is still a sensible starting point for your work

### 6. Debugging and Training Guide

Resource:

- https://isaac-sim.github.io/IsaacLab/main/source/overview/reinforcement-learning/training_guide.html

What to learn from it:

- how `num_envs` affects performance and memory
- why rendering can become expensive
- how NaNs often come from simulation instability rather than pure RL failure

## Exact Learning Tasks

### Task 1: Run a Stock Quadcopter Task

Do this in three modes if possible:

- interactive
- headless
- headless with logging or video

What to inspect:

- episode behavior
- reward signal trend
- action scale
- observation size and semantics

### Task 2: Extract the Action Abstraction

Read the quadcopter task source and answer:

- are actions raw motor commands, thrust values, rates, or higher-level commands?
- what part of the environment turns actions into applied forces or controls?
- would this abstraction let you study tracking and evasion cleanly?

Then decide your preferred initial abstraction for thesis transfer:

- high-level velocity or heading control
- attitude-rate control
- motor thrust control

For your first custom bridge task, high-level or mid-level control is usually the right answer.

### Task 3: Extract the Observation Abstraction

Answer:

- which observations are state-like?
- which are sensor-like?
- what is privileged versus realistic?
- what could later be replaced by a ray-cast or map-context input?

### Task 4: Run Noise and Perturbation Experiments

At minimum test:

- different initial poses
- mild action noise
- mild observation noise
- headless versus rendered training behavior

Goal:

- build intuition for how fragile aerial training can become

### Task 5: Create a Personal Baseline Memo

Write a 1 to 2 page memo answering:

- what control abstraction I will use first
- what observations I will use first
- what I will postpone
- what stability risks I saw in the stock aerial task

## What You Should Learn Conceptually

### 1. Action Abstraction Is a Research Decision

If you start with raw motor commands, you are partly studying low-level flight control.

If you start with heading or velocity abstractions, you are studying higher-level pursuit-evasion behavior.

Your thesis is much closer to the second category.

### 2. Sensor Realism Is Not Free

Full cameras increase compute, memory use, and debugging difficulty.

Ray casting and compact geometric context are often much better for early task development.

### 3. Aerial Tasks Fail Differently Than Toy Control Tasks

Cartpole mainly teaches task structure.

Quadcopter tasks teach:

- stability limits
- action scaling sensitivity
- reset validity importance
- performance costs that matter later in MARL

## Deliverables

Before leaving this phase, produce:

- one successful stock aerial run
- one written action-abstraction decision
- one written observation-abstraction decision
- one memo on what to keep simple in your first custom task

## Common Mistakes In This Phase

### Mistake 1: Confusing a Stock Task With a Ready Research Baseline

Fix:

- use stock tasks to learn platform design patterns, not as proof that your custom research problem is already solved

### Mistake 2: Starting With Cameras Too Early

Fix:

- prefer state plus geometric context first, then add richer sensing later

### Mistake 3: Choosing Low-Level Control Without a Good Reason

Fix:

- align the action abstraction with your research question, not with what looks more "realistic"

## Exit Criteria

You are done with Phase 3 only if:

- you have run a stock quadcopter task
- you understand its action and observation structure
- you know what control abstraction you will use first
- you know what sensing abstraction you will use first
- you have a written memo explaining those choices

## What You Should Learn Next

After this phase, you are ready to design the first real bridge from your thesis to Isaac.

That means the next phase is about building:

- one aerial observer
- one scripted ground target
- one simple urban obstacle scene
- one tracking-style reward
- one line-of-sight or occlusion model

That is your first serious milestone.
