#!/usr/bin/env python3
import rclpy
import tf_transformations
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped

def create_pose_stamped(navigator:BasicNavigator,position_x,position_y,orientation_z):
    q_x,q_y,q_z,q_w = tf_transformations.quaternion_from_euler(0.0,0.0,orientation_z)
    pose = PoseStamped()
    pose.header.frame_id = 'map'
    pose.header.stamp = navigator.get_clock().now().to_msg()
    pose.pose.position.x = position_x
    pose.pose.position.y = position_y
    pose.pose.position.z = 0.0
    pose.pose.orientation.x = q_x
    pose.pose.orientation.y = q_y
    pose.pose.orientation.z = q_z
    pose.pose.orientation.w = q_w

    return pose

def main():
    rclpy.init()
    nav = BasicNavigator()

    initial_pose = create_pose_stamped(nav,0.0,0.0,0.0)
    nav.setInitialPose(initial_pose=initial_pose)

    nav.waitUntilNav2Active()

    goal_pose1 = create_pose_stamped(nav,2.0,3.0,-1.57)
    goal_pose2 = create_pose_stamped(nav,-2.0,4.0,1.57)
    goal_pose3 = initial_pose

    # nav.goToPose(goal_pose1)

    wayPoints = [goal_pose1,goal_pose2,goal_pose3]

    nav.followWaypoints(wayPoints)

    while not nav.isTaskComplete():
        feedback = nav.getFeedback()
        if feedback:
            print(feedback)

    print(nav.getResult())
    nav.lifecycleShutdown()
    rclpy.shutdown()

if __name__ == '__main__':
    main()