import tkinter as tk
from tkinter import filedialog
from detector import webcam_handler, video_handler


def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi")])
    video_handler(filename)


root = tk.Tk()
root.title("Video Selection")

webcam_button = tk.Button(
    root, text="Webcam", command=webcam_handler, height=20, width=80, bg="liggt yellow"
)
webcam_button.pack(pady=10)

browse_button = tk.Button(
    root, text="Browse", command=browse_file, height=20, width=80, bg="light blue"
)
browse_button.pack(pady=10)

root.mainloop()
