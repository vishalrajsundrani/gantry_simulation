FROM osrf/ros:humble-desktop-full

# Install core dependencies
RUN apt-get update && apt-get install -y \
    gazebo \
    ros-humble-gazebo-ros-pkgs \
    ros-humble-xacro \
    ros-humble-rviz2 \
    python3-colcon-common-extensions \
    git build-essential && \
    rm -rf /var/lib/apt/lists/*

# Create workspace
RUN mkdir -p /root/gantry_ws/src
WORKDIR /root/gantry_ws

# Copy source code
COPY gantry_ws/src ./src

# Build the workspace
RUN /bin/bash -c "source /opt/ros/humble/setup.bash && colcon build"

# Source setup
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
RUN echo "source /root/gantry_ws/install/setup.bash" >> ~/.bashrc

CMD ["/bin/bash"]
