from tkinter import *
from scratchclient import ScratchSession

class Cloud:
    def __init__(self,session:ScratchSession):
        self.session = session
        self.root = Tk()
        self.notify = Listbox(self.root, width=60, height=10)
        self.notify.pack()
        self.txt = Entry(self.root)
        self.txt.pack()
        Button(self.root, text="Load Project", command=self.loadProject).pack()
        self.varName = Entry(self.root)
        self.varName.pack()
        self.varVal = Entry(self.root)
        self.varVal.pack()
        Button(self.root, text="Set Var", command=self.setVar).pack()
    def loadProject(self):
        self.cloud = self.session.create_cloud_connection(int(self.txt.get()))
        self.notify.insert(END, f'Project {self.cloud.project_id} has been loaded')
        @self.cloud.on("set")
        def on(var):
            self.notify.insert(END, f'{var.name} has been set to {var.value}')
    def setVar(self):
        varName = "☁ " + self.varName.get()
        newVal = self.varVal.get()
        self.cloud.set_cloud_variable(varName, int(newVal))
    def launch(self):
        self.root.title("Cloud Editor")
        self.root.geometry("400x300")
        self.root.mainloop()