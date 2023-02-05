from authentication import render_entry
from canvas import root

#If this is the first time to open the main.py file :
#We want to open the tk.mainloop to keep the program alive making an infinite loop while the file is open
#In order to do it just once we write the following line "if __name__ == "__main__"
#the name is __main__ only in the first opening. Later it is __main__1, __main__2 and so on.
#the mainloop is a method of the Tk() and it is the most important thing to run out app


if __name__ == "__main__":
    # First, we load the page
    render_entry()
    #Then, we run the program
    root.mainloop()
