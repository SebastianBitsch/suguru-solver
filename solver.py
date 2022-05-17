from board import Board

class Solver:

    def __init__(self, initial_board: Board) -> None:
        self.recursions_deep = 0
        self.board = initial_board
        self.values_tried = []
        
        # Only used for animating the solution later
        self.boards = []
    

    # TODO: Add clarification to user when puzzle has no solution
    def solve(self, b: Board, current: int = 0) -> bool:
        """
        Recursive backtracking function call to solve a suguru puzzle. Moves in the reading direction 
        and backtracks one step whenever it reaches an invalid board state, continues untill the solution
        is found or no solution can be found.
        """
        self.recursions_deep += 1
        next = b.next_empty(current)

        if next is None:
            print(f"Solution found going {self.recursions_deep} recursions deep")
            return True

        # Loop through every possible value the cell can have, i.e. the number of cells in its group
        for val in range(1, b.num_cells_in_group(next.group_id)+1):

            # Skip if we have already explored this path
            if b.path_to(next.cell_id)+str(val) in self.values_tried:
                continue
            
            b.set_cell_value(next.cell_id, val)
            self.boards.append(b.as_list())
            self.board = b

            # If the state is valid do recursion
            if self.board_valid(b):
                if self.solve(b, current+1):
                    return True

            # Backtrack
            self.values_tried.append(b.path_to(next.cell_id)+str(val))
            b.set_cell_value(next.cell_id, 0)
            self.boards.append(b.as_list())

        return False


    def board_valid(self, b: Board) -> bool:
        """
        Calls group_valid and neighbours_valid functions on the board to determine wether all cells and
        groups are in valid configurations, if this is the case the board is legal and return true
        """
        groups_valid = all([b.group_valid(id) for id in range(b.num_groups)])
        neighbours_valid = all([b.neighbours_valid(id) for id in range(b.w*b.h)])

        return groups_valid and neighbours_valid
