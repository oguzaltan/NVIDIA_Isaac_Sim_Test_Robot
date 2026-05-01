# Phase 6: Reintroduce Context Knowledge Properly

## Purpose

This phase brings back one of the strongest ideas from your thesis: context knowledge.

In the thesis, context knowledge came from maps, position maps, rotation maps, roads, and buildings, and then entered the policy through a CNN branch. In Isaac, you now have a choice: preserve that representation first, or move immediately to more embodied sensing.

The right move is to do both in sequence, not both at once.

## What You Should Know By The End

By the end of this phase, you should have:

- one context-aware version of your task
- one state-only baseline for comparison
- one reasoned choice between map-style context and sensor-derived context
- one ablation result that tells you whether context is actually helping

## Resource Stack

### 1. Ray Caster

Resource:

- https://isaac-sim.github.io/IsaacLab/main/source/overview/core-concepts/sensors/ray_caster.html

Use it to learn:

- how compact geometric sensing can summarize nearby environment structure
- why this is often a better early context signal than full image rendering

### 2. Camera and Sensor Overview

Resources:

- https://isaac-sim.github.io/IsaacLab/main/source/overview/core-concepts/sensors/index.html
- https://isaac-sim.github.io/IsaacLab/main/source/overview/core-concepts/sensors/camera.html

Use them to learn:

- what is available when you eventually move toward richer perception
- why tiled rendering and image observations have real compute implications

### 3. Add Sensors on a Robot

Resource:

- https://isaac-sim.github.io/IsaacLab/main/source/tutorials/04_sensors/add_sensors_on_robot.html

Use it to learn:

- how to wire sensors into the scene cleanly

### 4. Debugging and Training Guide

Resource:

- https://isaac-sim.github.io/IsaacLab/main/source/overview/reinforcement-learning/training_guide.html

Use it to learn:

- how image or sensor-heavy pipelines affect memory, throughput, and debugging

## Two Legitimate Representation Strategies

### Strategy A: Preserve the Thesis Representation First

Build context inputs analogous to your thesis:

- building map
- road map
- observer or target position map
- rotation map
- optional estimated target position map

Benefits:

- closest continuity with your thesis
- clean scientific bridge from old work to new platform
- easier to compare against earlier results conceptually

Costs:

- less physically embodied than true onboard sensing
- you must decide how these maps are generated inside or alongside the Isaac task

### Strategy B: Replace Map Channels With Isaac-Native Sensing

Use one or more of:

- ray-cast hit summaries
- occupancy-like local tensors
- depth images
- semantic or segmentation signals later if needed

Benefits:

- more natural fit to a drone perception story
- more realistic path toward physical deployment ideas

Costs:

- more engineering and performance cost
- harder to isolate whether learning changes come from context quality or sensor pipeline complexity

## Recommended Order

Do these in this order:

1. state-only baseline
2. thesis-style context baseline
3. sensor-derived context variant

This creates a clean research narrative and clean ablation design.

## Exact Work Plan

### Step 1: Lock a State-Only Baseline

Before adding context, freeze a baseline policy that uses only state-like observations.

You need this because otherwise every context result will be hard to interpret.

### Step 2: Implement the Smallest Useful Context Extension

Do not start with every map channel from the thesis.

Start with one compact extension such as:

- obstacle occupancy patch around the agent
- building map plus observer position map
- ray-cast summary converted into a small tensor

### Step 3: Decide How Context Enters the Network

You have two broad choices:

- concatenate a compact hand-engineered context vector with state observations
- process a structured tensor or image-like input with a CNN branch

Recommendation:

- first test a compact vector or small tensor
- then move to a CNN branch if the representation truly benefits from spatial locality

### Step 4: Run Clean Ablations

At minimum compare:

- state only
- state plus context

If you have time, also compare:

- thesis-style map context
- ray-cast or occupancy context

### Step 5: Evaluate Beyond Reward

Track changes in:

- tracking error
- visibility rate
- collision frequency
- time-to-loss-of-track
- path quality around obstacles

Context is only valuable if behavior changes in the intended direction.

## What To Learn Conceptually

### 1. Context Is Not the Same as Vision

Your thesis already showed that structured contextual information can help. Keep that insight.

The point of this phase is not to chase realism blindly. The point is to determine what environment knowledge actually improves pursuit-evasion behavior.

### 2. Spatial Structure Needs the Right Network Interface

If context is spatial, a CNN or spatial encoder may be justified.

If context is already compact and semantically meaningful, forcing it through a CNN can be unnecessary complexity.

### 3. Ablation Discipline Matters

If you change both the representation and the network and the reward at once, you will not know what helped.

## Deliverables

Before leaving this phase, produce:

- a state-only baseline result
- at least one context-aware result
- one ablation table or comparison note
- one explanation of why the chosen context representation is justified

## Common Mistakes In This Phase

### Mistake 1: Adding Too Many Context Channels at Once

Fix:

- begin with the smallest context signal that could plausibly help

### Mistake 2: Using a CNN Before the Representation Justifies It

Fix:

- ask whether the input truly has exploitable spatial structure

### Mistake 3: Dropping the State-Only Baseline

Fix:

- never evaluate context without a simpler baseline to compare against

## Exit Criteria

You are done with Phase 6 only if:

- you have a stable state-only baseline
- you have a stable context-aware variant
- you can explain what the context representation adds
- you have at least one meaningful ablation result

## What You Should Learn Next

After this phase, you are ready for the final transfer step: changing the target from a ground platform into another drone.

That means the next phase is about:

- moving from quasi-planar or mixed-ground setups to true aerial pursuit-evasion
- extending the observation and action design into 3D
- deciding what realism level and multi-agent scale actually serve your research
