import customtkinter as ctk
from tkinter import messagebox
from screenrecord import function_to_screen_record
from camera import function_to_take_picture
from screenshot import function_to_take_screenshot
from video import function_to_take_video
from database import *
from PIL import Image

create_table()

"""
This is the Parent class in which other classes inherit similar properties
"""

class BaseWindow(ctk.CTk):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.geometry("600x600")

        self.back_button = ctk.CTkButton(self, text="Back", command=self.go_back)
        self.back_button.place(x=10, y=10)

        self.image_frame = ctk.CTkScrollableFrame(self, width=500, height=370)
        self.image_frame.pack(expand=True, padx=20, pady=(60, 20))
        self.image_frame.pack_propagate(False) 

    def go_back(self):
        self.destroy()
        main() 

    def display_images(self, image_paths):
        row = 0
        col = 0
        for image_path in image_paths:
            try:
                ctk_image = self.load_image(image_path)
                image_label = ctk.CTkLabel(self.image_frame, image=ctk_image, text="")
                image_label.grid(row=row, column=col, padx=5, pady=5)

                col += 1
                if col == 3:
                    col = 0
                    row += 1
            except Exception as e:
                print(f"Error loading image: {e}")

    def load_image(self, image_path):
        try:
            pil_image = Image.open(image_path)
            pil_image = pil_image.resize((150, 150))
            return ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(150, 150))
        except Exception as e:
            print(f"Error loading image: {e}")
            return None


class PictureWindow(BaseWindow):
    def __init__(self):
        super().__init__("Camera")

        self.action_button = ctk.CTkButton(self, text="Capture Picture", command=self.take_picture)
        self.action_button.place(x=400, y=10)

        my_pictures = retrieve_from_database("camera")
        self.display_images(reversed(my_pictures))

    def take_picture(self):
        file_path, time = function_to_take_picture()
        add_to_gallery("camera", file_path, time)
        # Refresh the display to include the new image
        my_pictures = retrieve_from_database("camera")
        self.display_images(reversed(my_pictures))


class ScreenshotWindow(BaseWindow):
    def __init__(self):
        super().__init__("Screenshot")

        self.action_button = ctk.CTkButton(self, text="Screenshot", command=self.take_screen_shot)
        self.action_button.place(x=400, y=10)

        self.image_label = ctk.CTkLabel(self.image_frame)
        self.image_label.pack(pady=20)

        my_screenshots = retrieve_from_database("screenshot")
        self.display_images(reversed(my_screenshots))

    def take_screen_shot(self):
        file_path, time = function_to_take_screenshot()
        add_to_gallery("screenshot", file_path, time)
        my_screenshots = retrieve_from_database("screenshot")
        self.display_images(reversed(my_screenshots))



class VideoWindow(BaseWindow):
    def __init__(self):
        super().__init__("Video")

        self.action_button = ctk.CTkButton(self, text="Capture Video", command=self.take_video)
        self.action_button.place(x=400, y=10)

        self.image_label = ctk.CTkLabel(self.image_frame)
        self.image_label.pack(pady=20)

    def take_video(self):
        messagebox.showinfo("Information", 'Press "q" to stop recording')
        file_path, time = function_to_take_video()
        add_to_gallery("video", file_path, time)


class ScreenrecordWindow(BaseWindow):
    def __init__(self):
        super().__init__("Screenrecord")

        self.action_button = ctk.CTkButton(self, text="Screen Record", command=self.take_screen_record)
        self.action_button.place(x=400, y=10)

        self.image_label = ctk.CTkLabel(self.image_frame)
        self.image_label.pack(pady=20)

    def take_screen_record(self):
        messagebox.showinfo("Information", 'Press "q" to stop recording')
        file_path, time = function_to_screen_record()
        add_to_gallery("screenrecord", file_path, time)




class Gallery(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gallery")
        self.geometry("400x300")
        
        # Create buttons
        self.camera_button = ctk.CTkButton(self, text="Camera", command=self.open_picture_window)
        self.video_button = ctk.CTkButton(self, text="Video", command=self.open_video_window)
        self.screenshot_button = ctk.CTkButton(self, text="Screenshot", command=self.open_screenshot_window)
        self.screenrecord_button = ctk.CTkButton(self, text="Screenrecord", command=self.open_screenrecord_window)

        # Grid configuration
        self.camera_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.video_button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.screenshot_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.screenrecord_button.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        
        # Configure grid weights
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def open_picture_window(self):
        self.destroy()
        PictureWindow().mainloop()
        
    def open_video_window(self):
        self.destroy()
        VideoWindow().mainloop()

    def open_screenshot_window(self):
        self.destroy()
        ScreenshotWindow().mainloop()

    def open_screenrecord_window(self):
        self.destroy()
        ScreenrecordWindow().mainloop()

def main():
    app = Gallery()
    app.mainloop()

if __name__ == "__main__":
    main()
