from random import randint
from math import inf
import matplotlib.pyplot as plt


def random_grid(size:tuple = (10,10), num_range:tuple = (0,3)) -> list:
    """
    Generate a random grid of ints at a given ``size``. The numbers will lie within the given ``num_range``
    """
    return [[randint(*num_range) for _ in range(size[0])] for _ in range(size[1])]


class MarchingSquares(object):
    """
    An object for a marching-squares implementation.
    """

    def __init__(self, grid:list, lower_threshold:float = 1, upper_threshold:float = inf) -> None:

        self.lower_threshold = lower_threshold
        self.upper_threshold = upper_threshold


        self.h = len(grid)
        self.w = len(grid[0])
        self.N = self.w * self.h

        assert 1 < self.h and 1 < self.w  # We dont want any 1D grids

        self.grid = grid
        self.binary_grid = self.__binarize(self.grid)
        self.cells = self.__calc_cell_values(self.binary_grid)
        

    def __binarize(self, grid: list) -> list:
        """ Binarize the grid to 0 and 1 using a threshold. Threshold defaults to 1. """
        g = [[0 for _ in range(self.w)] for _ in range(self.h)]

        for x, row in enumerate(grid):
            for y, cell in enumerate(row):
                g[x][y] = int(self.lower_threshold <= cell and cell <= self.upper_threshold)            
        return g


    def __calc_cell_values(self, grid: list) -> list:
        """ 
        Every 2x2 block of cells in the binary image forms a contouring cell, so the whole image is 
        represented by a grid of such cells.
        Every cell is given a number between 0 and 15 corresponding to the neighbour configuration.
        Note that this grid of cells is one cell smaller in each direction than the original 2D field.
        
        Source: https://en.wikipedia.org/wiki/Marching_squares
        """

        cells = [[0 for _ in range(self.w-1)] for _ in range(self.h-1)]

        for y in range(self.h-1):
            for x in range(self.w-1):
                # Use 1 - x to invert 0 and 1 and use as a bitmask
                cells[y][x] = 8*(1-grid[y][x]) + 4*(1-grid[y][x+1]) + 1*(1-grid[y+1][x]) + 2*(1-grid[y+1][x+1])

        return cells


    def plot_polygons(self, fill:bool = True, plot_grid:bool = False, edge_color:str = 'orange', fill_color:str = 'orange', fig_size:tuple = (7,7)) -> None:
        """
        Plot the polygons of the marching squares sequence.
        """

        h,w = self.h-1, self.w-1
        
        plt.figure(figsize=fig_size)
        plt.axes(xlim=(0, w), ylim=(0, h))

        plt.title(f"N={self.N}", loc='left')
        plt.title("Marching Squares ", loc='center', fontweight='bold')
        
        if plot_grid:
            self.plot_grid()

        for y in range(h):
            for x in range(w):
                for polygon in contour_polygons[self.cells[y][x]]:

                    points = [[x0+x, h-y-1+y0] for (x0,y0) in polygon]
                    
                    p = plt.Polygon(points, edgecolor=edge_color, facecolor=fill_color, fill=fill)
                    plt.gca().add_patch(p)
            
        plt.show()


    def plot_edges(self, plot_grid:bool = False, edge_color:str = 'orange', fig_size:tuple = (7,7)) -> None:
        """ Plot the outer edges of the resulting marching squares sequence """
        
        h,w = self.h-1, self.w-1
        
        # plt.figure(figsize=fig_size)
        # plt.axes(xlim=(0, w), ylim=(0, h))

        # plt.title(f"N={self.N}", loc='left')
        # plt.title("Marching Squares ", loc='center', fontweight='bold')
        
        if plot_grid:
            self.plot_grid()

        for y in range(h):
            for x in range(w):

                cell_val = self.cells[y][x]
                for edge in tight_edges[cell_val]:

                    x1 = edge[0][0]+x
                    x2 = edge[1][0]+x
                    y1 = h+edge[0][1]-y-1
                    y2 = h+edge[1][1]-y-1

                    x1 -= 0.5 if x1 == 0.5 else 0
                    x2 -= 0.5 if x2 == 0.5 else 0
                    x1 += 0.5 if x1 == w+0.5 else 0
                    x2 += 0.5 if x2 == w+0.5 else 0

                    y1 -= 0.5 if y1 == 0.5 else 0
                    y2 -= 0.5 if y2 == 0.5 else 0
                    y1 += 0.5 if y1 == h+0.5 else 0
                    y2 += 0.5 if y2 == h+0.5 else 0
                    
                    plt.plot([x1, x2],[y1, y2], color=edge_color, zorder=1)
        # plt.show()


    def plot_grid(self, color:str = 'black') -> None:
        """ Plot the binary grid to show which grid cells are active """

        for y in range(self.h):
            for x in range(self.w):

                if self.binary_grid[y][x]:
                    plt.plot([x],[self.h-y-1], marker='.', color=color, markersize=4)



