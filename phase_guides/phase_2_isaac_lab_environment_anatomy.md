# Phase 2: Learn Isaac Lab Environment Anatomy

## Purpose

This phase is where you learn how an Isaac Lab RL environment is actually built and executed.

This is the key bridge from "I understand the simulator" to "I can write a task." Your thesis transfer depends heavily on this phase, because your original Python implementation already had custom logic for observations, rewards, and episode termination. Isaac Lab gives you a new structure for those same ideas.

## What You Should Know By The End

By the end of this phase, you should be able to explain and use:

- `DirectRLEnv`
- `DirectRLEnvCfg`
- `@configclass`
- scene setup inside a task
- observation computation
- reward computation
- done and reset logic
- gym registration
- RL library wrappers at a high level

## Why This Phase Matters For Your Thesis

Your thesis environment already had the essential RL pieces:

- custom observation space
- custom action space
- custom reward function
- custom termination criteria
- custom scenario logic

Isaac Lab does not remove those responsibilities. It reorganizes them.

This phase teaches you where those responsibilities now live.

## Resource Stack

Work through these in order.

### 1. Task Design Workflows

Resource:

- https://isaac-sim.github.io/IsaacLab/main/source/overview/core-concepts/task_workflows.html

What to learn from it:

- direct versus manager-based environments
- why direct workflow is closer to traditional custom RL environments
- why direct workflow is the correct first choice for your thesis migration

### 2. Creating a Direct Workflow RL Environment

Resource:

- https://isaac-sim.github.io/IsaacLab/main/source/tutorials/03_envs/create_direct_rl_env.html

What to learn from it:

- task configuration layout
- `_setup_scene`
- `_get_observations`
- `_get_rewards`
- `_get_dones`
- `_reset_idx`
- `_pre_physics_step`
- `_apply_action`

This is the single most important tutorial in this phase.

### 3. Registering an Environment

Resource:

- https://isaac-sim.github.io/IsaacLab/main/source/tutorials/03_envs/register_rl_env_gym.html

What to learn from it:

- how tasks are registered
- why `gym.register()` matters
- how configuration entry points are exposed
- how environment names and entry points are wired together

### 4. Training with an RL Agent

Resource:

- https://isaac-sim.github.io/IsaacLab/main/source/tutorials/03_envs/run_rl_training.html

What to learn from it:

- where wrappers appear
- why RL libraries need Isaac Lab wrappers
- how headless, off-screen video, and interactive execution differ

### 5. Project Structure

Resource:

- https://isaac-sim.github.io/IsaacLab/main/source/overview/own-project/project_structure.html

What to learn from it:

- where your future task code will live in a proper project
- how project packaging and task discovery work together

## Exact Learning Tasks

### Task 1: Reproduce the Direct Cartpole Tutorial

Do not just skim it. Run it.

While doing so, map each function to its role:

- scene creation
- action processing
- physics application
- reward computation
- observation assembly
- reset logic

Write one sentence for each function in your own words.

### Task 2: Modify the Reward

Make one small, controlled reward modification in a stock task.

Good examples:

- change one reward scale
- remove one penalty term
- strengthen one survival term

Goal:

- confirm you can locate and reason about reward logic

### Task 3: Modify the Observation

Make one small observation change.

Good examples:

- remove one state component
- add one tracked quantity
- reorder the observation deliberately and inspect the consequences

Goal:

- confirm that you understand how policy inputs are assembled

### Task 4: Trace the Registration Path

Pick one stock task and trace:

- task name
- `gym.register()` location
- environment class entry point
- environment config entry point
- training config entry point

This exercise is important because many Isaac Lab beginners can run tasks without understanding how task discovery works.

### Task 5: Compare Interactive and Headless Execution

Run the same task in:

- interactive mode
- headless mode
- headless with video

Then write:

- what changed in speed
- what changed in observability
- which mode you should use for development versus long runs

## Key Mapping Exercise

Write a mapping from your thesis implementation to Isaac Lab. Use this structure.

### Thesis Concept -> Isaac Lab Location

- environment initialization -> config class plus scene setup
- observation space design -> `_get_observations`
- action interpretation -> `_pre_physics_step` and `_apply_action`
- reward logic -> `_get_rewards`
- termination criteria -> `_get_dones`
- scenario reset logic -> `_reset_idx`

If you cannot write this mapping clearly, you are not done with the phase.

## Deliverables

Before leaving this phase, produce:

- one modified stock task
- one note mapping the direct RL lifecycle
- one note tracing how registration works
- one comparison note for interactive versus headless execution

## Practical Checklist

You should be able to answer all of these from memory:

1. Why is `DirectRLEnv` a good starting point for you?
2. What is stored in a `DirectRLEnvCfg`?
3. Where do resets happen?
4. Where are actions processed before physics stepping?
5. Why does the RL library wrapper come last?
6. What exactly does task registration enable?

## Common Mistakes In This Phase

### Mistake 1: Reading Tutorials Without Running Them

Fix:

- run every tutorial you plan to rely on later

### Mistake 2: Understanding Functions Only By Name

Fix:

- write the data flow explicitly: actions in, physics step, observations out, rewards computed, dones computed, resets applied

### Mistake 3: Ignoring Registration and Packaging

Fix:

- trace at least one environment from task name to environment class to config class to trainer config

## Exit Criteria

You are done with Phase 2 only if:

- you have run and modified a direct RL task
- you can explain the full direct task lifecycle
- you know where your thesis environment logic will live in Isaac Lab
- you can explain how task registration and training scripts connect

## What You Should Learn Next

After this phase, you are ready to learn around an aerial task instead of a toy task.

That means the next phase is about:

- built-in quadcopter tasks
- action abstraction choices
- sensor choices
- performance and logging habits
- what an aerial baseline should look like before multi-agent complexity enters
