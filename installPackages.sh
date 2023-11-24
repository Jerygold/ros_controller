#!/bin/bash

pip install evdev

rosdep install -i --from-path src --rosdistro humble -y

colcon build 

source install/setup.bash