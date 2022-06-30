# For animation
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.artist import Artist

import sample_board
from board import Board
from solver import Solver
from util import configure_plot

# Used to display animation
fps = 100
snapshots = []
texts = []

# Read in sample data
initial_board = sample_board.initial_board
grouping = sample_board.grouping

# Set up plot
fig = plt.figure(figsize=(7,7))
# im = plt.imshow(grouping, interpolation='none', aspect='auto',cmap='tab20c')


from MarchingSquares import MarchingSquares

def draw_board(board_size:tuple):
    pass
    # y = [[1,1], [2,1], [2,2], [1,2], [0.5,1.5]]

    # p = plt.Polygon(y, facecolor = 'k')

    # fig, ax = plt.subplots()

    # ax.add_patch(p)
    # ax.set_xlim([0,3])
    # ax.set_ylim([0,3])
    # plt.show()
    # plt.figure(figsize=(7,7))
    # plt.axes(xlim=(0, board_size[0]), ylim=(0, board_size[1]))
    #plt.title(options.title, loc='left')
    #plt.title("Bowyer-Watson Triangulation", loc='center')
    # plt.xticks([])
    # plt.yticks([])

    # Plot bounds
    # b = plt.Rectangle((0,0),2,1, color='black', fill=False, zorder=0)
    # plt.gca().add_patch(b)
    # plt.show()


def animate_text(i):
    global texts
    last_values= list(snapshots[i-1])
    values = list(snapshots[i])
    
    # Clear existing text
    for t in texts:
        Artist.remove(t)
    texts = []

    # Add new text
    for y in range(len(values)):
        for x in range(len(values[0])):
            if values[y][x] == 0:
                continue
            
            # Set color, purple for static, yellow for current
            color = 'navy' if initial_board[y][x] != 0 else 'black'
            color = 'yellow' if values[y][x] != last_values[y][x] else color

            t = plt.text(x, y, values[y][x], size=20, horizontalalignment='center', verticalalignment='center', fontweight="black", color=color)
            texts.append(t)
    
    return [t]

def animate_solution():
    _ = animation.FuncAnimation(fig, animate_text, frames = len(snapshots), interval = 1000 / fps, blit=True)
    plt.show()


import matplotlib.pyplot as plt
if __name__ == "__main__":

    # grid = [
    #     [1,1,1,1],
    #     [1,2,2,1],
    #     [1,2,2,1],
    #     [1,1,1,1]
    # ]    
    # ms = MarchingSquares(grid, lower_threshold=2)
    # ms.plot_edges(plot_grid=True)
    plt.xlim((0,8))
    plt.ylim((0,7))
    
    for i in range(12):
        ms = MarchingSquares(grouping, lower_threshold=i, upper_threshold=i)
        ms.plot_edges()
    plt.show()

    #draw_board((8,7))
    # b = Board(initial_board, grouping)
    # s = Solver(b)

    # s.solve(b)

    # # Solved board
    # print(s.board)

    # # Animate solution
    # snapshots = s.boards
    # configure_plot(s.board.w, s.board.h)
    # animate_solution()

