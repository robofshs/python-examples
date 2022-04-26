# This is an EV3Dev example logging the values
# from a light sensor

# Import ColorSensor and INPUT_1 objects from EV3Dev.
# ColorSensor is a colour sensor, and INPUT_1 is the
# input 1 port on an EV3 brick

# Be aware that, since ColorSensor is in a seperate 
# subdirectory of sensor (sensor.lego), it must be
# imported using a seperate import statment

from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1

# Import sleep from time, to let us do delays

from time import sleep

# Create a variable to control the colour sensor,
# specifying the OUTPUT_A port

colour_sensor = ColorSensor(INPUT_1)

# Enter loop that we will repeat every 2 seconds,
# forever. This isn't a good idea; it's just quick.
# I'll show you a better way to do this in class!
# This loop will contain all of the sampling code.

while True:

    # Create a variable which we record data to as a 
    # "buffer", then print. 
    #
    # Our buffer is an intemdiary stage - and technically
    # we could go straight to printing - but this makes
    # the code a bit more readable, and also lets us 
    # access this same value from other places if we want 
    # to expand this program later without having to
    # make a posisbly time-consuming call to our colour
    # sensor.
    #
    # This doesn't have to be an
    # list of values, but this makes it more re-usable
    # for different area of our code.
    #
    # Record the following data to the buffer:
    #   - color_name
    #   - raw
    #   - rgb

    buffer = [colour_sensor.color_name, colour_sensor.raw, colour_sensor.rgb]

    # Print this out to console with labels

    print("CS Readings: color_name = {color_name}, raw = {raw}, rgb = {rgb}".format(colour_name = buffer[0], raw = buffer[1], rgb = buffer[2]))

    # Wait 2 seconds before the next loop

    sleep(2)
