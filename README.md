ROS2 Autonomous Rover Navigation (Nav2)

Autonomous mobile robot simulation using the ROS2 Nav2 navigation stack with AMCL localization and waypoint patrol in Gazebo.

The robot can autonomously navigate in a mapped environment and follow predefined patrol routes using the Nav2 Simple Commander API.

Features

- Autonomous navigation using ROS2 Nav2
- AMCL localization with LiDAR
- Waypoint patrol system
- Custom URDF mobile robot
- Gazebo simulation
- ROS2 Simple Commander API
- Modular ROS2 packages

---

System Architecture
Gazebo Simulation
↓
Robot URDF + Sensors
↓
TF Tree
↓
AMCL Localization
↓
Nav2 Navigation Stack
↓
Waypoint Commander Node


---

Packages

nav2_robot_description
Contains robot description:

- URDF/Xacro files
- robot sensors
- RViz configuration

nav2_robot_bringup
Launch files for:

- Gazebo simulation
- robot spawn
- ROS-Gazebo bridge
- Nav2 bringup

nav2_commander
Autonomous control scripts using Nav2 Simple Commander.

Includes:

- goal navigation
- waypoint patrol

---

Installation

Requirements

- Ubuntu 24.04
- ROS2 Jazzy
- Gazebo

Install dependencies:

```bash
sudo apt install ros-jazzy-nav2-bringup
sudo apt install ros-jazzy-navigation2
```
Clone repository:
```bash
git clone https://github.com/YOUR_USERNAME/nav2_rover_navigation.git
cd nav2_rover_navigation
```
Build workspace:

```bash
colcon build
source install/setup.bash
```
Running the Simulation
Launch the robot and navigation stack:

```bash
ros2 launch nav2_robot_bringup nav2_robot_gazebo.launch.xml
```
Autonomous Waypoint Patrol
Run the patrol node:

```bash
ros2 run nav2_commander patrol
```
Map

The navigation uses a pre-built map:
maps/nav2_world.yaml
Generated using SLAM.

Technologies Used:

1.ROS2 Jazzy
2.Nav2 Navigation Stack
3.Gazebo
4.Python
5.URDF / Xacro
6.RViz2
7.TF2

nav_project
│
├── src
│   ├── nav2_robot_description
│   ├── nav2_robot_bringup
│   └── nav2_commander
│
├── maps
│
└── README.md

Author

Abhirup Chakraborty

Mechanical Engineering — NIT Silchar
Robotics | Autonomous Systems | AI
