from tkinter import *

class Login:
    def __init__(self):
        self.root = Tk()
        Label(self.root, text="Username: ").grid(column=1,row=1)
        self.name = Entry(self.root)
        self.name.grid(column=2, row=1)
        Label(self.root, text="Password: ").grid(column=1, row=2)
        self.password = Entry(self.root, show="*")
        self.password.grid(column=2, row=2)
        Button(self.root, text="Login", command=self.finish).grid(row=3,column=1)
    def readInfo(self):
        self.root.title("Login to Scratch")
        self.root.geometry("200x100")
        self.root.mainloop()
    def onDone(self,f):
        self.finished = f
    def finish(self):
        username = self.name.get()
        password = self.password.get()
        self.root.destroy()
        self.finished(username,password)