# ----------------------------------------------------------------------
# Name:     Homework 3
# Purpose: Create image blur
#
# Author:   Ian Soohoo and Trieu Nguyen
# ----------------------------------------------------------------------
""" Image Blurring

User can blur a representation of an image, pixels being represented
by integer values in a matrix. The user then uses the average
calculation function to modify the values and the box function
to find the area of which to blur
"""

def average_matrix(m):
    """Calculate average of a matrix

    Totals and finds average of a matrix

    Returns:
        float: the result of average calculation
    """

    rows = len(m)
    columns = len(m[0])
    total_value = 0
    for row in range(rows):
        total_value = total_value + sum(m[row])

    slots = rows * columns
    if slots==0:
        return None

    average = total_value / slots
    return average


def box (m, center):
    """Returns a box that is centered
    at the given row and column

    Takes as arguments a nested list representing a matrix and
    a tuple (row and column in that matrix).
    Returns a 3 x 3  submatrix that is centered
    at the given row and column.

    :param
       m (nested list): the matrix
       center (tuple): position of the center

    :returns
       nested list: the box around the center
    """

    row, col = center
    total_rows = len(m)

    if total_rows == 1:
        return m
    else:
        total_cols = len(m[0])

       # create 3x3 matrix consist of tuples
       # These are tuples of positions where each element of
       # the box is mapped in the parameter matrix
        box_matrix = \
            [[0 for i in range(3)] for j in range(3)]
        box_matrix[0][0] = (row-1, col - 1)
        box_matrix[0][1] = (row-1, col)
        box_matrix[0][2] = (row-1, col + 1)
        box_matrix[1][0] = (row, col - 1)
        box_matrix[1][1] = (row, col)
        box_matrix[1][2] = (row, col + 1)
        box_matrix[2][0] = (row+1, col - 1)
        box_matrix[2][1] = (row+1, col)
        box_matrix[2][2] = (row+1, col + 1)

        #use min, max build in functions
        # smallest column value in the box
        min_col = min(i[1] for i in box_matrix[0])
        # biggest column value in the box
        max_col = max(i[1] for i in box_matrix[0])
        # smallest row value in the box
        min_row = box_matrix[0][0][0]
        # biggest row value in the box
        max_row = box_matrix[2][0][0]

        if min_row < 0 : #first row of the box is out of the matrix
            if min_col < 0 :  # left upper edge
            # when the left column of the 3x3 box is out of the matrix
                return [m[0][:2],
                        m[1][:2]]
            elif max_col > total_cols - 1:  # right upper edge
            #when the right column of the 3x3 box is out of the matrix
                return [m[0][col - 1:],
                        m[1][col - 1:]]
            else:
            #just first row of the box out of the matrix,
            # no edge positions
                return [m[0][col - 1:col + 2],
                        m[1][col - 1:col + 2]]

        elif max_row > total_rows - 1:  # last row
            if min_col < 0:  # left under edge
                return [m[row - 1][:2],
                        m[row][:2]]
            elif max_col > total_cols - 1:  # right under edge
                return [m[row - 1][col - 1:],
                        m[row][col - 1:]]
            else:
                return [m[row - 1][col - 1:col + 2],
                        m[row][col - 1:col + 2]]

        elif min_col < 0:  # first column
            # (the edges are taken care of from first/last row cases)
            return [m[row - 1][:2],
                    m[row][:2],
                    m[row + 1][:2]]

        elif max_col > total_cols - 1:  # last column
            return [m[row - 1][col - 1:],
                    m[row][col - 1:],
                    m[row + 1][col - 1:]]

        else:  # other positions
            return [m[row - 1][col - 1: col + 2],
                    m[row][col - 1: col + 2],
                    m[row + 1][col - 1: col + 2]]



def blur(image):
    """Create image blur from the original image

    Takes as an argument a nested list representing
    a grayscale image and returns a nested list
    representing the blurred image.

    :param
       nested list: image: original image matrix
    :return
       nested list: blur image matrix
    """

    blur_image = \
        [[0 for i in range(len(image[0]))] for j in range( len(image))]
    for row in range(len(image)):
        for col in range(len(image[0])):
            blur_image [row][col] = \
                round(average_matrix(box(image, (row, col))))
    return blur_image

def main():
    print("Text average_matrix function")
    grid = [[1, 2, 0],
           [4, 0, 5],
           [7, 3, 9],
           [0, 8, 0]]

    print (average_matrix(grid))
    print (average_matrix([[5]]))
    print (average_matrix([[]]))

    grid2 = [[1, 2],
            [4, 0],
            [7, 3],
            [0, 8]]

    print(average_matrix(grid2))

    print()
    print("Test box function")

    print ( box(grid, (0,0)) )

    print ( box(grid, (2, 1)) )

    print ( box(grid, (3, 1)) )

    print ( box([[5]], (0, 0)) )

    print ()

    print(box(grid2, (0, 0)))

    print(box(grid2, (2, 1)))

    print(box(grid2, (3, 1)))

    print()

    grid3 = [[1],
             [4],
             [7],
             [0]]
    print(box(grid3, (0, 0)))

    print(box(grid3, (2, 0)))

    print(box(grid3, (3, 0)))

    print()

    print("Test blur function")

    image = [[168, 168, 170, 172, 174, 158, 154, 170],
            [172, 126, 109, 86, 72, 72, 95, 129],
            [146, 152, 165, 183, 176, 177, 178, 176],
            [181, 153, 80, 57, 79, 57, 29, 23],
            [29, 34, 19, 28, 38, 39, 15, 26],
            [14, 21, 18, 21, 21, 18, 24, 25]]

    print(blur(image))

if __name__ == "__main__":
   main()


