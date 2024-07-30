"""
SCREENSHOT.PY

SOURCE:"https://www.geeksforgeeks.org/how-to-take-screenshots-using-python/"

"""

import pyautogui
import os
import datetime

def function_to_take_screenshot():
    image = pyautogui.screenshot()
    timestamp = datetime.datetime.now()
    
    # Create a file path with the timestamp
    file_name = f"screenshot_{timestamp.strftime('%Y-%m-%d_%H-%M-%S')}.png"
    folder_path = "gallery/screenshots"
    file_path = os.path.join(folder_path, file_name)
    
    # Ensure the directory exists
    os.makedirs(folder_path, exist_ok=True)
    
    # Save the screenshot
    image.save(file_path)

    return file_path, timestamp