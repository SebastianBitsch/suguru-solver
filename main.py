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
# fig = plt.figure(figsize=(7,7))
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
    last_values = list(snapshots[i-1])
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
            color = 'darkorchid' if initial_board[y][x] != 0 else 'black'
            color = 'dodgerblue' if values[y][x] != last_values[y][x] else color
            

            t = plt.text(x+0.5, len(values)-y-1+0.5, values[y][x], size=20, horizontalalignment='center', verticalalignment='center', fontweight="black", color=color)
            texts.append(t)
    
    # Hacky way of making sure plt actually renderes the last digit, no idea how it works but it does
    t = plt.text(0,0, 0, size=20, horizontalalignment='center', verticalalignment='center', fontweight="black", color=color)
    return [t]


def animate_solution(fig):
    _ = animation.FuncAnimation(fig, animate_text, frames = len(snapshots), interval = 1000 / fps, blit=True)
    plt.show()


import matplotlib.pyplot as plt
if __name__ == "__main__":

    
    w, h = len(grouping[0]), len(grouping)
    num_groups = len({x for l in grouping for x in l})


    fig, ax = plt.subplots(figsize=(7,7))

    ax.grid(True, color='lightgrey', linestyle='-', linewidth=1, zorder=0)

    ax.set_xlim((0,w))
    ax.set_ylim((0,h))

    # Hide ticks
    ax.tick_params(axis='x', colors=(0,0,0,0))
    ax.tick_params(axis='y', colors=(0,0,0,0))


    for i in range(num_groups):
        ms = MarchingSquares(grouping, lower_threshold=i, upper_threshold=i)
        ms.plot_edges(fig, ax)

    #plt.show()
    
    #draw_board((8,7))
    b = Board(initial_board, grouping)
    s = Solver(b)

    s.solve(b)

    # # # Solved board
    # # print(s.board)

    # # # Animate solution
    snapshots = s.boards
    # configure_plot(s.board.w, s.board.h)
    animate_solution(fig)

