"""
Date: 05/19/2022
Author: Benjamin Parker
Version: 1.1
Name: ABQ Admin log-in
Summary: This application is the log-in screen for an attorney's office administrators.
"""
import tkinter as tk  # Import the tkinter framework
from tkinter import messagebox  # This is a tool inside tkinter that allows message boxes to pop up
window = tk.Tk()  # Main window for application
window.title("AAA log-in")  # The title for the main window
window.minsize(500, 300)  # The minimum size the main window can be


# The main window frame that encompasses the whole window
frame = tk.Frame(master=window, width=500, height=300)
frame.pack(fill=tk.X, side=tk.RIGHT, expand=True)

# This is the photo that is shown
icon = tk.PhotoImage(file="Screenshot (59).png")
small = icon.subsample(2, 2)  # This makes the image smaller to fit the window
pictureLabel = tk.Label(master=frame, image=small, bg="black")
pictureLabel.place(x=98, y=100)  # Anywhere there is a ".place", is where the item is placed in the window

# This is the company name label
companyNameLabel = tk.Label(master=frame, text="Albuquerque Associates: Attorneys at Law®", font="Tahoma",
                            bg="#865439", relief=tk.RIDGE)
companyNameLabel.place(x=100, y=0)

# This is the welcome label
welcomeLabel = tk.Label(master=frame, text="Welcome administrators,", font="Tahoma", bg="#865439", relief=tk.RIDGE)
welcomeLabel.place(x=7, y=30)

# This is the please log-in label
pleaseLabel = tk.Label(master=frame, text="Please log-in with your credentials", font="Tahoma", bg="#865439",
                       relief=tk.RIDGE)
pleaseLabel.place(x=7, y=60)

# This is the "USERNAME" label
usernameLabel = tk.Label(master=frame, text="USERNAME", font="Tahoma 9", bg="#865439")
usernameLabel.place(x=335, y=130)
# This is the entry box where you enter the username
usernameEntry = tk.Entry(master=frame, borderwidth=2, font="Tahoma 8")
usernameEntry.place(x=306, y=150)

# This is the "PASSWORD" label
passwordLabel = tk.Label(master=frame, text="PASSWORD", font="Tahoma 9", bg="#865439")
passwordLabel.place(x=335, y=180)
# This is the entry box where you enter the password
passwordEntry = tk.Entry(master=frame, borderwidth=2, font="Tahoma 8")
passwordEntry.place(x=306, y=200)
passwordEntry.config(show="*")  # This allows the password to be shown as "*" characters instead of the actual password


frame2 = tk.Frame(master=window)
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# Variables for the administrator's username and password
possibleU1 = "tsbsesnoecatf_aaa"  # this should be secure enough so no outside entity can access this form

adminPassword = "3dyuYYsXh3H-J#J$"  # A secure password


def open_new_window():
    """This module was created to open a new window
        after the user enters in credentials or nothing
        for the username and password field"""
    uname = usernameEntry.get()  # This takes the input for the username and plugs it in to see if it matches
    pword = passwordEntry.get()  # This takes the input for the password and plugs it in to see if it matches

    if uname == possibleU1 and pword == adminPassword:
        messagebox.showinfo("AAA log-in", "Logging in")
        window.destroy()  # This will close out of the application
    elif uname == "" and pword == "":
        messagebox.showinfo("AAA log-in", "No blanks allowed")
    elif uname != possibleU1:
        messagebox.showinfo("AAA log-in", "Incorrect credentials")
    elif pword != adminPassword:
        messagebox.showinfo("AAA log-in", "Incorrect credentials")
    else:
        messagebox.showinfo("AAA log-in", "There has been an error")


buttonFrame = tk.Frame(master=window)
buttonFrame.pack()
# This is the log-in button underneath the password entry
loginButton = tk.Button(master=frame, text="Login", bg="black", fg="white", font="Tahoma 9", command=open_new_window)
loginButton.place(x=350, y=230)


window.mainloop()
