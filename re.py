import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF
import time

# Create a tkinter window
window = tk.Tk()
window.title("Real-Time Human Detection & Counting")
window.geometry('1000x700')

# Function to start the main application
def start_application():
    window.destroy()

# Create a start button
start_button = tk.Button(
    window,
    text="▶ START",
    command=start_application,
    font=("Arial", 25),
    bg="orange",
    fg="blue",
    cursor="hand2",
    borderwidth=3,
    relief="raised"
)
start_button.place(x=130, y=570)

# Load and display an image on the main window
path1 = "Images/front2.png"
img2 = ImageTk.PhotoImage(Image.open(path1))
panel1 = tk.Label(window, image=img2)
panel1.place(x=90, y=250)

path = "Images/front1.png"
img1 = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(window, image=img1)
panel.place(x=380, y=180)

exit_flag = False

# Function to exit from the window
def exit_window():
    global exit_flag
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        exit_flag = True
        window.destroy()

# Create an exit button
exit_button = tk.Button(
    window,
    text="❌ EXIT",
    command=exit_window,
    font=("Arial", 25),
    bg="red",
    fg="blue",
    cursor="hand2",
    borderwidth=3,
    relief="raised"
)
exit_button.place(x=680, y=570)

# Configure the window's exit behavior
window.protocol("WM_DELETE_WINDOW", exit_window)
window.mainloop()

if not exit_flag:
    # Main Window & Configuration of window1
    window1 = tk.Tk()
    window1.title("Real Time Human Detection & Counting")
    window1.geometry('1000x700')

    filename = ""
    filename1 = ""
    filename2 = ""

    def argsParser():
        # Parse command line arguments
        pass  # Implement this if needed

    def open_img():
        global filename1
        filename1 = filedialog.askopenfilename(title="Select Image file", parent=window1)
        path_text1.delete("1.0", "end")
        path_text1.insert(tk.END, filename1)

    def det_img():
        global filename1
        image_path = filename1
        if not image_path:
            messagebox.showerror("Error", "No Image File Selected!", parent=window1)
            return
        info1.config(text="Status : Detecting...")
        messagebox.showinfo("Status", "Detecting, Please Wait...", parent=window1)
        window1.update()
        time.sleep(1)
        detectByPathImage(image_path)

    def detectByPathImage(path):
        # Implement image detection logic here
        pass

    def prev_img():
        global filename1
        img = cv2.imread(filename1, 1)
        cv2.imshow("Selected Image Preview", img)

    def image_option():
        global window1
        windowi = tk.Toplevel(window1)
        windowi.title("Human Detection from Image")
        windowi.geometry('1000x700')

        # Rest of the image option code here...

    def open_vid():
        global filename2
        filename2 = filedialog.askopenfilename(title="Select Video file", parent=window1)
        path_text2.delete("1.0", "end")
        path_text2.insert(tk.END, filename2)

    def det_vid():
        global filename2
        video_path = filename2
        if not video_path:
            messagebox.showerror("Error", "No Video File Selected!", parent=window1)
            return
        info1.config(text="Status : Detecting...")
        messagebox.showinfo("Status", "Detecting, Please Wait...", parent=window1)
        window1.update()
        time.sleep(1)

        args = argsParser()
        writer = None
        if args['output'] is not None:
            writer = cv2.VideoWriter(args['output'], cv2.VideoWriter_fourcc(*'MJPG'), 10, (600, 600))
        detectByPathVideo(video_path, writer)

    def detectByPathVideo(path, writer):
        # Implement video detection logic here
        pass

    def prev_vid():
        global filename2
        cap = cv2.VideoCapture(filename2)
        if not cap.isOpened():
            messagebox.showerror("Error", "Error in opening video file", parent=window1)
            return
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                cv2.imshow('Video', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()

    def video_option():
        global window1
        windowv = tk.Toplevel(window1)
        windowv.title("Human Detection from Video")
        windowv.geometry('1000x700')

        # Rest of the video option code here...

    # Create a tab control
    tabControl = tk.Notebook(window1)
    tab1 = tk.Frame(tabControl)
    tab2 = tk.Frame(tabControl)
    tabControl.add(tab1, text="Image Detection")
    tabControl.add(tab2, text="Video Detection")
    tabControl.pack(expand=1, fill="both")

    # Create labels and buttons in tab1 for image detection
    label1 = tk.Label(tab1, text="Select an image for detection:", font=("Arial", 14))
    label1.pack(pady=10)
    path_text1 = tk.Text(tab1, height=2, width=50)
    path_text1.pack()
    open_button1 = tk.Button(tab1, text="Open Image", command=open_img, font=("Arial", 12))
    open_button1.pack(pady=10)
    preview_button1 = tk.Button(tab1, text="Preview Image", command=prev_img, font=("Arial", 12))
    preview_button1.pack(pady=10)
    detect_button1 = tk.Button(tab1, text="Detect Image", command=det_img, font=("Arial", 12))
    detect_button1.pack(pady=10)
    info1 = tk.Label(tab1, text="Status : ", font=("Arial", 12))
    info1.pack()

    # Create labels and buttons in tab2 for video detection
    label2 = tk.Label(tab2, text="Select a video for detection:", font=("Arial", 14))
    label2.pack(pady=10)
    path_text2 = tk.Text(tab2, height=2, width=50)
    path_text2.pack()
    open_button2 = tk.Button(tab2, text="Open Video", command=open_vid, font=("Arial", 12))
    open_button2.pack(pady=10)
    preview_button2 = tk.Button(tab2, text="Preview Video", command=prev_vid, font=("Arial", 12))
    preview_button2.pack(pady=10)
    detect_button2 = tk.Button(tab2, text="Detect Video", command=det_vid, font=("Arial", 12))
    detect_button2.pack(pady=10)
    info2 = tk.Label(tab2, text="Status : ", font=("Arial", 12))
    info2.pack()

    def exit_window1():
        global window1
        if messagebox.askokcancel("Exit", "Do you want to exit?", parent=window1):
            window1.destroy()

    

# ... (Previous code remains the same)

if not exit_flag:
    # Main Window & Configuration of window1
    window1 = tk.Tk()
    window1.title("Real Time Human Detection & Counting")
    window1.geometry('1000x700')

    filename = ""
    filename1 = ""
    filename2 = ""

    def argsParser():
        # Parse command line arguments if needed
        pass

    # ... (Other functions remain the same)

    def detectByPathImage(path):
        # Implement image detection logic here
        # You should load the image using OpenCV, perform detection,
        # and update the "info1" label with the detection results.
        pass

    def detectByPathVideo(path, writer):
        # Implement video detection logic here
        # You should read frames from the video using OpenCV, perform detection,
        # and update the "info2" label with the detection results.
        pass

    # ... (Other functions remain the same)

    window1.protocol("WM_DELETE_WINDOW", exit_window1)
    window1.mainloop()

