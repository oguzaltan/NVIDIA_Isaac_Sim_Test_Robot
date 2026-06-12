"""Quick import test -- verifies Isaac Lab is accessible from your project.

This script launches the SimulationApp first (required by Isaac Sim),
then tests that all key modules can be imported.

Run:
    python scripts/test_imports.py --headless
"""

"""Launch Isaac Sim Simulator first (required before other imports)."""

import argparse

from isaaclab.app import AppLauncher

parser = argparse.ArgumentParser(description="Test Isaac Lab imports from project folder.")
AppLauncher.add_app_launcher_args(parser)
args_cli = parser.parse_args()
app_launcher = AppLauncher(args_cli)
simulation_app = app_launcher.app

"""Now test all imports."""

print("=" * 60)
print("Isaac Lab Import Test")
print("=" * 60)

# Core framework
from isaaclab.sim import SimulationCfg, SimulationContext
import isaaclab.sim as sim_utils
print("[OK] isaaclab.sim (SimulationCfg, SimulationContext)")

# Assets
from isaaclab.assets import AssetBaseCfg, RigidObjectCfg, ArticulationCfg
print("[OK] isaaclab.assets (AssetBaseCfg, RigidObjectCfg, ArticulationCfg)")

# Scene management
from isaaclab.scene import InteractiveScene, InteractiveSceneCfg
print("[OK] isaaclab.scene (InteractiveScene, InteractiveSceneCfg)")

# Config utilities
from isaaclab.utils import configclass
print("[OK] isaaclab.utils.configclass")

# Spawner configs
_ = sim_utils.GroundPlaneCfg
_ = sim_utils.CuboidCfg
_ = sim_utils.DomeLightCfg
_ = sim_utils.RigidBodyPropertiesCfg
_ = sim_utils.MassPropertiesCfg
_ = sim_utils.RigidBodyMaterialCfg
print("[OK] Spawner configs (GroundPlane, Cuboid, DomeLight, materials)")

# Tasks module
import isaaclab_tasks
print("[OK] isaaclab_tasks")

# RL environments
from isaaclab.envs import DirectRLEnv, DirectRLEnvCfg
print("[OK] isaaclab.envs (DirectRLEnv, DirectRLEnvCfg)")

print("\n" + "=" * 60)
print("All imports successful!")
print("Isaac Lab is ready to use from your project folder.")
print("=" * 60)

simulation_app.close()
