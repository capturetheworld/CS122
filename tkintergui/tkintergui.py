import tkinter# step 1 import tknter module

def main():
    root = tkinter.Tk()# step 2 create teh GUI app window
    root.title("CS 122")# customize title
    #instantiate a label widget with root as parent widget
    #use text option to specify text to display
    hello = tkinter.Label(root, text="Hello World!") #need to register with
    # geometry manager

    hello.pack()
    root.mainloop()# step 5 enter main event loop and wait

if __name__=='__main__':
    main()



