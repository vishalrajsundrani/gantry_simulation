from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg_gantry = get_package_share_directory('gantry_sim')

    # Path to URDF
    urdf_file = os.path.join(pkg_gantry, 'urdf', 'gantry.urdf.xacro')

    # Gazebo launch file
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
        ])
    )

    # Spawn model node
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-entity', 'gantry', '-file', urdf_file],
        output='screen'
    )

    return LaunchDescription([gazebo, spawn_entity])
