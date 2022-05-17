# Suguru solver


## Solver
This is a small no-dependency suguru-solver that solves a m x n suguru puzzle using a recursive backtracking algorithm.  
An arbitrary board of size n x m can be fed to the algorithm using two 2-dimensional lists, representing the board and the grouping. See `sample_board.py` for an example.
The game can be played at [puzzlemadness](https://puzzlemadness.co.uk/suguru/small/2022/5/17#rules). The site also has an archive of hundreds of suguru puzzles which can be exported to this solver.

## The game
Surugu is a puzzle game much like sudoku.
The game is played on a grid split up in to irregular shaped regions. The number of cells in each region will vary from one cell, up to six cells for the bigger puzzles.

The aim of Suguru is to fill each n-sized region with the numbers 1-n. For example, if a region has 3 cells, you need to insert the numbers 1, 2 and 3 in to those cells. If a region has 4 cells, you need to insert the numbers 1, 2, 3, and 4 in to those cells.

Each number can't be next to the same number in an adjacent cell, this includes horizontally, vertically, and diagonally.

## Animation
Animation of the algorithm solving a 7 x 8 suguru puzzle, the animation is created with matplotlib.  
Areas of different colors represent regions that must include unique numbers as described above.

![animation](https://user-images.githubusercontent.com/72623007/168904030-c02b6384-bfc0-41e2-a3d3-0fccbb781166.gif)


