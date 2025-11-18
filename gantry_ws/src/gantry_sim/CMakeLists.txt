cmake_minimum_required(VERSION 3.8)
project(gantry_sim)

# Default to C++17
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()

# Find required packages
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(gazebo_ros REQUIRED)

# -------------------------------------------------------------------
# (OPTIONAL) Build C++ nodes here
# Uncomment and modify if you add C++ executables later
#
# add_executable(gantry_controller src/gantry_controller.cpp)
# ament_target_dependencies(gantry_controller rclcpp gazebo_ros)
#
# install(
#   TARGETS gantry_controller
#   DESTINATION lib/${PROJECT_NAME}
# )
# -------------------------------------------------------------------

# Install launch files and URDF
install(
  DIRECTORY launch urdf
  DESTINATION share/${PROJECT_NAME}
)

# Install config or meshes if you add them later:
# install(
#   DIRECTORY config meshes
#   DESTINATION share/${PROJECT_NAME}
# )

ament_package()
