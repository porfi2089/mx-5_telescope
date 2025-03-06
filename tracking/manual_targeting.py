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
    if axis1 < 0.1 and axis1 > -0.1:
        axis1 = 0
    axis2 = joystick.get_axis(1)  # Up-down axis of the first stick
    if axis2 < 0.1 and axis2 > -0.1:
        axis2 = 0
    axis3 = joystick.get_axis(2)  # Left-right axis of the second stick
    if axis3 < 0.1 and axis3 > -0.1:
        axis3 = 0
    axis4 = joystick.get_axis(3)  # Up-down axis of the second stick
    if axis4 < 0.1 and axis4 > -0.1:
        axis4 = 0

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


targets = []
selected_target = 0
while True:
    ret, frame = input_video.read()
    if not ret:
        break
    
    axis, buttons = get_joystick_data()
    if targets is None:
        selected_target = 0
    else:

        target1.move(int(axis[0][0] * 10), int(axis[0][1] * 10))
        if buttons[4]:
            target1.set_size(target1.size + 2)
        if buttons[5]:
            target1.set_size(target1.size - 2)
        if buttons[6]:
            if selected_target > 0:
                selected_target -= 1
            else:
                selected_target = len(targets)-1

        if buttons[0] and not target1.tracking:
            target1.intialize_track(frame)
        if buttons[1]:
            target1.stop_track()

        if target1.tracking:
            target1.update_track(frame)    

        for n, target in enumerate(targets):
            if n == selected_target:
                target.draw(frame)
            else:
                target.draw(frame)


    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

    

