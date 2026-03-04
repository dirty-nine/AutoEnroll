import pyautogui
import time
import keyboard
import random
import win32api, win32con, win32gui


def click(x = None, y = None):
    if (x == None and y == None):
        x, y = win32api.GetCursorPos()
    win32api.SetCursorPos((int(x), int(y)))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)##shortDelay()
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
   
def keyPress(key):
    pyautogui.keyDown(key)
    time.sleep(0.008)
    pyautogui.keyUp(key)

def getPixelColor(x, y):
    r, g, b = pyautogui.pixel(int(x), int(y))
    return (r, g, b)

def getRandomCoordNearCenter():
    return (random.random()*6+957, random.random()*6+837)

def delay(s = None): 
    if not s:
        time.sleep(random.random()*0.01+0.06)
    else: time.sleep(s)
    
def hold(key, delay = None):
    pyautogui.keyDown(key)
    if delay:
        time.sleep(delay)
        pyautogui.keyUp(key)
    
def unhold(key):
    pyautogui.keyUp(key)
    
def mouseHold(key, delay):
    pyautogui.mouseDown(button = key)
    time.sleep(delay)
    pyautogui.mouseUp(button = key)

def getPixelColor(x, y):
    r, g, b = pyautogui.pixel(int(x), int(y))
    return (r, g, b)
