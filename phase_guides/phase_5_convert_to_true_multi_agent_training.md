# Phase 5: Convert to True Multi-Agent Training

## Purpose

This phase restores the core contribution style of your thesis: competitive co-training of observer and evader.

The task now becomes truly multi-agent. The target is no longer a scripted disturbance. It is now part of the learning problem.

## What You Should Know By The End

By the end of this phase, you should have:

- one `DirectMARLEnv`-based task design
- observer and target observation definitions that you can justify
- a stable first co-training experiment
- a plan for how to evaluate competition and not just reward curves

## Resource Stack

Because the dedicated direct MARL tutorial page is not a reliable doc entry point right now, use the following official source references.

### 1. Task Design Workflows

Resource:

- https://isaac-sim.github.io/IsaacLab/main/source/overview/core-concepts/task_workflows.html

What to learn from it:

- why direct workflow is still appropriate
- how direct MARL fits the framework philosophy

### 2. Direct MARL Example: Cart Double Pendulum

Resource:

- https://github.com/isaac-sim/IsaacLab/blob/main/source/isaaclab_tasks/isaaclab_tasks/direct/cart_double_pendulum/cart_double_pendulum_env.py

What to learn from it:

- how a `DirectMARLEnv` is structured in real code
- how multi-agent stepping is handled

### 3. Direct MARL Example: Shadow Hand Over

Resource:

- https://github.com/isaac-sim/IsaacLab/blob/main/source/isaaclab_tasks/isaaclab_tasks/direct/shadow_hand_over/shadow_hand_over_env.py

What to learn from it:

- how a more complex multi-agent task is organized
- how multiple agents can share a scene while maintaining separate interfaces

### 4. RL Framework Comparison

Resource:

- https://isaac-sim.github.io/IsaacLab/main/source/overview/reinforcement-learning/rl_frameworks.html

What to learn from it:

- when PPO is enough
- when you may eventually want richer MARL support

### 5. Debugging and Training Guide

Resource:

- https://isaac-sim.github.io/IsaacLab/main/source/overview/reinforcement-learning/training_guide.html

What to learn from it:

- how to debug instability and throughput issues before blaming multi-agent dynamics alone

## What To Design In This Phase

### Agent Roles

Define clearly:

- observer objective
- evader objective
- whether the game is pure zero-sum or partially shaped

For your first version, stay close to the thesis:

- observer reward tracks tracking quality
- target reward is its negation or a close structured complement

### Observation Asymmetry

You already used asymmetry in the thesis.

Keep that discipline here.

Examples:

- observer gets estimated target state and uncertainty
- target gets privileged knowledge of observer pose in the first version
- later versions can reduce privilege if needed

### Action Simplicity

Keep the same action abstraction you stabilized in Phase 4.

Do not change to lower-level control and multi-agent learning at the same time.

## Exact Work Plan

### Step 1: Freeze the Observer Task Definition

Before adding the learned target, freeze these parts from Phase 4:

- scene
- observer action interface
- observer reset logic
- observer reward scaffold

If you change all of these while adding MARL, you will not know what caused failure.

### Step 2: Replace Scripted Target With a Learnable Target Interface

Start by preserving the target's physical role but exposing:

- target observations
- target actions
- target rewards
- target reset state

Keep the target's motion model simple first.

### Step 3: Run Small-Scale Stability Experiments

Before long runs, test:

- very small `num_envs`
- short episode lengths
- easy obstacle layouts
- fixed seeds

The goal is not performance. The goal is to make sure nothing pathological happens immediately.

### Step 4: Compare Training Schedules

Try at least two training schemes conceptually, even if one becomes your main default:

- simultaneous co-training
- staged training where one policy starts from a stronger initialization

You do not need to overcomplicate this yet, but you should not assume simultaneous learning is automatically stable.

### Step 5: Build Evaluation Scenarios Early

Create scenario groups such as:

- open scene
- sparse obstacles
- dense obstacles
- different target start regions
- unseen layout seeds

Evaluate both quantitative metrics and recorded trajectories.

## What To Watch For

### 1. Reward Hacking

The target may discover ways to end episodes cheaply or exploit edge cases.

Check for:

- boundary exploitation
- reset exploitation
- visibility exploitation that is uninteresting scientifically

### 2. Training Collapse

Check whether:

- one agent dominates too quickly
- both agents become degenerate
- rewards oscillate without meaningful behavior improvement

### 3. Symmetry Problems

The two-agent problem is not necessarily symmetric, and forcing symmetry where it does not belong can make the task less meaningful.

## Deliverables

Before leaving this phase, produce:

- one `DirectMARLEnv` task design or implementation
- one written observer and target observation specification
- one written reward specification for both agents
- one small evaluation suite
- one training note describing what was stable and what was not

## Common Mistakes In This Phase

### Mistake 1: Assuming Multi-Agent Means Just "Add Another Policy"

Fix:

- treat agent interfaces, scenario design, evaluation, and stability as first-class concerns

### Mistake 2: Changing Scene, Rewards, and Control at the Same Time

Fix:

- keep as many stabilized pieces from Phase 4 unchanged as possible

### Mistake 3: Judging Success Only by Mean Reward

Fix:

- inspect trajectories, visibility rates, tracking error, and failure labels

## Exit Criteria

You are done with Phase 5 only if:

- both agents can act through a true multi-agent interface
- training runs without immediate collapse or obvious environment bugs
- you have at least one nontrivial emergent behavior worth keeping
- you can explain failure modes without hand-waving

## What You Should Learn Next

After this phase, you are ready to bring back one of the most thesis-specific contributions: context knowledge.

That means the next phase is about:

- structured context channels
- CNN processing
- ray-cast or occupancy alternatives
- ablation between state-only and context-aware policies
