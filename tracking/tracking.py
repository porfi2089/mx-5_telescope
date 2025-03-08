import cv2 as cv
import numpy as np

def get_star_position(frame: cv.typing.MatLike) -> list[int, int]:
    """Get the average position of the star in the frame"""
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    avrg_pos = [0, 0]
    for i in range(gray.shape[0]):
        for j in range(gray.shape[1]):
            avrg_pos[1] += i * (gray[i, j]/255)
            avrg_pos[0] += j * (gray[i, j]/255)
    print(avrg_pos)
    avrg_pos[0] /= gray.shape[0]*gray.shape[0]*gray.mean()/255
    avrg_pos[1] /= gray.shape[0]*gray.shape[0]*gray.mean()/255
    avrg_pos = [int(avrg_pos[0]), int(avrg_pos[1])]
    return avrg_pos

class target:
    """target class"""
    def __init__(self, x:int, y:int, size:int, frame:cv.typing.MatLike) -> None:
        self.x = x
        self.y = y
        self.size = size
        self.limit_x = frame.shape[1]
        self.limit_y = frame.shape[0]
        self.tracking = False

    def move(self, dx:int, dy:int) -> bool:
        if self.tracking:
            return False
        
        
        self.x += dx
        self.y += dy
        
        if self.x < 0:
            self.x = 0
        elif (self.x + self.size) > self.limit_x:
            self.x = self.limit_x - self.size

        if self.y < 0:
            self.y = 0
        elif (self.y + self.size) > self.limit_y:
            self.y = self.limit_y - self.size
        return True

    def set_position(self, x:int, y:int) -> bool:
        if x < 0 or x > self.limit_x:
            return False
        if y < 0 or y > self.limit_y:
            return False
        if self.tracking:
            return False
        
        self.x = x
        self.y = y
        return True

    def get_position(self) -> tuple[int, int]:
        return self.x, self.y
    
    def set_size(self, size: int) -> bool:
        if size < 0:
            return False
        if (self.x + size) > self.limit_x:
            return False
        if (self.y + size) > self.limit_y:
            return False
        if self.tracking:
            return False
        
        self.size = size
        return True
    
    def draw(self, frame:cv.typing.MatLike, selected:bool = False) -> None:
        color = (0, 0, 255)
        if self.tracking:
            color = (0, 255, 0)
            cv.circle(frame, (self.x + self.pos[0], self.y + self.pos[1]), 5, (0, 255, 0), -1)
            cv.circle(frame, (self.x + self.pos_start[0], self.y + self.pos_start[1]), 5, (0, 255, 0), -1)
        if selected:
            cv.rectangle(frame, (self.x-4, self.y-4), (self.x + self.size+4, self.y + self.size+4), (255, 0, 0), 2)
        cv.rectangle(frame, (self.x, self.y), (self.x + self.size, self.y + self.size), color, 2)

    def intialize_track(self, frame:cv.typing.MatLike) -> bool:
        roi = frame[self.y:self.y + self.size, self.x:self.x + self.size]
        if roi.max() - roi.min() < 10:
            return False 
        self.pos_start = get_star_position(roi)
        self.tracking = True
        return True
    
    def update_track(self, frame:cv.typing.MatLike) -> bool:
        if self.tracking == False:
            return False
        roi = frame[self.y:self.y + self.size, self.x:self.x + self.size]
        
        self.pos = get_star_position(roi)
        self.error = [self.pos[0] - self.pos_start[0], self.pos[1] - self.pos_start[1]]
        return True
    
    def get_error(self) -> list[int, int]:
        return self.error
    
    def stop_track(self) -> None:
        self.tracking = False

