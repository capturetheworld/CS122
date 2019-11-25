# ----------------------------------------------------------------------
# Name:        matchit
# Purpose:     Implement a single player matching game
#
# Author(s): Ian SooHoo
# ----------------------------------------------------------------------
"""
A single player matching game.

usage: matchit.py [-h] [-f] {blue,green,magenta} image_folder
positional arguments:
  {blue,green,magenta}  What color would you like for the player?
  image_folder          What folder contains the game images?

optional arguments:
  -h, --help            show this help message and exit
  -f, --fast            Fast or slow game?
"""
import tkinter
import os
import random
import argparse


class MatchGame(object):

    """
    GUI Game class for a matching game.

    Arguments:
    parent: the root window object
    player_color (string): the color to be used for the matched tiles
    folder (string) the folder containing the images for the game
    delay (integer) how many milliseconds to wait before flipping a tile

    Attributes:
    Please list ALL the instance variables here
    """

    # Add your class variables if needed here - square size, etc...)
    square_size = 10
    color = ''
    score = 100
    tries = 0


    def __init__(self, parent, player_color, folder, delay):
        parent.title('Match it!')
        self.color = player_color

        # Create the restart button widget
        restart_button = tkinter.Button(parent, text='RESTART', width=20,
                                      command=self.restart)
        restart_button.grid()
        self.canvas = tkinter.Canvas(parent, width=400, height=400)
        self.canvas.grid()

        for i in range(0,400,100):
            for j in range(0,400,100):
                 self.canvas.create_rectangle(i, j, i+100, j+100,
                                outline='black', fill="yellow")

        self.canvas.bind("<Button-1>", self.play)

        self.sammy = tkinter.PhotoImage(file=f'{folder}sjsu1.gif')



        # Create a canvas widget
        # Create a label widget for the score and end of game messages
        self.game_over = tkinter.Label(parent, text='Game Over!')
        status = tkinter.Label(parent, text=f'Score: {self.score}')
        status.grid()
        self.tries_label = tkinter.Label(parent,
                                       text=f'Number of tries: {self.tries}')

        # Create any additional instance variable you need for the game



    def restart(self):
        """
        This method is invoked when player clicks on the RESTART button.
        It shuffles and reassigns the images and resets the GUI and the
        score.
        :return: None
        """
        # self.canvas.delete(ALL)
        self.score = 100
        for shape in self.canvas.find_all():
            self.canvas.itemconfigure(shape, fill='yellow')
        self.tries = 0


    def play(self, event):
        """
        This method is invoked when the user clicks on a square.
        It implements the basic controls of the game.
        :param event: event (Event object) describing the click event
        :return: None
        """
        shape = self.canvas.find_closest(event.x, event.y)
        self.canvas.itemconfigure(shape, fill=self.color)
        self.tries+=1
        print(self.tries)
        self.image_id = self.canvas.create_image(80, 80,
                                                 image=self.sammy)
        self.canvas.after(1000, self.disappear)

    # Enter your additional method definitions below
    # Make sure they are indented inside the MatchGame class
    # Make sure you include docstrings for all the methods.



# Enter any function definitions here to get and validate the
# command line arguments.  Include docstrings.

def dir_type(img_folder):
    """
    Validate the user entered image folder
    :param img_folder: (string)
    :return: integer
    """
    # absolute_dir = os.getcwd()+os.sep+img_folder
    # worki = img_folder
    # print(absolute_dir)
    if os.path.exists(img_folder) is False:
        raise argparse.ArgumentTypeError(img_folder+" is not a valid folder")

    if len(os.listdir(img_folder)) < 8:
        raise argparse.ArgumentTypeError(img_folder + " must contain at "
                                                      "least 8 "
                                                  "gif images")
    return img_folder



def main():
    # Retrieve and validate the command line arguments using argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('color', help='What color would you like for the '
        'player? ',  choices=["blue", "green", "magenta"])
    parser.add_argument('image_folder',
                        help='What folder contains the game images?',
                        type=dir_type,
                        nargs='?')
    parser.add_argument('-f', '--fast',
                        help='Fast or slow game?',
                        action='store_true')


    arguments = parser.parse_args()
    color = arguments.color
    image_folder = arguments.image_folder
    speed = 0
    if arguments.fast is True:
        speed = 1000
    else:
        speed = 3000

    # Instantiate a root window
    root = tkinter.Tk()  # step 2: create the GUI application main window.


    # Instantiate a MatchGame object with the correct arguments
    matchapp = MatchGame(root, color, image_folder, speed)
    # Enter the main event loop
    root.mainloop()  # step 5: enter the main event loop and wait


if __name__ == '__main__':
    main()
    
