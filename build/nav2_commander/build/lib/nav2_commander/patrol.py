#!/usr/bin/env python3
import rclpy
import tf_transformations
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped

def create_pose(nav:BasicNavigator, x, y, yaw):

    qx, qy, qz, qw = tf_transformations.quaternion_from_euler(0,0,yaw)

    pose = PoseStamped()
    pose.header.frame_id = "map"
    pose.header.stamp = nav.get_clock().now().to_msg()

    pose.pose.position.x = x
    pose.pose.position.y = y
    pose.pose.orientation.x = qx
    pose.pose.orientation.y = qy
    pose.pose.orientation.z = qz
    pose.pose.orientation.w = qw

    return pose


def main():

    rclpy.init()

    nav = BasicNavigator()

    # initial pose
    initial_pose = create_pose(nav,0.0,0.0,0.0)
    nav.setInitialPose(initial_pose)

    nav.waitUntilNav2Active()

    # patrol points
    waypoints = [
        create_pose(nav,2.0,3.0,0.0),
        create_pose(nav,-2.0,4.0,1.57),
        create_pose(nav,-3.0,-2.0,3.14),
        create_pose(nav,0.0,0.0,0.0)
    ]

    while rclpy.ok():

        print("Starting patrol loop")

        nav.followWaypoints(waypoints)

        while not nav.isTaskComplete():

            feedback = nav.getFeedback()

            if feedback:
                print("Waypoint:", feedback.current_waypoint)

        result = nav.getResult()

        print("Patrol finished, restarting...")


    nav.lifecycleShutdown()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
