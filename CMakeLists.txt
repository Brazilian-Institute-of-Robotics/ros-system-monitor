cmake_minimum_required(VERSION 2.8.3)

project(system_monitor)

find_package(catkin)

catkin_package()

catkin_python_setup()

install(
  DIRECTORY config launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  USE_SOURCE_PERMISSIONS
)

install(
  PROGRAMS 
    src/cpu_monitor.py
    src/hdd_monitor.py
    src/mem_monitor.py
    src/net_monitor.py
    src/ntp_monitor.py
  DESTINATION 
    ${CATKIN_PACKAGE_BIN_DESTINATION}
)
