# Copilot Instructions

## Build, test, and lint commands

No project-local build, test, or lint automation is present in this repository. There is also no single-test workflow to invoke from the repo itself.

The repository currently consists of a single authored USD stage asset:

- `test_robot_nvidia.usd`

## High-level architecture

This repository is not a multi-module application; it is a single Omniverse/USD scene asset authored as a binary **USDC** file. The stage-level metadata embedded in the asset indicates:

- `World` is the default prim and the main scene root.
- The stage includes `Environment` and `Render` branches, so scene content and render/view configuration live in the same asset.
- Omniverse Kit metadata is embedded in the file (`/OmniverseKit_7`, viewport/Hydra/RTX-related settings), which means the file stores both scene data and authoring/view state from Omniverse tooling.
- Physics-related schemas and properties are authored directly into the stage: strings in the asset show `RigidBody`, collision settings, convex hull approximation, drive parameters, and wheel/body properties such as `_Left_Wheel`, `body0`, `localPos`, `localRot`, `breakForce`, `breakTorque`, `angularVelocity`, and related PhysX/USD physics fields.

In practice, treat the repository as a self-contained Isaac Sim / Omniverse scene file rather than code plus config.

## Key conventions

- Treat `test_robot_nvidia.usd` as the source of truth; there are no companion scripts, tests, or generated artifacts in the repo.
- Because the file is binary **USDC**, do not hand-edit it as text. Use USD-aware tooling such as Isaac Sim, Omniverse Kit, or other USD utilities for structural changes.
- Preserve stage-level metadata such as `defaultPrim`, axis/unit settings, and existing `World`/`Environment`/`Render` organization unless the task explicitly requires a scene-layout change.
- Preserve embedded Omniverse authoring metadata unless the task is specifically about cleaning or reauthoring viewport/render settings.
- When extending physics behavior, follow the existing schema-driven pattern already embedded in the stage: attach USD Physics / PhysX properties to prims instead of inventing parallel config files.
