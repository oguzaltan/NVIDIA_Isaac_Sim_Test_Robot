# Phase 1: Learn Isaac Sim Fundamentals

## Purpose

This phase teaches you how to think in Isaac Sim terms: stage, prims, USD structure, assets, rigid bodies, articulations, collisions, and scripted scene manipulation.

Your thesis previously used generated 2D maps as the environment substrate. In Isaac, the substrate becomes a 3D USD stage. If you do not understand how the stage is authored and manipulated, your later RL environment work will be fragile.

## What You Should Know By The End

By the end of this phase, you should be able to:

- create and save a simple USD scene
- explain what a prim is and what a prim path means
- distinguish visual geometry from collision geometry
- inspect a rigid body and an articulation
- spawn or place simple objects with Python
- reason about transforms, hierarchy, and references

## Core Concepts To Learn

### 1. USD Basics

You need practical understanding of:

- stage
- prim
- default prim
- Xform hierarchy
- references and composition
- authored properties
- meters, axes, and units

You do not need to become a USD expert yet. You need enough working literacy to avoid treating the scene as a black box.

### 2. Physics Representation

You need practical understanding of:

- rigid body
- articulation root
- joints and actuators at a high level
- collision shapes
- visual meshes
- gravity, solver stability, and contact behavior

### 3. Scripted Scene Manipulation

You need to understand:

- how Python interacts with the stage
- how objects are spawned and modified
- how simulation state differs from authored scene structure

## Resource Stack

Work through these in order.

### 1. Python Scripting and Tutorials

Resource:

- https://docs.isaacsim.omniverse.nvidia.com/latest/python_scripting/index.html

Focus on:

- Python scripting concepts
- Core API overview
- scene setup snippets
- robot simulation snippets

What to learn from it:

- how Isaac Sim scripting is structured
- what the core Python APIs manipulate
- how a scripted scene differs from a purely manual GUI-authored scene

### 2. Isaac Sim Robot Setup

Resource:

- https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/index.html

Focus on:

- robot inspector
- physics inspector
- asset structure
- validation tools

What to learn from it:

- how to inspect assets instead of guessing
- how to validate whether an asset is sane for simulation

### 3. Importers and Exporters

Resource:

- https://docs.isaacsim.omniverse.nvidia.com/latest/importer_exporter/importers_exporters.html

What to learn from it:

- what formats are supported
- where URDF or MJCF would fit later if you import your own robot
- why imported assets often still need cleanup and validation

### 4. USD Primer

Resource:

- https://developer.nvidia.com/usd

What to learn from it:

- the mental model of USD composition and hierarchy
- why scene structure matters in robotics workflows

## Exact Learning Tasks

### Task 1: Build a Minimal Scene by Hand

Create a stage with:

- ground plane
- one light
- at least three obstacles
- one robot or rigid object asset

What to practice:

- naming prims
- moving objects
- grouping objects under a meaningful hierarchy
- saving and reloading the stage

### Task 2: Inspect the Scene Tree Carefully

Pick one object and answer:

- what is its prim path?
- is it an Xform or mesh or physics prim?
- what properties are authored on it?
- what is visual and what is collision?

### Task 3: Script a Procedural Obstacle Layout

Use Python to create a small wall, corridor, or obstacle field.

Goal:

- get comfortable creating repeated geometry from code

Why it matters:

- your later urban scenes will depend on procedural generation ideas

### Task 4: Inspect a Robot or Articulated Asset

Using the GUI and available inspectors, identify:

- articulation root
- joint structure
- collision bodies
- important transforms

This is less about drones specifically and more about learning how simulated robots are represented.

### Task 5: Compare Two Scene Edits

Make one change via GUI and one via Python.

Then answer:

- what is easier with the GUI?
- what is easier with Python?
- which approach will scale better for RL task creation?

## What To Write As You Learn

Create a note answering these:

1. What is the smallest useful explanation of a USD stage?
2. What is the difference between authored scene structure and runtime simulation state?
3. Why can bad collision geometry ruin later RL work?
4. Why is procedural spawning better than manual layout for repeated experiments?

## Deliverables

Before leaving this phase, produce:

- one saved simple USD scene you understand
- one small Python script or notebook snippet that spawns repeated obstacles
- one written explanation of prim paths and hierarchy
- one written explanation of visual versus collision geometry

## Practical Checklist

You should be able to do all of the following without searching every step:

- open a stage and navigate the hierarchy
- find a prim path
- move or duplicate an object
- inspect physics properties
- save a stage variant
- explain what would need to change if this scene had to be replicated many times for RL

## Common Mistakes In This Phase

### Mistake 1: Learning Only Through the GUI

Why it is a problem:

- GUI familiarity helps inspection but does not scale to RL environment creation

Fix:

- always pair GUI inspection with at least one scripted manipulation exercise

### Mistake 2: Ignoring Collision Quality

Why it is a problem:

- later training failures may look like reward issues when they are really collision artifacts

Fix:

- inspect collision meshes early and often

### Mistake 3: Treating Prim Paths as Incidental Details

Why it is a problem:

- Isaac Lab configuration and scene binding rely heavily on stable paths and path patterns

Fix:

- write down the path structure of your scenes explicitly

## Exit Criteria

You are done with Phase 1 only if you can:

- create a small stage intentionally, not randomly
- explain the stage hierarchy clearly
- identify physics-relevant asset properties
- script a small procedural obstacle layout
- describe how this scene knowledge will later support an RL task

## What You Should Learn Next

After finishing this phase, you should learn how Isaac Lab wraps simulation into task structure.

That means the next phase is about:

- task classes
- config classes
- vectorization
- environment stepping
- rewards, observations, dones, resets
- registration and training wrappers
