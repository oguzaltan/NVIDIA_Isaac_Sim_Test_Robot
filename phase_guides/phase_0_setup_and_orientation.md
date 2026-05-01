# Phase 0: Setup and Orientation

## Purpose

This phase is about building a correct mental model of the Isaac ecosystem and getting a working installation. It is not just an installation phase. It is the phase where you stop treating Isaac Sim, Isaac Lab, Omniverse, USD, and the RL library as one blurry platform.

If you skip this phase, you will later lose time on category mistakes such as:

- trying to debug a scene problem inside RL code
- trying to solve an Isaac Lab problem inside Isaac Sim GUI workflows
- mixing unstable docs, mismatched releases, and incompatible environments

## What You Should Know By The End

By the end of this phase, you should be able to explain all of the following clearly:

- what Isaac Sim is
- what Isaac Lab is
- what the RL library does and does not do
- why USD matters
- why Isaac Lab tasks are vectorized
- why direct workflow is the right starting point for your thesis transfer

You should also have at least one working training command and one working GUI session.

## Before You Start

### Environment Strategy

Use a stable Isaac Sim release for real work.

- Do not anchor your learning on unstable early developer release docs.
- Prefer a stable workstation install for GUI work.
- Keep notes about the exact version you installed.

### Windows and WSL Note

For your setup, keep this distinction clean:

- Isaac Sim GUI and native workstation installation: Windows
- Linux-style scripting habits and shell work: WSL only when clearly appropriate

Do not casually mix Python environments across Windows and WSL. That is a reliable way to create path, interpreter, and GPU confusion.

### Version Control Note

Create a separate working area for Isaac Lab itself later. This repository currently holds your thesis PDF, a USD asset, and roadmap notes. It is not a real Isaac Lab project yet.

## Resource Stack

Work through these in order.

### 1. Isaac Lab Ecosystem

Resource:

- https://isaac-sim.github.io/IsaacLab/main/source/setup/ecosystem.html

Learn this from it:

- Isaac Lab is not the simulator itself
- Isaac Lab sits on top of Isaac Sim
- Isaac Lab replaces older robot-learning stacks like IsaacGymEnvs and OmniIsaacGymEnvs
- Isaac Sim provides physics, rendering, sensors, robotics tooling, and USD workflows

What to write after reading:

- a 5 to 8 sentence explanation of the Isaac ecosystem in your own words

### 2. Isaac Sim Overview

Resource:

- https://docs.isaacsim.omniverse.nvidia.com/latest/index.html

Learn this from it:

- Isaac Sim is the robotics simulator and application
- it uses Omniverse Kit underneath
- scenes are represented with USD
- sensors, physics, rendering, and ROS capabilities live here

What to write after reading:

- what belongs in Isaac Sim that does not belong in Isaac Lab

### 3. Isaac Lab Quickstart Guide

Resource:

- https://isaac-sim.github.io/IsaacLab/main/source/setup/quickstart.html

Learn this from it:

- installation flow
- vectorized training mindset
- available environments listing
- project template generation
- configuration classes and task registration

What to write after reading:

- what `num_envs`, `headless`, `task`, and `@configclass` mean at a high level

### 4. Isaac Lab Project Structure

Resource:

- https://isaac-sim.github.io/IsaacLab/main/source/overview/own-project/project_structure.html

Learn this from it:

- project versus extension versus module versus task
- why package installation matters
- why `gym.register()` matters

What to write after reading:

- where your future custom thesis task will live in a real Isaac Lab project

## Exact Learning Tasks

### Task 1: Draw the Stack

Draw this stack on paper or in a note:

- Omniverse Kit
- Isaac Sim
- Isaac Lab
- task code
- RL wrapper
- PPO trainer

Then write one sentence per layer describing its responsibility.

If you cannot do this without looking back at the docs, you are not ready to move on.

### Task 2: Install and Launch Isaac Sim

Goal:

- you can launch Isaac Sim GUI successfully

What to confirm:

- GUI opens without broken extensions
- sample stage or empty stage loads
- GPU is recognized
- no version mismatch warnings are blocking use

### Task 3: Install Isaac Lab and Run a Stock Task

Goal:

- one stock Isaac Lab training job starts and progresses

Suggested first checks:

- list environments
- run a simple stock training command
- use `--headless` once and interactive mode once

What to observe:

- where logs are written
- how the task name maps to the environment implementation
- how many environments are used by default

### Task 4: Inspect Your Existing USD File

Open [test_robot_nvidia.usd](../test_robot_nvidia.usd) in Isaac Sim.

What to inspect:

- stage tree
- default prim
- physics properties
- how the scene is organized
- whether authoring metadata is stored inside the scene

The goal is not to edit it yet. The goal is to become less intimidated by a USD stage.

## Questions You Must Be Able To Answer

Write answers to all of these:

1. Why is Isaac Lab not a simulator?
2. Why does Isaac Lab still need Isaac Sim?
3. What is vectorization and why does it matter for RL?
4. Why is USD central to Isaac Sim workflows?
5. Why is the direct workflow a better first fit for your thesis than the manager workflow?
6. What is one reason not to start immediately with raw image observations?

## Deliverables

You should produce all of these before leaving the phase:

- a written ecosystem summary
- a written stack diagram or equivalent note
- one verified Isaac Sim launch
- one verified Isaac Lab training launch
- one short note after opening your USD stage

## Common Mistakes In This Phase

### Mistake 1: Installing Whatever the `latest` Docs Suggest Without Checking Release Stability

Fix:

- use stable Isaac Sim binaries and stable docs as your operational baseline

### Mistake 2: Treating Isaac Lab Like a Big Python Package With No Simulation Boundary

Fix:

- always remember that task code ultimately runs on top of a simulator application

### Mistake 3: Skipping the Ecosystem Explanation Step

Fix:

- force yourself to explain the stack in your own words before doing anything deeper

## Exit Criteria

You are done with Phase 0 only if all of the following are true:

- you can explain the Isaac stack clearly from memory
- you launched Isaac Sim successfully
- you launched Isaac Lab training successfully
- you know where a future custom project will live structurally
- you are no longer confusing simulator, task framework, and RL library roles

## What You Should Learn Next

After this phase, you should learn how Isaac Sim scenes actually work.

That means Phase 1 is about:

- scene graph
- assets
- transforms
- collision setup
- articulation basics
- Python scripting around the stage

Do not jump into custom RL code yet. First learn the substrate it will run on.
