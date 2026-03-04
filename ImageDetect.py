import cv2
import mss 
import numpy as np
import logging

def findIconConfidence(templatePath, x1 = 0, y1 = 0, x2 = 0, y2 = 0):
    # get screen width and height
    left = x1 
    top = y1
    width = x2-x1
    height = y2-y1
    if (x2 == 0 or y2 == 0):
        with mss.mss() as sct:
            monitor = sct.monitors[1]  # primary monitor
            width = monitor["width"]
            height = monitor["height"]
            
    template = cv2.imread(rf"{templatePath}")

    #get screenshot of screen
    region = {'top': top, 'left': left, 'width': width, 'height': height} #top is top left corner's y, left is its x
    with mss.mss() as sct:
        screenshot = sct.grab(region) 
        
    # reformat screenshot for in usable cv2 format
    img = np.array(screenshot)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    #get confidence
    result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    confidence = result.max()
    return(confidence)

def findIconLocation(templatePath, x1 = 0, y1 = 0, x2 = 0, y2 = 0):
    # get screen width and height
    left = x1 
    top = y1
    width = x2-x1
    height = y2-y1
    if (width == 0 or height == 0):
        with mss.mss() as sct:
            monitor = sct.monitors[1]  # primary monitor
            width = monitor["width"]
            height = monitor["height"]  
    template = cv2.imread(rf"{templatePath}")
    #get screenshot of screen
    region = {'top': top, 'left': left, 'width': width, 'height': height} #top is top left corner's y, left is its x
    with mss.mss() as sct:
        screenshot = sct.grab(region) 
    # reformat screenshot for in usable cv2 format
    img = np.array(screenshot)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    #get confidence
    result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    confidence = result.max()
    
    if confidence > 0.9:
        # Extract the confidence and the top-left coordinate of the best match
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        # max_loc is (x, y) relative to your 'region' screenshot
        match_x, match_y = max_loc
        # Adjust for the global screen position (if you provided top/left offsets)
        screen_x = match_x + left
        screen_y = match_y + top
        # Optional: Calculate the center of the icon
        h, w = template.shape[:2]
        center_x = screen_x + (w // 2)
        center_y = screen_y + (h // 2)
        return {
            "confidence": max_val,
            "top_left": (screen_x, screen_y),
            "center": (center_x, center_y)
        }
    return {
        "confidence": confidence,
        "top_left": (0,0),
        "center": (0,0)
    }