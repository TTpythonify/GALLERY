"""
SCREENRECORD.PY

SOURCE:"https://www.geeksforgeeks.org/create-a-screen-recorder-using-python/"

"""
import pyautogui
import cv2
import numpy as np
import os
from datetime import datetime

def function_to_screen_record():
    # Define the resolution and codec
    resolution = (1920, 1080)
    codec = cv2.VideoWriter_fourcc(*"mp4v")
    fps = 60.0

    # Create a timestamp for filenames
    timestamp = datetime.now()
    file_name = f"screen_record_{timestamp.strftime('%Y-%m-%d_%H-%M-%S')}.mp4"

    output_folder = "gallery/screenrecord"

    output_file = os.path.join(output_folder, file_name)

    # Create a VideoWriter object
    out = cv2.VideoWriter(output_file, codec, fps, resolution)

    # Create an empty window for displaying the live feed
    cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Live", 480, 270)

    while True:
        # Take a screenshot using PyAutoGUI
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        out.write(frame)

        # Display the recording screen
        cv2.imshow('Live', frame)

        # Check if 'q' is pressed to stop recording
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the VideoWriter and destroy all windows
    out.release()
    cv2.destroyAllWindows()

    # Return the file path and timestamp
    return output_file, timestamp
