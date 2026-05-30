# Phase 7: Move From Ground Target to Drone Target

## Goal

Convert the target from a ground agent into another drone. This is the start of true aerial pursuit-evasion research.

Estimated time: 3 to 6 weeks or more.

## Sources

- Add a new robot: https://isaac-sim.github.io/IsaacLab/v2.3.0/source/tutorials/01_assets/add_new_robot.html
- Import a new asset: https://isaac-sim.github.io/IsaacLab/v2.3.0/source/how-to/import_new_asset.html
- Write articulation config: https://isaac-sim.github.io/IsaacLab/v2.3.0/source/how-to/write_articulation_cfg.html
- Simulation performance: https://isaac-sim.github.io/IsaacLab/main/source/how-to/simulation_performance.html
- Reproducibility: https://isaac-sim.github.io/IsaacLab/v2.3.0/source/features/reproducibility.html
- Multi-GPU: https://isaac-sim.github.io/IsaacLab/v2.3.0/source/features/multi_gpu.html
- Curriculum utilities: https://isaac-sim.github.io/IsaacLab/v2.3.0/source/how-to/curriculums.html
- Sim-to-real policy deployment: https://isaac-sim.github.io/IsaacLab/v2.3.0/source/policy_deployment/index.html

## Choose the First 3D Level

Start with one of these:

- quasi-3D: fixed or narrow altitude band, mostly horizontal pursuit
- structured 3D: full 3D positions inside a bounded flight volume
- fully free 3D: only after the previous two are stable

Recommendation: start quasi-3D or structured 3D.

## Preserve From Earlier Phases

Keep stable pieces if possible:

- observer action abstraction
- observer reward scaffold
- metrics
- scene family
- context representation

Only change the target dynamics first. This keeps the research story interpretable.

## Do

- Spawn two drones reliably.
- Verify both are stable before learning.
- Update observations for relative 3D position, velocity, heading/orientation, altitude difference, and visibility.
- Update rewards so pursuit/evasion remains meaningful in 3D.
- Add curriculum: open space first, lower target agility first, then obstacles and richer sensing.
- Save videos and trajectories for every curriculum stage.

## Next Scale-Up Options

After stable two-agent drone-vs-drone:

- multiple observers
- multiple evaders
- decentralized actors with centralized critic
- communication constraints
- partial observability
- stronger domain randomization
- sim-to-real-oriented control abstractions

## Thesis Link

This phase changes pursuit geometry and reachable states. It is not just the ground-target task with altitude. Preserve thesis metrics and context ablations so the paper can explain what changed.

## Exit Gate

You can move on when:

- A first drone-vs-drone task exists.
- Rollouts are stable enough for controlled experiments.
- You have a 3D observation/action design note.
- You know the next research variable to test.

## Avoid

- Making the environment fully realistic immediately.
- Importing custom drone assets before the built-in/reference drone is insufficient.
- Scaling agent count before two-agent drone-vs-drone is stable.
