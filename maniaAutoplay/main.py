from pyautogui import *
import pyautogui
import keyboard
import time

while keyboard.is_pressed('q') == False:
        
    if pyautogui.pixel(750, 960)[0] != 0:
        keyboard.press("a")
        keyboard.release("a")
        print("Key: a")
    if pyautogui.pixel(890, 960)[0] != 0:
        keyboard.press("s")
        keyboard.release("s")
        print("Key: s")
    if pyautogui.pixel(1028, 960)[0] != 0:
        keyboard.press("k")
        keyboard.release("k")
        print("Key: k")
    if pyautogui.pixel(1160, 960)[0] != 0:
        keyboard.press("l")
        keyboard.release("l")
        print("Key: l")