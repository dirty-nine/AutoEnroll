import ActionHelpers as act
import ImageDetect as imd
import os
#only works in chrome, dark mode browser

dir_path = os.path.dirname(os.path.realpath(__file__))

def setup():
    '''
    make sure on chrome/edge
    make sure its full screen
    make sure its on correct tab zoom
    make sure its on couses shopping cart tab
    '''
    act.delay(1)
    
    act.hold('ctrlleft')
    for _ in range(15):
        act.keyPress('-')
    for _ in range(7):
        act.keyPress('+')
    act.unhold('ctrlleft')
    print('done')
setup()
    

def findEnroll():
    
    enroll_button_path = imd.findIconConfidence(f"{dir_path}\enroll_button.PNG")
    finish_enrolling_button_path = imd.findIconConfidence(rf"{dir_path}\finish_enrolling_button.PNG")
    
    
import time
a = True
while a:
    
    start = time.time()
    
    findEnroll()
    
    print(f"Time: {time.time() - start} seconds")
    a = False