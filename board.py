from re import I
import util
from cell import Cell

class Board:
    def __init__(self, board, grouping) -> None:
        self.w = len(board[0])
        self.h = len(board)
        self.grouping = util.flat_list(grouping)
        self.cells = []

        for y in range(self.h):
            for x in range(self.w):
                self.cells.append(Cell(len(self.cells), grouping[y][x], board[y][x], board[y][x] != 0))


    def next_empty(self, current) -> Cell or None:
        while self.cells[current+1].value == 0:
            current += 1
            if current == self.w*self.h:
                return None
        
        return self.cells[current]


    def group_legal(self, group_id: int) -> bool:
        cell_values = [c.value for g, c in zip(self.grouping, self.cells) if g == group_id]
        return sum(cell_values) == sum(set(cell_values))
        
    def neighbours_legal(self, cell_id: int) -> bool:
    
        # Dont bother with checking border cells or empty cells
        if self.cells[cell_id].empty() or cell_id % 8 == 0 or cell_id // self.h == self.h:
            return True

        # Look down
        if self.cells[cell_id].value == self.cells[cell_id+self.w].value:
            return False

        # Look right
        if self.cells[cell_id].value == self.cells[cell_id+1].value:
            return False
        
        return True
        
            

    def set_cell_value(self, cell_id: int, new_val: int) -> None:
        self.cells[cell_id].value = new_val

    def id_from_coords(self, x: int, y:int) -> int:
        return y*self.h + x
