import time
import keyboard
import random

while keyboard.is_pressed('esc') == False:
    time.sleep(.2)
    keyboard.press_and_release('up')
    print("up")
    time.sleep(.2)
    keyboard.press_and_release('ctrl+a, backspace')
    print("ctrl+a, delete")
    time.sleep(.2)
    keyboard.press_and_release('enter')
    print("enter")
    time.sleep(.2)
    keyboard.press_and_release('enter')
    print("enter")
    