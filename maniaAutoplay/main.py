from pyautogui import *
import pyautogui
import keyboard

while keyboard.is_pressed('q') == False:
        
    if pyautogui.pixel(815, 980)[1] == 211:
        keyboard.press_and_release("d")
        print("Key: d")
    if pyautogui.pixel(916, 980)[0] == 254:
        keyboard.press_and_release("f")
        print("Key: f")
    if pyautogui.pixel(1006, 980)[0] == 254:
        keyboard.press_and_release("j")
        print("Key: j")
    if pyautogui.pixel(1105, 980)[1] == 211:
        keyboard.press_and_release("k")
        print("Key: k")