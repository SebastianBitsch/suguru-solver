from dataclasses import dataclass

# TODO: probablby redudant using a class here
@dataclass
class Cell:
    cell_id: int
    group_id: int
    value: int = 0