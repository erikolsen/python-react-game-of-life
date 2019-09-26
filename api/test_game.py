from game import Game
from presenter import enliven
import pytest

def test_size():
    game = Game(None, 3)
    assert game.size == 3

def test_board():
    empty_board = [[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]
    game = Game(empty_board)
    assert game.board == empty_board

def test_seeded_board():
    seeded_board = [[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]]
    game = Game(seeded_board)
    assert game.board == seeded_board

def test_is_alive():
    one_el_board = [[1, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]

    game = Game(one_el_board)
    cell = (0,0)
    assert game.is_alive(cell) is True

def test_is_dead():
    game = Game()
    cell = (0,0)
    assert game.is_alive(cell) is False

def test_populate():
    game = Game()
    cell = (0,0)
    assert game.is_alive(cell) is False

    game.populate(cell)
    print(game.board)
    assert game.is_alive(cell) is True
    assert game.is_alive((1,0)) is False

def test_kill():
    game = Game()
    cell = (0,0)
    game.populate(cell)
    assert game.is_alive(cell) is True

    game.kill(cell)
    assert game.is_alive(cell) is False

def test_living_neighbors():
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

    game = Game(board)
    cell = (1,1)

    assert game.living_neighbors(cell) == 0


def test_living_neighbors():
    board = [[1, 0, 1],
             [0, 0, 0],
             [1, 0, 1]]

    game = Game(board)
    cell = (1,1)

    assert game.living_neighbors(cell) == 4

def test_cell_value():
    board = [[1, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

    game = Game(board)
    cell = (0,0)
    assert game.cell_value(cell) == 1

def test_neighbors():
    game = Game()
    cell = (1,1)
    expected = [
        (0,0),
        (0,1),
        (0,2),
        (1,0),
        (1,2),
        (2,0),
        (2,1),
        (2,2)
    ]
    assert game.neighbors(cell) == expected
    # assert [1, 2, 3] == [3, 2, 1]

def test_underpopulated():
    board = [[1, 0, 0],
             [0, 1, 1],
             [1, 1, 1]]

    game = Game(board)
    dead_cell = (0, 1)
    alive_cell = (0, 0)
    bad_alive_cell = (1, 1)

    assert game.underpopulated(dead_cell) is False
    assert game.underpopulated(alive_cell) is True
    assert game.underpopulated(bad_alive_cell) is False

def test_overpopulated():
    board = [[1, 0, 1],
             [1, 1, 1],
             [0, 0, 0]]

    game = Game(board)
    alive_cell = (1,1)
    dead_cell = (0,1)
    bad_alive_cell = (1,0)

    assert game.overpopulated(alive_cell) is True
    assert game.overpopulated(dead_cell) is False
    assert game.overpopulated(bad_alive_cell) is False

def test_reproducable():
    board = [[0, 1, 0],
             [1, 1, 1],
             [0, 0, 0]]

    game = Game(board)
    dead_valid_cell = (2, 1)
    dead_invalid_cell = (2, 0)
    alive_cell = (0, 1)

    assert game.reproducable(dead_valid_cell) is True
    assert game.reproducable(dead_invalid_cell) is False
    assert game.reproducable(alive_cell) is False

def test_tick():
    board = [[1, 1, 1],
             [0, 0, 0],
             [0, 0, 0]]

    expected = [[0, 1, 0],
                [0, 1, 0],
                [0, 0, 0]]

    game = Game(board)
    game.tick()

    assert game.board == expected

