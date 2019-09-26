from game import Game
import time
import os
import sys

if __name__ == '__main__':
    game = Game()
    # game.randomize()
    glider_start_possitions = [(0,0), (1,1), (1,2), (2,0), (2,1)]
    for cell in glider_start_possitions:
        game.populate(cell)
    for move in range(1, 101):
        os.system('clear')
        print(f'Iteration {move} of 100')
        game.show()
        game.tick()
        time.sleep(0.1)
    sys.exit(0)


