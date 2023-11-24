#!/bin/bash

pip install evdev

rosdep install -i --from-path src --rosdistro humble -y

colcon build --packages-select py_manette_ps4 ps4_messages

source install/setup.bash