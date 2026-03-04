import ActionHelpers as ah
import ImageDetect as imd
import os
import win32gui
import time
#only works in chrome, dark mode browser, with enrollemnt shopping cart already open

dir_path = os.path.dirname(os.path.realpath(__file__))

def setup():
    '''
    make sure on chrome/edge
    make sure its full screen
    '''
    if is_shopping_cart_focused():
        ah.hold('ctrlleft')
        ah.keyPress('0')
    
    '''
    check if on shopping cart tab
    '''

def is_shopping_cart_focused():
    hwnd = win32gui.GetForegroundWindow()
    window_title = win32gui.GetWindowText(hwnd)


    if "Google Chrome" in window_title and 'Enrollment Shopping Cart' in window_title:
        return True
    return False
    
def is_time(h, m, s):
    print(time.strftime("%H:%M:%S"))
    isHour = time.localtime().tm_hour >= h
    isMin = time.localtime().tm_min >= m
    isSec = time.localtime().tm_sec >= s
    return isHour and isMin and isSec

nig
a = True
while a:
    # start = time.time()
    # print(f"Time: {time.time() - start} seconds")

    
    targetTime = 11, 50, 30
    isTime = is_time(*targetTime)
    click_enroll()

    print(imd.findIconLocation(rf"{dir_path}\enroll_button.PNG")["center"])
    # a = not isTime