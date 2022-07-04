import sample_board

from board import Board
from solver import Solver


# Sample usage
if __name__ == "__main__":

    # Read in sample data
    initial_board, grouping = sample_board.sample3

    b = Board(initial_board, grouping)
    s = Solver(b)

    s.solve(b)
    print(f"Solved the puzzle in {len(s.boards)} steps")
    #s.plot_solution()
    s.animate_solution(fps=150)
    