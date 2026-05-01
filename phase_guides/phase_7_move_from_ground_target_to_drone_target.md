# Phase 7: Move From Ground Target to Drone Target

## Purpose

This is the final transfer phase in the roadmap. The target is no longer a ground agent constrained by roads and buildings in the original way. It is now another drone, and the problem becomes true aerial pursuit-evasion.

This is where your long-term research goal starts to look like itself.

## What You Should Know By The End

By the end of this phase, you should have:

- one first drone-versus-drone pursuit-evasion task
- a justified 3D action and observation design
- a clear decision about how much realism and complexity to include
- one roadmap for scaling beyond two agents later

## Resource Stack

### 1. Add New Robot

Resource:

- https://isaac-sim.github.io/IsaacLab/main/source/tutorials/01_assets/add_new_robot.html

Use it to learn:

- how a new robot would be introduced if the built-in drone is not enough later

### 2. Import New Asset

Resource:

- https://isaac-sim.github.io/IsaacLab/main/source/how-to/import_new_asset.html

Use it to learn:

- the path from external asset to Isaac-ready asset

### 3. Write Articulation Config

Resource:

- https://isaac-sim.github.io/IsaacLab/main/source/how-to/write_articulation_cfg.html

Use it to learn:

- how robot configuration is represented in Isaac Lab

### 4. Simulation Performance and Tuning

Resource:

- https://isaac-sim.github.io/IsaacLab/main/source/how-to/simulation_performance.html

Use it to learn:

- how added agent count and sensing complexity affect training performance

### 5. Reproducibility and Multi-GPU

Resources:

- https://isaac-sim.github.io/IsaacLab/main/source/features/reproducibility.html
- https://isaac-sim.github.io/IsaacLab/main/source/features/multi_gpu.html

Use them to learn:

- how to keep experiments comparable
- what scaling options exist once the task grows heavier

### 6. Curriculum Utilities

Resource:

- https://isaac-sim.github.io/IsaacLab/main/source/how-to/curriculums.html

Use it to learn:

- how to stage difficulty instead of throwing the hardest version at the learner immediately

## Design Decisions You Must Make

### 1. How 3D Is the Task Initially?

You have at least three reasonable choices.

#### Option A: Quasi-3D First

- limited altitude change
- mostly horizontal pursuit-evasion
- easier bridge from your thesis

#### Option B: Structured 3D

- full position in 3D
- bounded flight corridor or altitude band
- moderate complexity increase

#### Option C: Fully Free 3D

- no major simplification beyond environment bounds
- highest realism and difficulty

Recommendation:

- start with Option A or B

### 2. What Does the Target Know?

Choices include:

- privileged observer pose
- partial observer state
- observer detection only when visible
- noisy relative sensing

Your first version can stay asymmetric and somewhat privileged. Later versions can reduce privilege if the research question calls for it.

### 3. What Is the Action Interface?

Do not change it casually if the earlier phases already stabilized one that serves the research question.

You only need a lower-level action interface if your research genuinely requires low-level control behavior.

## Exact Work Plan

### Step 1: Preserve the Observer Side As Much As Possible

When converting the target to a drone, keep these pieces stable if you can:

- observer control abstraction
- observer reward scaffold
- evaluation metrics

This keeps the research story interpretable.

### Step 2: Upgrade the Target Dynamics Carefully

Before learning, verify that the target drone:

- spawns correctly
- moves stably
- respects environment bounds
- does not create physics pathologies immediately

### Step 3: Revisit Observations for 3D

You now need to decide what enters the policy in 3D.

Examples:

- relative 3D position and velocity
- relative heading or orientation cues
- altitude difference
- visibility or occlusion status
- obstacle context in 3D or projected local form

### Step 4: Revisit Rewards for 3D Pursuit-Evasion

Your 2D or mixed-ground logic may not transfer perfectly.

Check whether the reward still promotes:

- meaningful pursuit
- meaningful evasive behavior
- nondegenerate episode lengths
- obstacle-aware movement

### Step 5: Reintroduce Curriculum

Start easier, then harder.

Good curriculum dimensions:

- simpler obstacle density first
- lower target agility first
- shorter sensing range assumptions first or later, depending on stability
- fewer distractors first

### Step 6: Plan the Next Scale-Up

Only after two-agent drone-versus-drone is stable should you consider:

- multiple observers
- multiple evaders
- communication constraints
- decentralized execution with centralized critic designs

## What To Learn Conceptually

### 1. Drone-Versus-Drone Is Not Just a Harder Version of Drone-Versus-Ground

It changes:

- reachable state space
- occlusion patterns
- pursuit geometry
- control stability requirements
- likely failure modes

### 2. Realism Has a Cost

Every increase in realism adds complexity in:

- training stability
- sensor pipeline cost
- environment debugging
- evaluation complexity

Only include realism that supports the research question.

### 3. The End of the Roadmap Is the Start of Real Research Iteration

Once this phase works, the roadmap ends and your research loop begins:

- propose hypothesis
- modify representation or reward or curriculum
- run controlled ablations
- compare behavior and metrics

## Deliverables

Before leaving this phase, produce:

- one first drone-versus-drone task definition
- one first stable training or rollout result
- one note on 3D observation and action design
- one follow-up plan for scaling difficulty or agent count

## Common Mistakes In This Phase

### Mistake 1: Making the World Fully Realistic Too Soon

Fix:

- increase realism in layers, not in one jump

### Mistake 2: Changing Representation, Control, and Agent Dynamics Together

Fix:

- keep at least some earlier stabilized choices unchanged

### Mistake 3: Scaling Agent Count Before Two-Agent Stability Exists

Fix:

- prove the two-agent case first

## Exit Criteria

You are done with Phase 7 only if:

- a first drone-versus-drone pursuit-evasion task exists
- the task is stable enough to run controlled experiments
- you know what your next research variables are
- you are no longer using the roadmap to guess what to build next

## What You Should Learn After Finishing The Roadmap

After finishing all phases, your learning shifts from platform learning to research iteration.

The next topics to pursue depend on your specific thesis extension goals, but likely include:

- centralized critic or alternative MARL training schemes
- richer sensing and partial observability
- procedural 3D urban scene generation at scale
- robustness and domain randomization
- sim-to-real-oriented abstraction choices
- communication-aware multi-agent control

At that point, you should no longer ask "How do I learn Isaac?" You should ask "Which experiment do I run next, and what hypothesis am I testing?"
