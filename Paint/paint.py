# ----------------------------------------------------------------------
# Name:        paint
# Purpose:     A very simple coloring application
#
# Author:      Rula Khayrallah
# ----------------------------------------------------------------------
"""
Module to implement a simple coloring app
"""
import tkinter

class PaintApp:
    
    """
    GUI PaintApp class for a simple coloring application.

    Argument:
    parent (tkinter.Tk): the root window object

    Attribute:
    canvas (tkinter.Canvas): the widget defining the area to be painted
    """

    # Define a class variable for the default color to be used
    default_color = 'red'

    def __init__(self, parent):
        parent.title("CS 122 - Let's Paint!")

        color_frame=tk

        # instantiate our Canvas widget with the root as parent
        self.canvas= tkinter.Canvas(parent, width=300, height=300)

        # draw a rectangle on the canvas for the background
        self.canvas.create_rectangle(0, 0, 300, 300)

        # draw a house
        self.canvas.create_rectangle(175, 150, 275, 250)
        # the roof is a triangle (polygon with 3 sides)
        self.canvas.create_polygon(165, 150, 225, 100, 285, 150,
                                   outline='black', fill='white')
        # draw a flower
        self.canvas.create_oval(50, 200, 75, 225)
        self.canvas.create_oval(50, 175, 75, 200)
        self.canvas.create_oval(50, 225, 75, 250)
        self.canvas.create_oval(25, 187, 50, 212)
        self.canvas.create_oval(25, 212, 50, 237)
        self.canvas.create_oval(75, 187, 100, 212)
        self.canvas.create_oval(75, 212, 100, 237)

        # register our canvas with a geometry manager
        self.canvas.grid()

    def blue(self):


def main():
    # create the GUI application main window
    root = tkinter.Tk()
    # Instantiate our painting app object
    painting = PaintApp(root)
    # enter the main event loop and wait for events
    root.mainloop()


if __name__ == '__main__':
    main()
