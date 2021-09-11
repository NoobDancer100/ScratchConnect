from tkinter import *
from scratchclient import ScratchSession

class Commenter:
    def __init__(self,session:ScratchSession):
        self.session = session
        self.root = Tk()
        self.notify = Listbox(self.root,width=60, height=10)
        self.notify.pack()
        self.txt = Entry(self.root)
        self.txt.pack()
        Button(self.root, text="Load Project", command=self.loadProject).pack()
        self.txtb = Entry(self.root)
        self.txtb.pack()
        Button(self.root, text="Post Comment", command=self.comment).pack()
    def loadProject(self):
        self.project = self.session.get_project(int(self.txt.get()))
        self.notify.insert(END, f'Loaded {self.project.title} by {self.project.author.username} into commenter.')
    def comment(self):
        self.project.post_comment(self.txtb.get())
    def launch(self):
        self.root.title("Commenter")
        self.root.mainloop()
