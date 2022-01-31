from pyautogui import *
import pyautogui
import keyboard
import time

while keyboard.is_pressed('q') == False:
        
    if pyautogui.pixel(815, 980)[1] == 211:
        keyboard.press("d")
        time.sleep(0.006)
        keyboard.release("d")
        print("Key: d")
    if pyautogui.pixel(916, 980)[0] == 254:
        keyboard.press("f")
        time.sleep(0.006)
        keyboard.release("f")
        print("Key: f")
    if pyautogui.pixel(1006, 980)[0] == 254:
        keyboard.press("j")
        time.sleep(0.006)
        keyboard.release("j")
        print("Key: j")
    if pyautogui.pixel(1105, 980)[1] == 211:
        keyboard.press("k")
        time.sleep(0.006)
        keyboard.release("k")
        print("Key: k")