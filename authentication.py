from canvas import *
from helpers import *
from json import loads, dump
from Buying_page import *

def get_all_users_data():
    info = []
    # When we are reading from .json file we get the lines in this format:
    # {"first_name": "Ivan"} --- always with double quotation marks
    # json works with loads function to read strings
    with open("db/users_information.json", "r") as users_file:
        for line in users_file:
            info.append(loads(line))
    return info

# in the command section we write the name of the function we want to be executed but without the parenthesis,
# because we do not want it to be executed yet, but when the button is being clicke on - we say we pass the function only as a reference
# bg = background
# fg = colour of the text
# root - the first position, the page, where the button is appended
# we import canvas, because there is imported tkinter and we use everything from the file

def render_entry():
    register_btn = Button(root, text="Register", bg="green", fg="white", borderwidth=0, width=20, height=3,
                          command=register)
    login_btn = Button(root, text="Login", bg="blue", fg="white", borderwidth=0, width=20, height=3, command=login)
    # We append the buttons to the frame by the create_window tk function
    # x = 350, y = 260
    # Window - what is being vizualized - picture, page, button, etc.
    frame.create_window(350, 260, window=register_btn)
    frame.create_window(350, 320, window=login_btn)

def login():
    clean_screen()
    frame.create_text(100, 50, text = "Username:")
    frame.create_text(100, 100, text="Password:")

    frame.create_window(200, 50, window = username_box)
    frame.create_window(200, 100, window=password_box)

    logging_btn = Button(root, text = "Login", bg = "blue", fg= "white", command = logging)

    frame.create_window(250, 160, window = logging_btn)

def logging():
    if check_logging():
        display_products()
    else:
        frame.create_text(175, 200, text = "Invalid username or password!", fill = "red")

def check_logging():
    info_data = get_all_users_data()

    for i in range(len(info_data)):
        username = info_data[i]["username"]
        password = info_data[i]["password"]

        if username == username_box.get() and password == password_box.get():
            return True

    return False

def register():
    # We had made this function, which returns blank frame, in the helpers.py file and import * from it
    clean_screen()
    # create_text function is another tk function, again receiving x,y coordinates and the text we want to appear
    frame.create_text(100, 50, text="First name:")
    frame.create_text(100, 100, text="Last name:")
    frame.create_text(100, 150, text="Username:")
    frame.create_text(100, 200, text="Password:")
    # We append the blank boxes where the users type their data by create_window, and the type of window are the already made entry boxes
    frame.create_window(200, 50, window=first_name_box)
    frame.create_window(200, 100, window=last_name_box)
    frame.create_window(200, 150, window=username_box)
    frame.create_window(200, 200, window=password_box)

    registration_btn = Button(root, text = "Register", bg = "green", fg = "white", command = registration)
    frame.create_window(300, 250, window=registration_btn)

def registration():
    #get function takes what is typed in the box
    info_dict = {"first_name": first_name_box.get(),
                 "last_name": last_name_box.get(),
                 "username": username_box.get(),
                 "password": password_box.get(),
                 "products":[]}

    if check_registration(info_dict):
        #json.dumps() function will convert a subset of Python objects into a json string
        #dump() which converts the Python objects into appropriate json object
        #dump(what to put in, where to put it in)
        with open("db/users_information.json", "a") as users_file:
            dump(info_dict, users_file)
            users_file.write("\n")
            display_products()

def check_registration(info):
    for el in list(info.values())[:-1]:
        if el.strip() == "":
            #possible mistake- fill instead of fg needed
            frame.create_text(300,300,text="Filling all tabs is required...", fill= "red", tag="error")
            return False
    frame.delete("error")

    info_data= get_all_users_data()

    for i in range(len(info_data)):
        if info_data[i]["username"] == info["username"]:
            frame.create_text(300, 300, text = "Username already exists!", fill = "red", tags = "error")
            return False

    frame.delete("error")
    return True

# Entry makes an empty box, which takes single line of input from the user
# Entry(master, options)
# The master is the parent window
first_name_box = Entry(root, bd=0)
last_name_box = Entry(root, bd=0)
username_box = Entry(root, bd=0)
password_box = Entry(root, bd=0, show = "*")
