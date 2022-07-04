import sample_board

from board import Board
from solver import Solver


# Sample usage
if __name__ == "__main__":

    # Read in sample data
    #initial_board, grouping = sample_board.sample1
    initial_board, grouping = sample_board.sample2

    b = Board(initial_board, grouping)
    s = Solver(b)

    s.solve(b)

    s.plot_solution()
    print("here")
    #s.animate_solution(fps=400)
    