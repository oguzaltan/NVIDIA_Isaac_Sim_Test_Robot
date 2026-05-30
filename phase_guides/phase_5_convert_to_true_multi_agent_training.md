# Phase 5: Convert to True Multi-Agent Training

## Goal

Restore the core thesis idea: competitive co-training between observer and evader. The scripted target becomes a learned agent.

Estimated time: 2 to 3 weeks.

## Sources

- Task workflows: https://isaac-sim.github.io/IsaacLab/v2.3.0/source/overview/core-concepts/task_workflows.html
- `DirectMARLEnv` API/source: https://isaac-sim.github.io/IsaacLab/main/_modules/isaaclab/envs/direct_marl_env.html
- Cart double pendulum MARL example: https://github.com/isaac-sim/IsaacLab/blob/v2.3.0/source/isaaclab_tasks/isaaclab_tasks/direct/cart_double_pendulum/cart_double_pendulum_env.py
- Shadow hand over MARL example: https://github.com/isaac-sim/IsaacLab/blob/v2.3.0/source/isaaclab_tasks/isaaclab_tasks/direct/shadow_hand_over/shadow_hand_over_env.py
- RL framework comparison: https://isaac-sim.github.io/IsaacLab/main/source/overview/reinforcement-learning/rl_frameworks.html
- Debugging/training guide: https://isaac-sim.github.io/IsaacLab/main/source/overview/reinforcement-learning/training_guide.html

## Design

Agents:

- observer: maximize tracking/localization quality
- evader: degrade observer tracking while avoiding degenerate failures

Start close to the thesis:

- observer reward from tracking quality, visibility, collision avoidance
- evader reward as negative observer reward or structured evasion reward
- asymmetric observations allowed in the first version
- same action abstraction as Phase 4

## Do

- Freeze the Phase 4 scene, observer control, reset logic, and reward scaffold.
- Replace scripted target motion with target observation/action/reward interfaces.
- Start with small `num_envs`, short episodes, easy maps, and fixed seeds.
- Compare simultaneous co-training with staged initialization if simultaneous learning collapses.
- Build evaluation scenarios early: open, sparse obstacles, dense obstacles, unseen layout seeds.

## Watch

- target exploiting boundaries or termination
- one agent dominating immediately
- oscillating rewards without useful behavior
- reset bugs that look like MARL instability
- reward hacking through visibility or collision edge cases

## Write

- Observer observation/reward spec.
- Target observation/reward spec.
- Training stability note.
- Scenario evaluation table.

## Thesis Link

Your thesis used adversarial co-training to avoid overfitting the observer to a fixed target. This phase reintroduces that idea only after the environment is already trustworthy.

## Exit Gate

You can move on when:

- Both agents act through a true multi-agent interface.
- Training runs without immediate environment-driven collapse.
- You have at least one nontrivial behavior worth preserving.
- You can label failure modes from trajectories, not just reward curves.

## Avoid

- Changing scene, action abstraction, rewards, and MARL interface all at once.
- Calling it successful because mean reward increases.
- Scaling to more agents before two-agent behavior is understood.
