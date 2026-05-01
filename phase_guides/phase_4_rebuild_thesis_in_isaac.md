# Phase 4: Rebuild the Thesis in Isaac, but Keep It Simple

## Purpose

This is the first phase where you build something that is genuinely yours and genuinely close to your thesis.

The goal is not to build the full final research system. The goal is to create the correct bridge task:

- observer is a drone
- target is scripted and ground-based
- environment contains meaningful obstacles
- tracking reward exists
- visibility and occlusion matter

If you do this phase well, you will have a clean, debuggable platform for later multi-agent work.

## What You Should Know By The End

By the end of this phase, you should have:

- one custom task concept written down clearly
- one simple urban or obstacle scene suitable for tracking experiments
- one custom observer-versus-scripted-target environment running in Isaac Lab
- one reward definition you can defend technically
- one visibility or line-of-sight model working reliably

## Why This Phase Must Stay Simple

Your thesis already contains a lot of complexity:

- estimation-based tracking
- occlusion
- map context
- antagonistic agents
- procedural variation

If you reintroduce all of that at once inside a new simulator, you will not know whether failures come from:

- simulation
- scene design
- action scaling
- reward design
- reset logic
- target behavior
- sensor design
- training instability

This phase deliberately removes learned target behavior and rich perception so the environment logic can be verified first.

## Resource Stack

Work through these in order.

### 1. Revisit the Direct RL Environment Tutorial

Resource:

- https://isaac-sim.github.io/IsaacLab/main/source/tutorials/03_envs/create_direct_rl_env.html

Why you are revisiting it:

- this time you are no longer reading for structure only
- you are reading to adapt the pattern to your own task

### 2. Modifying an Existing Direct RL Environment

Resource:

- https://isaac-sim.github.io/IsaacLab/main/source/tutorials/03_envs/modify_direct_rl_env.html

What to learn from it:

- how to start from something known and adapt it incrementally
- how to avoid rewriting everything at once

### 3. Adding Sensors on a Robot

Resource:

- https://isaac-sim.github.io/IsaacLab/main/source/tutorials/04_sensors/add_sensors_on_robot.html

What to learn from it:

- how sensors are attached and configured
- how sensor data enters the scene and can later enter observations

### 4. Draw Markers and Record Video

Resources:

- https://isaac-sim.github.io/IsaacLab/main/source/how-to/draw_markers.html
- https://isaac-sim.github.io/IsaacLab/main/source/how-to/record_video.html

What to learn from them:

- how to visualize target positions, line of sight, and debug states
- how to record short qualitative rollouts for later analysis

### 5. Wrap RL Environments

Resource:

- https://isaac-sim.github.io/IsaacLab/main/source/how-to/wrap_rl_env.html

What to learn from it:

- how custom tasks are exposed to supported training stacks cleanly

## What To Build In This Phase

### Environment Definition

Build a task with:

- one observer drone
- one scripted ground target
- simple obstacle layout or urban-block-like scene
- no learned target yet
- no RGB camera yet

### Action Space Recommendation

Use a simplified action space first.

Good first choices:

- horizontal velocity command plus yaw command
- waypoint delta command
- heading-rate command with fixed forward speed

Avoid raw motor thrust at this stage unless you have a strong research reason.

### Observation Space Recommendation

Start with privileged state plus one compact context feature.

Good early observation terms:

- relative target position or estimated relative target position
- relative velocity
- observer pose and speed
- line-of-sight boolean or visibility score
- obstacle-distance summary or ray-cast summary
- target estimate uncertainty scalar if you model one

### Reward Recommendation

Start with a reward that measures tracking quality directly and can be debugged.

Good early reward components:

- positive reward for maintaining visibility or reducing tracking error
- penalty for losing line of sight
- penalty for collisions or invalid states
- mild action smoothness penalty only if needed

Do not start with a reward that is so elaborate that you cannot explain a bad rollout.

## Exact Work Plan

### Step 1: Write the Task Spec Before Coding

In one page, define:

- state variables
- action definition
- observation definition
- reward definition
- termination conditions
- reset distribution
- evaluation scenarios

If you cannot write the task spec cleanly, do not code yet.

### Step 2: Build the Scene and Scripted Target Behavior First

Before training anything, confirm that:

- the observer can exist in the scene stably
- the target moves through the scene as intended
- collisions and boundaries behave correctly
- line-of-sight logic produces sensible outputs

### Step 3: Add Visual Debugging

Use markers or overlays to visualize:

- observer pose
- target pose
- target estimated pose if applicable
- line-of-sight ray or visibility status
- collision or failure states

If you skip visual debugging, this phase becomes much slower.

### Step 4: Run No-Learning Rollouts

Before long training runs, execute short rollouts with:

- scripted actions
- random actions
- fixed target paths

Goal:

- verify that rewards, resets, and dones fire when expected

### Step 5: Train the Observer Only

Do not add a learned target yet.

Goal:

- confirm that the observer learns a sensible behavior against a stable scripted target policy

## Deliverables

Before leaving this phase, produce:

- a written task spec
- a running custom task
- a small set of rollout videos
- one short report explaining the reward and observation design
- one scenario table for evaluation

## What To Learn While Doing This Phase

You should actively learn how to answer these questions:

1. What parts of the thesis transfer directly into Isaac?
2. What parts become simpler in 3D simulation and what parts become harder?
3. What is the minimal context signal that already improves tracking?
4. Which failures come from environment logic rather than learning?

## Common Mistakes In This Phase

### Mistake 1: Building the Learned Target Too Early

Fix:

- keep the target scripted until the observer-side task is verified

### Mistake 2: Adding Rich Perception Too Early

Fix:

- use compact geometric context first

### Mistake 3: Writing Reward Logic Before Watching Random Rollouts

Fix:

- always watch short random or scripted rollouts before trusting training curves

## Exit Criteria

You are done with Phase 4 only if:

- the custom observer-versus-scripted-target task runs reliably
- rewards behave sensibly during short rollouts
- visibility or occlusion logic is visibly correct
- you can explain every term in the observation and reward definitions
- the observer learns something nontrivial in at least one simple scenario

## What You Should Learn Next

After this phase, you are ready to turn the scripted target into a learned opponent.

That means the next phase is about:

- `DirectMARLEnv`
- two-agent task design
- asymmetric observation design
- co-training stability
- scenario-based multi-agent evaluation
