
"""
VIDEO.PY

SOURCE:"https://www.geeksforgeeks.org/python-opencv-capture-video-from-camera/"

"""

import cv2
import os
from datetime import datetime

def function_to_take_video():
    # Define the video capture object
    vid = cv2.VideoCapture(0)

    # Get the default resolutions of the frame
    frame_width = int(vid.get(3))
    frame_height = int(vid.get(4))
    resolution = (frame_width, frame_height)

    # Define the codec and create VideoWriter object
    codec = cv2.VideoWriter_fourcc(*'mp4v')  # or 'XVID' for AVI

    # Create a timestamp for unique filenames
    timestamp = datetime.now()
    file_name = f"my_video_{timestamp.strftime('%Y-%m-%d_%H-%M-%S')}.mp4"

    # Define the output folder and file path
    output_folder = "saved_gallery/videos"
    output_file = os.path.join(output_folder, file_name)

    fps = 60.0  # Frames per second

    # Create VideoWriter object
    out = cv2.VideoWriter(output_file, codec, fps, resolution)

    while True:
        # Capture the video frame by frame
        ret, frame = vid.read()
        
        if not ret:
            break

        # Write the frame to the output file
        out.write(frame)

        # Display the resulting frame
        cv2.imshow('frame', frame)

        # The 'q' button is set as the quitting button
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture object and the VideoWriter object
    vid.release()
    out.release()
    
    # Destroy all the windows
    cv2.destroyAllWindows()

    return output_file, timestamp
