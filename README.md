# Gantry Simulation (ROS 2 + Gazebo)

This repository provides a ready-to-use Docker environment for simulating a 3-axis gantry robot in ROS 2 Humble + Gazebo.

---

## Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/gantry_simulation.git
cd gantry_simulation
```

### 2. Build the container
```bash
docker build -t gantry_sim:latest .
```

### 3. Run with GUI (Linux)
```bash
xhost +local:root
docker run -it --net=host \
  --env="DISPLAY=$DISPLAY" \
  --env="QT_X11_NO_MITSHM=1" \
  --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
  gantry_sim:latest
```
or
```bash
xhost +local:root
docker-compose up
```

### 4. Test the simulation
```bash
ros2 launch gantry_sim gantry.launch.py
```

## Contributing

### 1. Make changes in gantry_ws/src/gantry_sim
### 2. Rebuild inside container (then exit):
```bash
cd ~/gantry_ws
colcon build
```
### 3. Commit and push changes:
```bash
git add .
git commit -m "Added Z-axis limit update"
git push
```
