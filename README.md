# Sudoku-Solver
 A Sudoku solver implementing the backtracking algorithm
 
 ## How it works
Basically, the algorithm puts in a number and checks if it is valid for the row, column, and the smaller 3 * 3 box, and moves on to the next empty box. When it comes across a situation when it cannot put a valid num, it **BACKTRACKS** to previous filled spot and tries to look for another number. It's way better than the Brute force approach.
