import cv2 as cv
import numpy as np
import time


class target:
    """target class"""
    def __init__(self, x, y, size, limit_x, limit_y):
        self.x = x
        self.y = y
        self.size = size
        self.limit_x = limit_x
        self.limit_y = limit_y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

        if self.x < 0:
            self.x = 0
        elif (self.x + self.size) > self.limit_x:
            self.x = self.limit_x + self.size

        if self.y < 0:
            self.y = 0
        elif (self.y + self.size) > self.limit_y:
            self.y = self.limit_y - self.size

    def set_position(self, x:int, y:int) -> bool:
        if x < 0 or x > self.limit_x:
            return False
        
        if y < 0 or y > self.limit_y:
            return False
        
        self.x = x
        self.y = y
        return True

    def get_position(self) -> tuple[int, int]:
        return self.x, self.y
    
    def set_size(self, size: int) -> bool:
        if size < 0:
            return False
        self.size = size
        return True
    
    def draw(self, frame) -> None:
        cv.rectangle(frame, (self.x, self.y), (self.x + self.size, self.y + self.size), (0, 255, 0), 2)

    def intialize_track(self, frame) -> bool:
        roi = frame[self.y:self.y + self.size, self.x:self.x + self.size]
        gray = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
        
        return True, gray