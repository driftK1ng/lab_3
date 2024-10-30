import numpy as np
from random import choice, randint

class Model():
    empty_count: int
    red_count: int
    blue_count: int
    size: int
    others_count: int
    iterations_count: int

    def __init__(self, others_count: int, iterations_count: int) -> None:
        self.others_count = others_count
        self.iterations_count = iterations_count

    def count_cells(self, matrix_size: int, empty_percent: int):
        self.empty_count = matrix_size // (1 / empty_percent)
        self.red_count = (matrix_size - self.empty_count) // 2
        self.blue_count = (matrix_size - self.empty_count) // 2
        if ((matrix_size - self.empty_count) % 2 != 0):
            if (choice([0, 1]) == 0):
                self.red_count += 1
            else:
                self.blue_count += 1

    def fill(self, size: int, empty_percent: int):
        self.size = size
        self.count_cells(size**2, empty_percent)
        empty = np.full(self.empty_count, 0)
        blue = np.full(self.blue_count, -1)
        red = np.full(self.red_count, 1)
        self.box = np.concatenate((empty, blue, red))
        for i in range(2):
            np.random.shuffle(self.box)
        self.box = self.box.reshape((size, size))
        for i in range(2):
            np.random.shuffle(self.box)

    def find_others(self, x: int, y: int):
        numbers = list(range(self.size))
        to_delete = []
        coords = self.get_other_coords(x, y)
        for coord in coords:
            if (coord[0] == x and coord[1] == y):
                to_delete.append(coord)
            elif (coord[0] not in numbers or coord[1] not in numbers):
                to_delete.append(coord)
        for item in to_delete:
            coords.remove(item)
        return coords
    
    def get_other_coords(self, x: int, y: int):
        coords = []
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                coords.append([i, j])
        return coords
    
    def is_cell_happy(self, x, y):
        cell_color = self.box[x][y]
        same_color_counter = 0
        others = self.find_others(x, y)
        for other in others:
            if (self.box[other[0]][other[1]] == cell_color):
                if(same_color_counter + 1 == self.others_count):
                    return True
                same_color_counter += 1
        return False
    
    def check_cells(self):
        self.not_happy = np.array([[-1, -1]])
        self.empty = np.array([[-1, -1]])
        for i in range(self.size):
            for j in range(self.size):
                if (self.box[i][j] != 0):
                    if (not self.is_cell_happy(i, j)):
                        self.not_happy = np.concatenate((self.not_happy, np.array([i, j])), axis=0)
                else:
                    self.empty = np.concatenate((self.empty, np.array([[i, j]])), axis=0)

    def iteration(self):
        self.check_cells()
        self.not_happy = np.delete(self.not_happy, 0, 0)
        self.empty = np.delete(self.empty, 0, 0)

        not_happy_index = randint(0, len(self.not_happy) - 1)
        empty_index = randint(0, len(self.empty) - 1)

        not_happy_cell = self.not_happy[not_happy_index]
        empty_cell = self.empty[empty_index]

        self.box[empty_cell[0]][empty_cell[1]] = self.box[not_happy_cell[0]][not_happy_cell[1]]
        self.box[not_happy_cell[0]][not_happy_cell[1]] = 0

    def get_box(self):
        return self.box
    
    def get_iterations_count(self):
        return self.iterations_count
        

    