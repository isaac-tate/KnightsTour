"""Tour Noise -- pure python implementation"""

__version__ = '1'

from random import randint


class TourNoise(object):

    """
    General class for Knight Tour Noise of all sizes and steps
    """

    randint_function = randint

    def __init__(self, w, h, steps):

        """
        Initialized TourNoise generator. Takes in 3 arguement: the width of the image being
        generated (w, int), the height of the image being generated (h, int) and
        the number of tour steps (steps, int). Array is initialized as 0s (white in gray scale)
        and are adjusted based on how many times the knight lands on the pixel in <steps> steps
        """

        self.size = (h, w)

        self.visited = []
        for x in range(h):
            x_arr = []
            for y in range(w):
                x_arr.append(0)
            self.visited.append(x_arr)

        """
        The knight starts at h//2 and w//2 by deafult. It also creates the first visit
        at the starting point
        """

        self.k_position = (h//2, w//2)
        self.visited[h//2][w//2] = 1

        self.steps = steps



    def move_knight(self):

        """
        The move_knight randomly will select one of the possible 8 knight
        moves and pass the movement tuple to the update_knight class. This
        class has the main loop for each knight step
        """

        for i in range(self.steps):

            move = (0,0)
            direction = self.randint_function(0, 8)

            if(direction == 0):
                move = (-2, -1)
            elif(direction == 1):
                move = (-2, 1)
            elif(direction == 2):
                move = (-1, -2)
            elif(direction == 3):
                move = (-1, 2)
            elif(direction == 4):
                move = (1, -2)
            elif(direction == 5):
                move = (1, 2)
            elif(direction == 6):
                move = (2, -1)
            elif(direction == 7):
                move = (2, 1)

            self.update_knight(move)

    def update_knight(self, move):

        """
        This class moves a knight from one postion to another and
        marks the map with a pass. If the knight moves out of bounds
        it just does not move and the step is void
        """

        x = self.k_position[0] + move[0]
        y = self.k_position[1] + move[1]

        if(x < 0):
            pass
        elif(x >= self.size[0]):
            pass
        elif(y < 0):
            pass
        elif(y >= self.size[1]):
            pass

        else:
            self.k_position = (x,y)
            self.visited[self.k_position[0]][self.k_position[1]] += 1

knight = TourNoise(100, 100, 200000)
knight.move_knight()

#Show Image
import matplotlib.pyplot as plt
plt.imshow(knight.visited)
#plt.savefig("Example.png", bbox_inches='tight')
