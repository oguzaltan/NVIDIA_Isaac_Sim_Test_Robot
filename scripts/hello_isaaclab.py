"""Hello World -- visual Isaac Lab script with a falling cube.

Demonstrates that Isaac Lab works from your project folder by creating
a simple scene with a ground plane and a falling cube.

Run from the NVIDIA_Isaac_Sim_Test_Robot root:

    # Visual mode (opens Isaac Sim window)
    python scripts/hello_isaaclab.py

    # Headless mode (no GUI, runs simulation steps then exits)
    python scripts/hello_isaaclab.py --headless

Note: This script follows the same pattern as Isaac Lab's own tutorials.
See /home/oguz/IsaacLab/scripts/tutorials/ for more examples.

"""

"""Launch Isaac Sim Simulator first."""

import argparse

from isaaclab.app import AppLauncher

parser = argparse.ArgumentParser(
    description="Hello World -- verify Isaac Lab works from your project folder."
)
AppLauncher.add_app_launcher_args(parser)
args_cli = parser.parse_args()
app_launcher = AppLauncher(args_cli)
simulation_app = app_launcher.app

"""Rest of the code follows."""

import isaaclab.sim as sim_utils
from isaaclab.assets import AssetBaseCfg, RigidObjectCfg
from isaaclab.scene import InteractiveScene, InteractiveSceneCfg
from isaaclab.sim import SimulationContext
from isaaclab.utils import configclass


@configclass
class HelloSceneCfg(InteractiveSceneCfg):
    """A minimal scene: ground plane + light + one falling cube."""

    # Ground plane
    ground = AssetBaseCfg(
        prim_path="/World/defaultGroundPlane",
        spawn=sim_utils.GroundPlaneCfg(),
    )

    # Dome light for visibility
    dome_light = AssetBaseCfg(
        prim_path="/World/DomeLight",
        spawn=sim_utils.DomeLightCfg(intensity=3000.0, color=(0.75, 0.75, 0.75)),
    )

    # A single cube that falls onto the ground
    cube = RigidObjectCfg(
        prim_path="/World/Cube",
        spawn=sim_utils.CuboidCfg(
            size=(0.5, 0.5, 0.5),
            rigid_props=sim_utils.RigidBodyPropertiesCfg(),
            mass_props=sim_utils.MassPropertiesCfg(mass=1.0),
            physics_material=sim_utils.RigidBodyMaterialCfg(
                static_friction=1.0, dynamic_friction=1.0, restitution=0.0
            ),
        ),
        init_state=RigidObjectCfg.InitialStateCfg(pos=(0.0, 0.0, 3.0)),
    )


def run_simulator(sim: SimulationContext, scene: InteractiveScene):
    """Run the simulation loop."""
    cube = scene["cube"]

    print("[INFO]: Simulation started! Cube is falling onto the ground plane.")
    print("[INFO]: Close the Isaac Sim window or press Ctrl+C to stop.\n")

    count = 0
    while simulation_app.is_running():
        # Reset every 500 steps so the cube falls again
        if count % 500 == 0:
            scene.reset()

        sim.step()
        cube.write_data_to_sim()
        count += 1

        if count % 100 == 0:
            pos = cube.data.root_pos_w[0]
            print(f"[INFO]: Step {count} -- Cube position: "
                  f"({pos[0].item():.2f}, {pos[1].item():.2f}, {pos[2].item():.2f})")


def main():
    """Main function."""
    # Initialize simulation context
    sim_cfg = sim_utils.SimulationCfg(dt=0.01, render_interval=1)
    sim = SimulationContext(sim_cfg)
    sim.set_camera_view(eye=(4.0, 3.0, 4.0), target=(0.0, 0.0, 0.0))

    # Create scene from config
    print("[INFO]: Creating scene...")
    scene_cfg = HelloSceneCfg(num_envs=1, env_spacing=4.0)
    scene = InteractiveScene(scene_cfg)

    # Play the simulator
    sim.reset()

    # Run!
    run_simulator(sim, scene)


if __name__ == "__main__":
    main()
    simulation_app.close()
