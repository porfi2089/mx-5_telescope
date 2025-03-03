import cv2 as cv
import numpy as np
import pygame
import serial
import time

# Initialize Pygame and the joystick
pygame.init()
pygame.joystick.init()

# Check if a joystick is connected
if pygame.joystick.get_count() == 0:
    print("No joystick connected.")
    exit()

# Initialize the first joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()

def get_joystick_data():
    # Handle joystick events
    pygame.event.pump()

    # Get values from the joystick axes
    axis1 = joystick.get_axis(0)  # Left-right axis of the first stick
    axis2 = joystick.get_axis(1)  # Up-down axis of the first stick

    # Convert axis values from range [-1, 1] to [0, 1023]
    axis1 = int((axis1 + 1) * 511.5)  # Map to 0-1023
    axis2 = int((axis2 + 1) * 511.5)  # Map to 0-1023

    axis = (axis1, axis2)

    # Get the state of a button (button 0 in this case)
    button0 = joystick.get_button(0)  # Boolean (pressed or not)
    button1 = joystick.get_button(1)  # Boolean (pressed or not)
    button2 = joystick.get_button(2)  # Boolean (pressed or not)
    button3 = joystick.get_button(3)  # Boolean (pressed or not)
    button4 = joystick.get_button(4)  # Boolean (pressed or not)
    button5 = joystick.get_button(5)  # Boolean (pressed or not)
    button6 = joystick.get_button(6)  # Boolean (pressed or not)
    button7 = joystick.get_button(7)  # Boolean (pressed or not)

    buttons = (button0, button1, button2, button3, button4, button5, button6, button7)

    return axis, buttons

try:
    while True:
        # Get joystick data
        axis, buttons = get_joystick_data()

        # Print the joystick data
        print("Axis: ", axis)
        print("Buttons: ", buttons)
        print()

except KeyboardInterrupt:
    print("Program interrupted by user")

finally:
    # Close the serial port and quit pygame
    pygame.quit()
