from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    IncludeLaunchDescription,
    OpaqueFunction,
)
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def launch_setup(context, *args, **kwargs):

    vrx_gz_prefix = get_package_share_directory("vrx_gz")
    no_gui = str(context.perform_substitution(LaunchConfiguration("no_gui")))

    extra_gz_args = "-v -s 0" if no_gui == "true" else "-v 0"
    sim_ld = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([vrx_gz_prefix, "/launch/competition.launch.py"]),
        launch_arguments={
            "world": "follow_path_task.sdf",
            "extra_gz_args": extra_gz_args,
        }.items(),
    )

    return [
        sim_ld,
    ]


def generate_launch_description():
    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "no_gui", default_value="false", choices=["true", "false"]
            ),
            OpaqueFunction(function=launch_setup),
        ]
    )
