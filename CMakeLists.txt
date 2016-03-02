cmake_minimum_required(VERSION 2.8.3)
project(external_emergency_button_trigger)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)

catkin_package()

#############
## Install ##
#############

## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination
install(PROGRAMS
  scripts/keyboard_emergency.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
