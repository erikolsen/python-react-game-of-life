import random

class Game:
    def __init__(self, board=None, size=20):
        self.size = len(board[0]) if board else size
        self.board = board or [[0]*self.size for _ in range(self.size)]

    def randomize(self):
        return [self.set_random((row,col)) for col in range(self.size) for row in range(self.size)]

    def cell_value(self, cell):
        x,y = cell
        return self.board[x][y]

    def set_random(self, cell):
        x,y = cell
        self.board[x][y] = random.randint(0,1)

    def set_cell(self, cell, value):
        x,y = cell
        self.board[x][y] = value

    def is_alive(self, cell):
        return self.cell_value(cell) is 1

    def is_dead(self, cell):
        return self.cell_value(cell) is 0

    def populate(self, cell):
        self.set_cell(cell, 1)

    def kill(self, cell):
        self.set_cell(cell, 0)

    def neighbors(self, cell):
        a,b = cell
        possible = [
            (a-1, b-1), (a-1, b), (a-1, b+1),
            (a, b-1), (a, b+1),
            (a+1, b-1), (a+1, b), (a+1, b+1)
        ]
        in_bounds = lambda cell: 0 <= cell[0] < self.size and 0 <= cell[1] < self.size
        return list(filter(in_bounds, possible))

    def living_neighbors(self, cell):
        return sum([self.cell_value(cell) for cell in self.neighbors(cell)])

    def underpopulated(self, cell):
        return self.is_alive(cell) and self.living_neighbors(cell) < 2

    def overpopulated(self, cell):
        return self.is_alive(cell) and self.living_neighbors(cell) > 3

    def reproducable(self, cell):
        return self.is_dead(cell) and self.living_neighbors(cell) == 3

    def filter_by(self, rule):
        return [(row, col) for col in range(self.size) for row in range(self.size) if rule((row, col))]

    def tick(self):
        deaths = self.filter_by(self.overpopulated) + self.filter_by(self.underpopulated)
        births = self.filter_by(self.reproducable)

        for cell in deaths:
            self.kill(cell)

        for cell in births:
            self.populate(cell)


    def show(self):
        for row in self.board:
            for cell in row:
                if cell == 1:
                    print('■', end='')
                else:
                    print(' ', end='')
            print(' ')

