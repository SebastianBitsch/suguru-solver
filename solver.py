from board import Board
import util

class Solver:

    def __init__(self, initial_board: Board, grouping: list) -> None:
        self.board = initial_board
        self.grouping = grouping
        self.num_groups = len(set(util.flat_list(grouping)))

    def solve(self) -> bool:
        next = self.next_empty()

        if next is None:
            return True

        for val in range(self.num_cells_in_group(next.group_id)):
            b = self.copy()
            pass

    def num_cells_in_group(self, id) -> int:
        return util.flat_list(self.grouping).count(id)

    def board_valid(self, b: Board) -> bool:
        groups_valid = all([b.group_legal(id) for id in range(self.num_groups)])
        neighbours_valid = all([b.neighbours_legal(id) for id in range(b.w*b.h)])

        return groups_valid and neighbours_valid
