# spiral using pyautogui

import pyautogui
import time

time.sleep(5)
pyautogui.click()  # make the window active
distance = 300
change = 20

while distance > 0:
    pyautogui.drag(distance, 0, duration=1)  # move right
    distance = distance - change
    pyautogui.drag(0, distance, duration=1)  # move down
    pyautogui.drag(-distance, 0, duration=1)  # move left
    distance = distance - change
    pyautogui.drag(0, -distance, duration=1)  # move up
