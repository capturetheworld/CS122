import tkinter# step 1 import tknter module

class GenApp:
    """
    class to support general purpose GUI

    Argument:
    parent:(tkinter.Tk) the root window object

    Attributes:
    status:(tkinter.Label) A label eidget showing the current status
    """



    def __init__(self,parent):
        parent.title("CS 122")
        start_button = tkinter.Button(parent, text="START", width = 20,
                                      command = self.start)
        start_button.grid()
        stop_button = tkinter.Button(parent, text="STOP", width = 20,
                                      command = self.stop)
        stop_button.grid()
        self.status = tkinter.Label(parent, text = "Ready to start")
        self.status.grid()

    def start(self):
        self.status.configure(text="in progress", foreground = "green")

    def stop(self):
        self.status.configure(text="all done", foreground="red")

def main():
    root = tkinter.Tk()# step 2 create teh GUI app window
    gen_app = GenApp(root) #instantiate generic app object
    root.mainloop()

if __name__=='__main__':
    main()

