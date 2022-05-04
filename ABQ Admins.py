import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title("AAA log-in")


frame = tk.Frame(master=window, width=500, height=250)
frame.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)


icon = tk.PhotoImage(file="Screenshot (59).png")
small = icon.subsample(5, 5)
pictureLabel = tk.Label(master=window, image=small)
pictureLabel.place(x=40, y=96)


companyNameLabel = tk.Label(master=frame, text="Albuquerque Associates: Attorneys at Law®", font="Tahoma",
                     fg="black", bg="#865439", relief=tk.RIDGE)
companyNameLabel.place(x=100, y=2)


welcomeLabel = tk.Label(master=frame, text="Welcome administrators,", font="Tahoma", relief=tk.RIDGE)
welcomeLabel.place(x=7, y=30)


pleaseLabel = tk.Label(master=frame, text="Please log-in with your credentials", font="Tahoma", relief=tk.RIDGE)
pleaseLabel.place(x=7, y=54)


usernameLabel = tk.Label(master=frame, text="USERNAME", font="Tahoma 9")
usernameLabel.place(x=335, y=80)

usernameEntry = tk.Entry(master=frame, borderwidth=2, font="Tahoma 8")
usernameEntry.place(x=307, y=100)


passwordLabel = tk.Label(master=frame, text="PASSWORD", font="Tahoma 9")
passwordLabel.place(x=335, y=129)

passwordEntry = tk.Entry(master=frame, borderwidth=2, font="Tahoma 8")
passwordEntry.place(x=307, y=150)
passwordEntry.config(show="*")


frame2 = tk.Frame(master=window)
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# Variables for the administrator's username and password
possibleU1 = "tsbsesnoecatf_aaa"
# this should be secure enough so no outside entity can access this form
adminPassword = "3dyuYYsXh3H-J#J$"


def open_new_window():
    uname = usernameEntry.get()
    pword = passwordEntry.get()

    if uname == possibleU1 and pword == adminPassword:
        messagebox.showinfo("AAA log-in", "Logging in")
        window.destroy()
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

button = tk.Button(master=frame, text="Login", bg="black", fg="white", font="Tahoma 9", command=open_new_window)
button.place(x=348, y=180)


window.mainloop()