# tight_edges = {
#     0  : [],
#     1  : [[[0.5, 0],[0.5, 0.5]],[[0.5, 0.5],[0, 0.5]]],
#     2  : [[[1, 0.5],[0.5, 0.5]],[[0.5, 0.5], [0.5, 0]]],
#     3  : [[[1, 0.5],[0, 0.5]]],
#     4  : [[[1, 0.5],[0.5, 0.5]],[[0.5, 0.5],[0.5, 1]]],
#     5  : [[[1, 0.5],[0.5, 0.5]],[[0.5, 0.5],[0.5, 0]],[[0, 0.5],[0.5, 0.5]],[[0.5, 0.5],[0.5, 1]]],
#     6  : [[[0.5, 0],[0.5, 1]]],
#     7  : [[[0, 0.5],[0.5, 0.5]],[[0.5, 0.5],[0.5, 1]]],
#     8  : [[[0, 0.5],[0.5, 0.5]],[[0.5, 0.5],[0.5 , 1]]],
#     9  : [[[0.5, 0],[0.5, 1]]],
#     10 : [[[0.5, 0],[0.5, 0.5]],[[0.5, 0.5],[0, 0.5]],[[1, 0.5],[0.5, 0.5]],[[0.5, 0.5],[0.5, 1]]],
#     11 : [[[1, 0.5],[0.5, 0.5]],[[0.5, 0.5],[0.5, 1]]],
#     12 : [[[0, 0.5],[1, 0.5]]],
#     13 : [[[0.5, 0],[0.5, 0.5]],[[0.5, 0.5],[1, 0.5]]],
#     14 : [[[0.5, 0],[0.5, 0.5]],[[0.5, 0.5],[0, 0.5]]],
#     15 : [],
# }


tight_edges = {
    0  : [],
    1  : [[[1, 0.5],[1, 1]],[[1, 1],[0.5, 1]]],
    2  : [[[1.5, 1],[1, 1]],[[1, 1], [1, 0.5]]],
    3  : [[[1.5, 1],[0.5, 1]]],
    4  : [[[1.5, 1],[1, 1]],[[1, 1],[1, 1.5]]],
    5  : [[[1.5, 1],[1, 1]],[[1, 1],[1, 0.5]],[[0.5, 1],[1, 1]],[[1, 1],[1, 1.5]]],
    6  : [[[1, 0.5],[1, 1.5]]],
    7  : [[[0.5, 1],[1, 1]],[[1, 1],[1, 1.5]]],
    8  : [[[0.5, 1],[1, 1]],[[1, 1],[1 , 1.5]]],
    9  : [[[1, 0.5],[1, 1.5]]],
    10 : [[[1, 0.5],[1, 1]],[[1, 1],[0.5, 1]],[[1.5, 1],[1, 1]],[[1, 1],[1, 1.5]]],
    11 : [[[1.5, 1],[1, 1]],[[1, 1],[1, 1.5]]],
    12 : [[[0.5, 1],[1.5, 1]]],
    13 : [[[1, 0.5],[1, 1]],[[1, 1],[1.5, 1]]],
    14 : [[[1, 0.5],[1, 1]],[[1, 1],[0.5, 1]]],
    15 : [],
}

contour_edges = {
    0  : [],
    1  : [[[0.5, 0],[0, 0.5]]],
    2  : [[[1, 0.5],[0.5, 0]]],
    3  : [[[1, 0.5],[0, 0.5]]],
    4  : [[[1, 0.5],[0.5, 1]]],
    5  : [[[1, 0.5],[0.5, 0]],[[0, 0.5],[0.5, 1]]],
    6  : [[[0.5, 0],[0.5, 1]]],
    7  : [[[0, 0.5],[0.5, 1]]],
    8  : [[[0, 0.5],[0.5 , 1]]],
    9  : [[[0.5, 0],[0.5, 1]]],
    10 : [[[0.5, 0],[0, 0.5]],[[1, 0.5],[0.5, 1]]],
    11 : [[[1, 0.5],[0.5, 1]]],
    12 : [[[0, 0.5],[1, 0.5]]],
    13 : [[[0.5, 0],[1, 0.5]]],
    14 : [[[0.5, 0],[0, 0.5]]],
    15 : [],
}

contour_polygons = {
    0  : [[[0,0],[1,0],[1,1],[0,1]]],
    1  : [[[0.5, 0],[1,0],[1,1],[0,1],[0, 0.5]]],
    2  : [[[1, 0.5],[1,1],[0,1],[0,0],[0.5, 0]]],
    3  : [[[1, 0.5],[1,1],[0,1],[0, 0.5]]],
    4  : [[[1, 0.5],[0.5, 1],[0,1],[0,0],[1,0]]],
    5  : [[[1, 0.5],[0.5, 0],[1,0]],[[0, 0.5],[0.5, 1],[0,1]]],
    6  : [[[0.5, 0],[0.5, 1],[0,1],[0,0]]],
    7  : [[[0, 0.5],[0.5, 1],[0,1]]],
    8  : [[[0.5, 1],[0, 0.5],[0,0],[1,0],[1,1]]],
    9  : [[[0.5, 1],[0.5, 0],[1,0],[1,1]]],
    10 : [[[0.5, 0],[0, 0.5],[0,0]],[[1, 0.5],[0.5, 1],[1,1]]],
    11 : [[[0.5, 1],[1, 0.5],[1,1]]],
    12 : [[[1, 0.5],[0, 0.5],[0,0],[1,0]]],
    13 : [[[1, 0.5],[0.5, 0],[1,0]]],
    14 : [[[0.5, 0],[0, 0.5],[0,0]]],
    15 : [],
}

