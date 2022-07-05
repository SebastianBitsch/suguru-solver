import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.artist import Artist

from MarchingSquares import MarchingSquares
from board import Board


class Solver:

    def __init__(self, initial_board: Board) -> None:
        self.recursions_deep = 0
        self.board = initial_board
        self.values_tried = []
        

        # Only used for animating the solution later, 
        # the first board is the initial board, the last is the solution
        self.boards = [initial_board.as_list()]

        self.text_fields = []
    

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


    def plot_solution(self, figsize:tuple = (7,7)):
        """ Plot the board and the solution found """
        fig, ax = self.__configure_plot(figsize)

        self.__draw_grouping(fig, ax)
        self.__draw_board_values(len(self.boards)-1)

        plt.show()
        

    def animate_solution(self, figsize:tuple = (7,7), fps: int = 100):
        """ Animate the process of finding the solution to the board """
        fig, ax = self.__configure_plot(figsize)

        self.__draw_grouping(fig, ax)
        _ = animation.FuncAnimation(fig, self.__draw_board_values, frames = len(self.boards), interval = 1000 / fps, repeat=False)

        plt.show()


    def __draw_board_values(self, i:int):
        
        values = list(self.boards[i])
        
        # Clear existing text
        for t in self.text_fields:
            Artist.remove(t)
        self.text_fields = []

        # Add new text
        for y in range(len(values)):
            for x in range(len(values[0])):
                if values[y][x] == 0:
                    continue
                
                # Set color, purple for static
                color = 'limegreen' if self.boards[i][y][x] == self.boards[-1][y][x] else 'black'
                color = 'darkorchid' if self.boards[0][y][x] != 0 else color
                

                t = plt.text(x+0.5, len(values)-y-1+0.5, values[y][x], size=20, horizontalalignment='center', verticalalignment='center', fontweight="black", color=color)
                self.text_fields.append(t)
        
        # Hacky way of making sure plt actually renderes the last digit, no idea how it works but it does
        # t = plt.text(-2,-2, 0, size=20, horizontalalignment='center', verticalalignment='center', fontweight="black", color=color)
        # return [t]


    def __draw_grouping(self, fig: plt.Figure, ax: plt.Axes):
        """ Draw the grouping i.e. the clumps of numbers, using Marching Squares to determinte the bounds"""
        for i in range(self.board.num_groups):
            ms = MarchingSquares(self.board.grouping, lower_threshold=i, upper_threshold=i)
            ms.plot_edges(fig, ax)


    def __configure_plot(self, figsize:tuple = (7,7)):
        """ Helper function to do basic setup of the plot """
        fig, ax = plt.subplots(figsize=figsize)
        ax.grid(True, color='lightgrey', linestyle='-', linewidth=1, zorder=0)

        ax.set_xlim((0,self.board.w))
        ax.set_ylim((0,self.board.h))

        # Hide ticks
        ax.tick_params(axis='x', colors=(0,0,0,0))
        ax.tick_params(axis='y', colors=(0,0,0,0))

        return fig, ax
