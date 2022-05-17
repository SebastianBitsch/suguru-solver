from copy import copy, deepcopy
from board import Board
import util

class Solver:

    def __init__(self, initial_board: Board, grouping: list) -> None:
        self.board = initial_board
        self.boards = []
        self.grouping = grouping
        self.num_groups = len(set(util.flat_list(grouping)))
        self.values_tried = []#dict([(key, []) for key in range(56)])


    def solve(self, b: Board, current: int) -> bool:
        next = b.next_empty(current)

        if next is None:
            return True

        for val in range(1, self.num_cells_in_group(next.group_id)+1):
            if b.values_to(val) in self.values_tried:
                continue
            
            b.set_cell_value(next.cell_id, val)
            print(b)
            print("-")

            if self.board_valid(b):

                if self.solve(b, current+1):
                    print("going deeper")
                    return True

            b.set_cell_value(next.cell_id, 0)
            # self.values_tried[next.cell_id].append(val)
            self.values_tried.append(b.values_to(val))
            print(self.values_tried)

        return False

    def num_cells_in_group(self, id: int) -> int:
        return util.flat_list(self.grouping).count(id)

    def board_valid(self, b: Board) -> bool:
        groups_valid = all([b.group_valid(id) for id in range(self.num_groups)])
        neighbours_valid = all([b.neighbours_valid(id) for id in range(b.w*b.h)])

        return groups_valid and neighbours_valid
