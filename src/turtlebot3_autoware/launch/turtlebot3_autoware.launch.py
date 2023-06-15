from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='pointcloud_to_laserscan',
            executable='laserscan_to_pointcloud_node',
            name='laserscan_to_pointcloud',
            remappings=[('scan_in', '/scan'),
                        ('cloud',  '/cloud')],
            parameters=[{'target_frame': '', 
                         'transform_tolerance': 0.01, 
                         'use_sim_time': True}]
        ),
        Node(
            package='turtlebot3_autoware',
            executable='ackermann_to_twist_node',
            name='ackermann_to_twist',
        ),
    ])
