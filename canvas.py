from tkinter import *

#The geometry states the size of the app
#root = Tk() the class that makes the app itself
#The initial title before changing from root.title is "tk"

def create_app():
    root = Tk()
    root.geometry("700x600+0+0")
    root.title("Gun shop")
    return root

#We create a framework - like an unvisible blanket on the page where we can append buttons, pctures and etc.
#We can use the framework in two ways - as a grid(matrix) or as a coordinate system(700*x, 600 *y), which is the easiest way to find the center
#Again, first we state where we want the frame to be appended
#We return "frame" in order to use it in a variable

def create_frame():
    frame = Canvas(root, width = 700, height = 700)
    frame.grid(row = 0, column = 0)
    #We forbid the option to maximise the screen in order to keep our design unbroken
    root.resizable(False, False)
    return frame

root = create_app()
frame = create_frame()