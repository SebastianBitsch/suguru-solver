import util
from cell import Cell

class Board:
    def __init__(self, board, grouping) -> None:
        self.w = len(board[0])
        self.h = len(board)

        self.grouping = util.flat_list(grouping)
        self.num_groups = len(set(self.grouping))

        self.cells = []

        # Initialize cells
        for y in range(self.h):
            for x in range(self.w):
                c = Cell(cell_id=len(self.cells), group_id=grouping[y][x], value=board[y][x])
                self.cells.append(c)


    def next_empty(self, i) -> Cell or None:
        while self.cells[i].value != 0:
            i += 1
            if i == self.w*self.h:
                return None
        
        return self.cells[i]


    def group_valid(self, group_id: int) -> bool:
        cell_values = [c.value for g, c in zip(self.grouping, self.cells) if g == group_id]
        return sum(cell_values) == sum(set(cell_values))
        
    
    # TODO: Not the neatest way of checking
    def neighbours_valid(self, cell_id: int) -> bool:
        x, y = self.coords_from_id(cell_id)
        
        # Dont bother with checking empty cells
        if self.cells[cell_id].empty():
            return True

        # Look down
        if y != (self.h-1) and self.cells[cell_id].value == self.cells[cell_id+self.w].value:
            return False
        
        # Look right
        if x != (self.w-1) and self.cells[cell_id].value == self.cells[cell_id+1].value:
            return False
        
        # Look down right diagonal
        if x != (self.w-1) and y != (self.h-1) and self.cells[cell_id].value == self.cells[cell_id+1+self.w].value:
            return False
        
        # Look down left diagonal
        if x != 0 and y != (self.h-1) and self.cells[cell_id].value == self.cells[cell_id-1+self.w].value:
            return False
        
        return True
        
    def __repr__(self) -> str:
        lines = ""
        for y in range(self.h):
            line = ""
            for x in range(self.w):
                line += f" {self.cells[self.id_from_coords(x,y)].value}"
            lines += f"{line}\n"
        return lines
    
    def path_to(self, cell_id: int) -> str:
        return "".join([str(self.cells[x].value) for x in range(cell_id+1)])

    def num_cells_in_group(self, id: int) -> int:
        return self.grouping.count(id)


    def set_cell_value(self, cell_id: int, new_val: int) -> None:
        self.cells[cell_id].value = new_val

    def id_from_coords(self, x: int, y:int) -> int:
        return y*self.w + x

    def coords_from_id(self, id:int) -> tuple[int,int]:
        return (id % self.w, id // (self.h+1))


    def as_list(self) -> list:
        vals = [x.value for x in self.cells]
        vals_2d = []
        for i in range(self.w, self.h*self.w + self.w, self.w):
            vals_2d.append(vals[i-self.w:i])

        return vals_2d
