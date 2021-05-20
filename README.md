# Universal-Robot-ROS (Python)
Working on using python to control UR arm in ROS. The functions been explored are using rviz to provide planning visualisation in RViz and Gazebo and also collision detection in actual deployment.

# Acknowledgement
The work done is based on [ur_modern_driver](https://github.com/ros-industrial/ur_modern_driver)

# Contents
- Test.py to allow the arm execute 3 command - Home, Up and a specific orientation through set_pose_target

![TestUR5](https://user-images.githubusercontent.com/67405818/118764854-bc6bd000-b8ac-11eb-9b8a-90ff74ed786c.gif)

# Collision Avoidance
The benefits of running ROS include the ability to visualise it in Gazebo or provide collision aovidance in Moveit. Below is the code i have inserted into the URDF file for my UR5 to add a table and activate collision avodiance for the table

    <link name="table">
      <visual>
        <geometry>
          <box size="1.2 1.2 0.05"/>
        </geometry>
       </visual>
       <collision>
         <geometry>
           <box size="1.2 1.2 0.05"/>
         </geometry>
       </collision>
    </link>

    <joint name="table_joint" type="fixed">
      <parent link="${prefix}base_link"/>
      <child link="table" />
      <origin rpy="0 0 0" xyz="0 0.5 -0.025"/>
    </joint>
    
<img src = "https://user-images.githubusercontent.com/67405818/118958054-a2f18380-b993-11eb-952b-8dd47c308338.png" width="300" height="280">








