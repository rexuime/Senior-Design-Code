import time
import threading
import cv2
import numpy as np
from cubeClasses import cubeSide
from cubeClasses import sideSquare

'''
    Global matrix for current state of cube which will be modified by threads
    May need fine locking to prevent threads from accessing same value of matrix
    Would have to create a separate class/structure for a single square
    Each square would include its value and a lock
    Would then be a matrix of side objects that have square objects as the data
    lock = threading.Lock()
    with lock:
'''

# Global array side objects 
sides = []

# Global variable to wait until Arduino is done turning motors
arduinoIsRunning = False

# Global variable to hold all threads
threads = []

# Global dictionary of colors
colors = {"green":'g',
          "red":'r',
          "blue":'b',
          "white":'w',
          "yellow":'y',
          "orange":'o'}

# OpenCV objects for cameras, find port values
cam1 = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(1)

def setUp():

    # Thread initialization
    global threads
    t1 = threading.Thread(target = p1)
    threads.append(t1)
    t2 = threading.Thread(target = p2)
    threads.append(t2)

    # sides list initialization
    global sides
    for i in range(6):
        sides.append(cubeSide(i))


# function to start threads and read the cube/modify global matrix
def readCube():

    global threads
    # Start all the threads
    for thread in threads:
        thread.start()

    # Wait for all the threads to finish
    for thread in threads:
        thread.join()

# may want to implement a function to check? not sure yet

# function for thread1 to do work for camera1/modify matrix
def p1():

    # Read colors 
    while True:
        # Capture a frame
        ret, frame = cam1.read()

        break

    # modify squareSide objects
    return
    
# function for thread2 to do work for camera2/modify matrix
def p2():

    # Read colors
    while True:
        # Capture a frame
        ret, frame = cam2.read()

        break
    
    # modify squareSide objects
    return

# function to decode matrix into move for motors
def decode():

    # return data which will be used in sendData function
    return  


if __name__ == "__main__":

    setUp()

    readCube()

    # Release the VideoCapture object
    cam1.release()
    cam2.release()