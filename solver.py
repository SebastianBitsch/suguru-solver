from board import Board
import util

class Solver:

    def __init__(self, initial_board: Board) -> None:
        self.board = initial_board
        self.boards = []
        self.values_tried = []
        self.recursions_deep = 0


    def solve(self, b: Board, current: int = 0) -> bool:
        self.recursions_deep += 1
        next = b.next_empty(current)

        if next is None:
            print(f"Solution found going {self.recursions_deep} recursions deep")
            return True

        for val in range(1, b.num_cells_in_group(next.group_id)+1):
            if b.path_to(next.cell_id)+str(val) in self.values_tried:
                continue
            
            b.set_cell_value(next.cell_id, val)
            self.boards.append(b.as_list())
            self.board = b

            if self.board_valid(b):
                if self.solve(b, current+1):
                    return True

            self.values_tried.append(b.path_to(next.cell_id)+str(val))
            b.set_cell_value(next.cell_id, 0)
            self.boards.append(b.as_list())

        return False


    def board_valid(self, b: Board) -> bool:
        groups_valid = all([b.group_valid(id) for id in range(b.num_groups)])
        neighbours_valid = all([b.neighbours_valid(id) for id in range(b.w*b.h)])

        return groups_valid and neighbours_valid
