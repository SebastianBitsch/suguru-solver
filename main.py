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
im = plt.imshow(grouping, interpolation='none', aspect='auto',cmap='tab20c')


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


if __name__ == "__main__":
    b = Board(initial_board, grouping)
    s = Solver(b)

    s.solve(b)

    # Solved board
    print(s.board)

    # Animate solution
    snapshots = s.boards
    configure_plot(s.board.w, s.board.h)
    animate_solution()

