import random
import time
import pyautogui
import win32api
import win32con
import cv2 as cv
import numpy as np

# Variabile di stato per controllare se il primo clic è stato già effettuato
first_click_done = False


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def kbPress(x):
    pyautogui.keyDown(x)
    time.sleep(random.randint(1, 3))
    pyautogui.keyUp(x)


def findBattle():
    kbPress('space')
    kbPress('k')


for i in range(1, 10):
    # Finding Village
    time.sleep(5)
    findBattle()
    time.sleep(random.randint(10, 15))

    # Firt Village
    time.sleep(3)
    time.sleep(random.randint(1, 2))
    kbPress('space')
    click(926, 14)
    time.sleep(1)
    kbPress('1')
    click(204, 413)
    time.sleep(random.uniform(0.3, 0.8))
    click(458, 240)
    time.sleep(random.uniform(0.3, 0.8))
    click(695, 69)
    time.sleep(random.uniform(0.3, 0.8))
    click(1325, 146)
    time.sleep(random.uniform(0.3, 0.8))
    click(1448, 291)
    time.sleep(random.uniform(0.3, 0.8))
    click(1448, 291)
    time.sleep(70)

    # Second village
    kbPress('space')
    click(1029, 49)
    kbPress('7')
    click(347, 425)
    time.sleep(random.uniform(0.3, 0.8))
    click(604, 238)
    time.sleep(random.uniform(0.3, 0.8))
    click(823, 106)
    time.sleep(random.uniform(0.3, 0.8))
    click(547, 786)
    time.sleep(random.uniform(0.3, 0.8))
    click(1277, 82)
    time.sleep(random.uniform(0.3, 0.8))
    click(1450, 250)
    time.sleep(random.uniform(0.3, 0.8))
    click(1536, 315)
    time.sleep(random.uniform(0.3, 0.8))
    click(534, 805)
    time.sleep(65)
    kbPress('p')
    time.sleep(random.uniform(4, 7))
