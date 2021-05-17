#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

class Test(object):

	def __init__(self):
		# First initialize `moveit_commander`_ and a `rospy`_ node:
		rospy.init_node('test', anonymous=True)
		moveit_commander.roscpp_initialize(sys.argv)
		# Provides information such as the robot’s kinematic model and the robot’s current joint states
		self.robot = moveit_commander.RobotCommander()
		# Provides a remote interface for getting, setting, and updating the robot’s internal understanding of the surrounding world
		self.scene = moveit_commander.PlanningSceneInterface()
		# an interface to a planning group (group of joints) - end effector and manipulator parameters
		self.move_group = moveit_commander.MoveGroupCommander('manipulator')
		# display trajectories in Rviz
		self.display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory)
		# obtain the necessary geometry information  such as pose that include position and orientation
		self.pose_goal = geometry_msgs.msg.Pose()
		# checking the group name for UR5 arms - end effector and manipulator should show up
		self.group_name = self.robot.get_group_names()


	def get_goal_pose(self):
		joint_state = self.move_group.get_current_pose()
		return joint_state

	def home(self):
		self.move_group.set_named_target('up')
		plan = self.move_group.plan()
		self.move_group.execute(plan, wait=True)
		self.robot.get_current_state()
		print(self.get_goal_pose())
		self.move_group.stop()
		self.move_group.clear_pose_targets()

	def transformation_to_pose(self):
		# for changing it pose
		self.pose_goal.orientation.w = 0.1
		self.pose_goal.position.x = 0.1
		self.pose_goal.position.y = 0.1
		self.pose_goal.position.z = 0.1
		self.move_group.set_pose_target(self.pose_goal)
		# Now, we call the planner to compute the plan and execute it.
		plan = self.move_group.go(wait=True)
		print(self.get_goal_pose())
		# Calling `stop()` ensures that there is no residual movement
		self.move_group.stop()
		# It is always good to clear your targets after planning with poses.
		# Note: there is no equivalent function for clear_joint_value_targets()
		self.move_group.clear_pose_targets()

# # Add base box

# p = geometry_msgs.msg.PoseStamped()
# p.header.frame_id = robot.get_planning_frame()
# p.pose.position.x = 0.
# p.pose.position.y = -0.045
# p.pose.position.z = -0.03
# scene.add_box("table", p, (0.6, 1.2, 0.05))

def main():

	try:
		test = Test()
		test.home()
		test.transformation_to_pose()

	except rospy.ROSInterruptException:
	 	return
	except KeyboardInterrupt:
	    return

if __name__ == '__main__':
	main()

