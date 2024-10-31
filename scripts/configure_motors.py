import argparse

from lerobot.common.robot_devices.motors.dynamixel import DynamixelMotorsBus

def configure_motors(robot_cfg):
    leader_port = robot_cfg.leader_arms.main.port
    follower_port = robot_cfg.follower_arms.main.port
    
    leader_arm = DynamixelMotorsBus(
        port=leader_port,
        motors={
            # name: (index, model)
            "shoulder_pan": (1, "xl330-m077"),
            "shoulder_lift": (2, "xl330-m077"),
            "elbow_flex": (3, "xl330-m077"),
            "wrist_flex": (4, "xl330-m077"),
            "wrist_roll": (5, "xl330-m077"),
            "gripper": (6, "xl330-m077"),
        },
    )

    follower_arm = DynamixelMotorsBus(
        port=follower_port,
        motors={
            # name: (index, model)
            "shoulder_pan": (1, "xl430-w250"),
            "shoulder_lift": (2, "xl430-w250"),
            "elbow_flex": (3, "xl330-m288"),
            "wrist_flex": (4, "xl330-m288"),
            "wrist_roll": (5, "xl330-m288"),
            "gripper": (6, "xl330-m288"),
        },
    )
    
    print(f"Connect to leader_port: {leader_port}")
    leader_arm.connect()
    
    print(f"Connect to follower_port: {follower_port}")
    follower_arm.connect()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--robot-path",
        type=str,
        default="lerobot/configs/robot/koch.yaml",
        help="Path to robot yaml file used to instantiate the robot using `make_robot` factory function.",
    )
    parser.add_argument(
        "--robot-overrides",
        type=str,
        nargs="*",
        help="Any key=value arguments to override config values (use dots for.nested=overrides)",
    )
    args = parser.parse_args()
    robot_cfg = init_hydra_config(args.robot_path, args.robot_overrides)
    configure_motors(robot_cfg)
