# Phase 1: Isaac Sim Fundamentals

## Goal

Learn enough Isaac Sim and USD to create, inspect, save, and script simple scenes. Your thesis maps become USD scenes, so scene literacy matters before RL code.

Estimated time: 4 to 7 days.

## Sources

- Isaac Sim Python scripting: https://docs.isaacsim.omniverse.nvidia.com/5.1.0/python_scripting/index.html
- Isaac Sim basic usage tutorial: https://docs.isaacsim.omniverse.nvidia.com/5.1.0/introduction/quickstart_isaacsim.html
- Isaac Sim robot setup: https://docs.isaacsim.omniverse.nvidia.com/5.1.0/robot_setup/index.html
- Isaac Sim importers/exporters: https://docs.isaacsim.omniverse.nvidia.com/5.1.0/importer_exporter/importers_exporters.html
- OpenUSD docs: https://openusd.org/release/index.html
- NVIDIA USD overview: https://developer.nvidia.com/usd

## Learn

- stage, prim, prim path, default prim
- Xform hierarchy, references, authored properties
- visual mesh versus collision mesh
- rigid body, articulation root, joints, drives, gravity
- scripted scene changes versus runtime simulation state

## Do

- Build a simple scene with a ground plane, light, obstacles, and one robot or rigid object.
- Save, close, reload, and verify the scene.
- Inspect prim paths and physics properties.
- Create a small obstacle wall/corridor procedurally with Python.
- Compare one GUI edit with one scripted edit.

## Write

- What is a USD stage in one paragraph?
- What is the difference between visual and collision geometry?
- Why can bad collision geometry ruin RL training?
- Which parts of your thesis map generator could become USD scene generation?

## Thesis Link

Your thesis used 2D maps with buildings and roads. In Isaac, buildings, roads, collision geometry, and semantic metadata must become scene assets or task-side tensors. Start simple: blocks and corridors before full procedural cities.

## Exit Gate

You can move on when:

- You can create and save a simple stage intentionally.
- You can identify prim paths and collision geometry.
- You have one obstacle-spawning script or snippet.
- You can explain how this scene would be cloned many times for RL.

## Avoid

- Learning only through the GUI.
- Importing a custom drone yet.
- Ignoring collision approximations.
