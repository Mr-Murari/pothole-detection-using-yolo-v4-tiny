import tkinter as tk
from PIL import Image,ImageTk
import cv2 as cv

root = tk.Tk()
root.title("Pothole Detection System")
#root.geometry("430x300")


def image():
    with open("pothole-detection\\image.py", "r") as f:
        script_code = f.read()
    # Execute the script code
    exec(script_code)

def video():
    with open("pothole-detection\\video.py", "r") as f:
        script_code = f.read()
    # Execute the script code
    exec(script_code)

def camera():
    with open("pothole-detection\\camera.py", "r") as f:
        script_code = f.read()
    # Execute the script code
    exec(script_code)
    

#logo
logo=Image.open("pothole-detection\\logo.jfif")
logo=ImageTk.PhotoImage(logo)
logo_label=tk.Label(image=logo)
logo_label.image=logo
logo_label.grid(column=1,row=1)



#instructions
instructions=tk.Label(root,text="Select file type to detect potholes",fg='black',font=18)
instructions.grid(column=1,row=2)

#frame=tk.Frame(root)

label=tk.Label(root,text="POTHOLE DETECTION SYSTEM",font=30)
label.grid(row=0,column=1,sticky='news')


img_btn=tk.Button(root,text="Image",command=lambda:image(),font="Raleway",bg="black",fg="#FFD700",height=2,width=10)
img_btn.grid(column=0,row=3)

vid_btn=tk.Button(root,text="Video",command=lambda:video(),font="Raleway",bg="black",fg="#FFD700",height=2,width=10)
vid_btn.grid(column=1,row=3)


cam_btn=tk.Button(root,text="Camera",command=lambda:camera(),font="Raleway",bg="black",fg="#FFD700",height=2,width=10)
cam_btn.grid(column=2,row=3)


#frame.pack()


root.mainloop()
