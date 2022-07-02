import sample_board

from board import Board
from solver import Solver


# Sample usage
if __name__ == "__main__":

    # Read in sample data
    initial_board = sample_board.initial_board
    grouping = sample_board.grouping


    b = Board(initial_board, grouping)
    s = Solver(b)

    s.solve(b)

    s.plot_solution()
    #s.animate_solution()
    