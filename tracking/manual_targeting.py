import cv2 as cv
import numpy as np
import pygame
import serial
import time
import tracking

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

input_video = cv.VideoCapture(0)
input_video.set(cv.CAP_PROP_FRAME_WIDTH, 640)
input_video.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

def get_joystick_data():
    # Handle joystick events
    pygame.event.pump()

    # Get values from the joystick axes
    axis1 = joystick.get_axis(0)  # Left-right axis of the first stick
    axis2 = joystick.get_axis(1)  # Up-down axis of the first stick
    axis3 = joystick.get_axis(2)  # Left-right axis of the second stick
    axis4 = joystick.get_axis(3)  # Up-down axis of the second stick
    
    for i in (axis1, axis2, axis3, axis4):
        if abs(i) < 0.1:
            i = 0

    axis = ((axis1, axis2), (axis3, axis4))

    # Get the state of a button (button 0 in this case)
    button0 = joystick.get_button(0)  # Boolean (pressed or not)
    button1 = joystick.get_button(1)  # Boolean (pressed or not)
    button2 = joystick.get_button(2)  # Boolean (pressed or not)
    button3 = joystick.get_button(3)  # Boolean (pressed or not)
    button4 = joystick.get_button(11)  # Boolean (pressed or not)
    button5 = joystick.get_button(12)  # Boolean (pressed or not)
    button6 = joystick.get_button(13)  # Boolean (pressed or not)
    button7 = joystick.get_button(14)  # Boolean (pressed or not)

    buttons = (button0, button1, button2, button3, button4, button5, button6, button7)

    return axis, buttons

target1 = tracking.target(320, 240, 50, 640, 480)

while True:
    ret, frame = input_video.read()
    if not ret:
        break
    
    axis, buttons = get_joystick_data()

    target1.move(int(axis[0][0] * 10), int(axis[0][1] * 10))
    if buttons[4]:
        target1.set_size(target1.size + 2)
    if buttons[5]:
        target1.set_size(target1.size - 2)

    target1.draw(frame)

    # Print the joystick data
    print("Axis: ", axis)
    print("Buttons: ", buttons)
    print()



    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

    

