from random import choice

class RandomWalk():
    """Class for generating random walks"""
    def __init__(self, num_points=5000):
        """Initializes the wander attributes"""
        self.num_points = num_points

        #All walks start from the point (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """"Computes all walk points"""
        #Steps are generated until the desired length is reached
        while len(self.x_values) < self.num_points:
            #Determining the direction and length of movement
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #Deviation of zero displacements
            if x_step == 0 and y_step == 0:
                continue

            #Calculating the next x and y values
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)