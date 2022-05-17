from dataclasses import dataclass, field

# groups = [
#     [0,8,16],
#     [1,2,9,10,17],
#     [3,4,5,12,13],
#     [6,7,15,23],
#     [11,18,19,26,27],
#     [14,21,22,29,30],
#     [20,28,36,44,]
#     [24,25,32,33],
#     [31,38,39,47],
#     [34,35,42,43,51],
#     [37,45,46,53],
#     [54,55],
#     [52],
#     [40,41,48,49,50],
# ]


@dataclass
class Cell:
    cell_id: int
    group_id: int
    value: int = 0
    static: bool = False
    # values_tried: list[int] = field(default_factory=list)

    def empty(self) -> bool:
        return self.value == 0


"""
3 | 3 | 3 | 3
- + - + - + - 
3 | 3 | 3 | 3
- + - + - + - 
3 | 3 | 3 | 3
- + - + - + - 
3 | 3 | 3 | 3
"""