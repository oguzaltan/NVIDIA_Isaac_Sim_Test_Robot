# Phase 0: Setup and Orientation

## Goal

Install Isaac Sim and Isaac Lab cleanly, then build the mental model: Isaac Sim is the simulator; Isaac Lab is the robot-learning/task framework; the RL backend trains policies on top of Isaac Lab environments.

Estimated time: 2 to 4 days.

## Sources

- Isaac Sim 5.1 overview: https://docs.isaacsim.omniverse.nvidia.com/5.1.0/index.html
- Isaac Sim download: https://docs.isaacsim.omniverse.nvidia.com/5.1.0/installation/download.html
- Isaac Sim requirements: https://docs.isaacsim.omniverse.nvidia.com/5.1.0/installation/requirements.html
- Isaac Lab ecosystem: https://isaac-sim.github.io/IsaacLab/v2.3.0/source/setup/ecosystem.html
- Isaac Lab installation: https://isaac-sim.github.io/IsaacLab/v2.3.0/source/setup/installation/index.html
- Isaac Lab quickstart: https://isaac-sim.github.io/IsaacLab/v2.3.0/source/setup/quickstart.html
- Isaac Lab project structure: https://isaac-sim.github.io/IsaacLab/v2.3.0/source/overview/own-project/project_structure.html

## Do

- Install a version-matched Isaac Sim and Isaac Lab setup.
- Record Isaac Sim version, Isaac Lab tag/commit, Python version, GPU driver, CUDA/PyTorch version, and OS.
- Launch Isaac Sim GUI once and confirm a simple stage loads.
- Run one Isaac Lab stock training job.
- List available Isaac Lab environments.
- Open [test_robot_nvidia.usd](../test_robot_nvidia.usd) in Isaac Sim and inspect the stage tree.

## Write

- A 5 to 8 sentence Isaac stack explanation: Omniverse Kit -> Isaac Sim -> Isaac Lab -> task -> RL backend.
- A short note on what belongs in Isaac Sim, what belongs in Isaac Lab, and what belongs in the RL library.
- A one-line warning to yourself about not mixing Windows and WSL Python environments.

## Thesis Link

Your old thesis code was one custom RL environment. In Isaac, that splits into USD scene/asset work, Isaac Lab task logic, and RL backend configuration. This phase prevents confusion between those layers.

## Exit Gate

You can move on when:

- Isaac Sim launches.
- One Isaac Lab training command starts and writes logs.
- You can explain `num_envs`, `headless`, `task`, and `@configclass` at a high level.
- You know where a future custom thesis task would live in a generated Isaac Lab project.

## Avoid

- Following `latest` docs blindly if they point to early developer pages.
- Treating Isaac Lab as the simulator.
- Debugging RL before you know the install is sane.
