"""

Capture Current X,Y Cord Of Cursor - Landen Fisher - 10/2/2022

Requirements:

    pip install pyautogui

    pip install colored

    pip install keyboard

"""


# Import Pyautogui To Get Mouse
import pyautogui

# Import OS 
import os

# Import Keyboard To Get User Input
import keyboard

# Import Colored Terminal 
import colored

# Import Colored Terminals Ability To Style Text
from colored import stylize


# Check For User Input Forever
while True:

    # Check If Ctrl + Shift Is Pressed
    if keyboard.is_pressed("ctrl+shift"):

        # Clear Previous Console Output
        os.system('cls')

        # Capture Mouse X And Y Into Variables      
        currentMouseX, currentMouseY = pyautogui.position()
        
        # Print Cords In Green Text
        print(stylize("Current Mouse X Cord: " + str(currentMouseX) + " : " + "Current Mouse Y Cord: " + str(currentMouseY) + "  (" + str(currentMouseX) + ", " + str(currentMouseY) + ")" , colored.fg("green")))
