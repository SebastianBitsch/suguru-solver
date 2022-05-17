from copy import copy, deepcopy
from tokenize import group
import matplotlib.pyplot as plt
from board import Board
from solver import Solver

BOARD_SIZE = 8


initial_board = [
    [0,0,0,0,1,0,0,0],
    [0,0,5,0,0,3,0,3],
    [0,0,0,0,0,0,0,0],
    [0,4,0,3,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [5,0,2,4,0,0,0,0]
]

grouping = [
    [0, 1, 1, 2, 2, 2, 3, 3], 
    [0, 1, 1, 6, 2, 2, 4, 3], 
    [0, 1, 6, 6, 5, 4, 4, 3], 
    [7, 7, 6, 6, 5, 4, 4,10], 
    [7, 7, 9, 9, 5,11,10,10], 
    [8, 8, 9, 9, 5,11,11,10], 
    [8, 8, 8, 9,13,11,12,12]
]
def main():

    b = Board(initial_board, grouping)
    s = Solver(b, grouping)

    # print(s.board.values_to(8))

    print(b)
    a = s.solve(deepcopy(b),0)
    print("after")
    print(s.board)
    
    
    # plt.imshow(grouping)
    # plt.show()

if __name__ == "__main__":
    main()



