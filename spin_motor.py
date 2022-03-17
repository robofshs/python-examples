# This is an EV3Dev example for spinning the motor
# It powers port A, presuming it is a large motor

# Import LargeMotor, SpeedPercent and OUTPUT_A 
# modules from EV3Dev. LargeMotor is a large LEGO 
# motor, SpeedPercent is how we set the speed on 
# the motor (because setting speed is a little more
# complicated then just indicating a number) so we 
# need an object to do it for us and OUTPUT_A is the
# A output port on an EV3 brick

from ev3dev2.motor import LargeMotor, SpeedPercent,  OUTPUT_A

# Create a variable to control the large motor,
# specifying the OUTPUT_A port

motor = LargeMotor(OUTPUT_A)

# Use LargeMotor#on_for_rotations to turn the large
# motor on for a certian number of rotations (in
# this case, 50). LargeMotor#on_for_rotations takes
# two paramaters - a SpeedPercent object for speed,
# and an integer for number of rotations

motor.on_for_rotations(SpeedPercent(100), 50)