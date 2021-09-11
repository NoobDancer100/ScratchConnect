from tkinter import *
from scratchclient import ScratchSession
from windows.cloudedit import Cloud
from windows.commenter import Commenter

class Home:
    def __init__(self,session:ScratchSession):
        self.session = session
        self.root = Tk()
        self.notify = Listbox(self.root,width=60, height=10)
        self.notify.pack()
        self.getNotifications()
        Button(self.root, text="Open Cloud Editor", command=self.openCloud).pack()
        Button(self.root, text="Open Comment Poster", command=self.openComment).pack()
    def openCloud(self):
        Cloud(self.session).launch()
    def openComment(self):
        Commenter(self.session).launch()
    def getNotifications(self):
        for msg in self.session.get_messages(limit=10):
            if msg.type == "addcomment":
                self.notify.insert(END, f'{msg.actor} commented "{msg.comment_fragment}"')
            if msg.type == "followuser":
                self.notify.insert(END, f'{msg.actor} followed you!')
            if msg.type == "loveproject":
                self.notify.insert(END, f'{msg.actor} has loved something.')
    def launch(self):
        self.root.title("Scratch Access - " + self.session.username)
        self.root.geometry("400x300")
        self.root.mainloop()