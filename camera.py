import cv2
import os
from datetime import datetime

def function_to_take_picture():
    # Initialize the camera
    camera = cv2.VideoCapture(0)

    # Capture a single frame
    ret, frame = camera.read()

    file_path = None
    timestamp = None

    # Check if frame was captured successfully
    if ret:
        # Create a timestamp for the filename
        timestamp = datetime.now()
        file_name = f"picture{timestamp.strftime('%Y-%m-%d_%H-%M-%S')}.png"
        folder_path = "gallery/pictures"

        # Save the captured frame to a file
        file_path = os.path.join(folder_path, file_name)
        cv2.imwrite(file_path, frame)

    # Release the camera
    camera.release()
    cv2.destroyAllWindows()

    # Return the file path and timestamp
    return file_path, timestamp
