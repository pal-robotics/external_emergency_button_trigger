# external_emergency_button_trigger

This package contains example node(s) on how to use the external emergency stop trigger via software to stop the current controllers that are controlling any joint in the robot.


This can be done just by publishing into the topic `/external_stop_trigger` with a message of type `std_msgs/Bool` of value `True`.

## keyboard_emergency.py

Example node that when pressed any key triggers the emergency stop.

````
rosrun external_emergency_button_trigger keyboard_emergency.py 
[INFO] [WallTime: 1456936400.106729] 


Press ANY KEY to trigger emergency stop.


Stop with Control+C+Enter.
[WARN] [WallTime: 1456936403.549429] Publishing emergency stop trigger! (pressed ' ')
````

