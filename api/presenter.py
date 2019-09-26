def enliven(array):
    return [['alive' if el == 1 else '' for el in row] for row in array]

# from itertools import product, starmap
# import operator
# x,y = cell
# neighbors = starmap(lambda a,b: (x+a, y+b), product((0,-1,+1), (0,-1,+1)))
# neighbors = list(filter(self.in_bounds, [el for el in whee if el != cell]))
# neighbors.sort(key = operator.itemgetter(0, 1))
# return neighbors

# def enliven(array):
    # enlivened_array = []
    # for row in array:
        # new_row = []
        # for el in row:
            # new_state = 'alive' if el == 1 else ''
            # new_row.append(new_state)
        # enlivened_array.append(new_row)
    # return enlivened_array

# def enliven(array):
    # build_new = lambda row: list(map(stringify, row))
    # stringify = lambda cell: 'alive' if cell == 1 else ''
    # return list(map(build_new, array))

