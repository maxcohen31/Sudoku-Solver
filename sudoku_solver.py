# Sudoku Solver using backtracking algorithm
# Author: Emanuele - maxcohen31


grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]
 
class Sudoku:
    def __init__(self, grid):
        self.grid = grid
         
    def print_grid(self):
        for row_index, row in enumerate(self.grid): # Looping through the rows
            new_grid = '' # Define a string as new grid 
            if row_index % 3 == 0 and row_index != 0:
                print('------------')
            for i, element in enumerate(row): # Searching for the index and the equivalent element
                if i % 3 == 0 and i != 0:
                    new_grid += '|'
                if element == 0:
                    new_grid += '0' # Replace each zero with a str(0)        
                else:
                    new_grid += str(element) # 
            print(new_grid)
            
    # This method loop through the grid and search for empty spaces
    def empty_cells(self):
        for x in range(len(self.grid)): # Looping through the grid
            for y in range(len(self.grid[0])):
                if self.grid[x][y] == 0:
                    return (x, y) # Return a tuple (row, col)
                
        return None
                    
    # This method will check if the current puzzle is a solvable one
    # It takes the number and the position as a tuple
    def solvable_grid(self, n, position): 
        for x in range(len(self.grid[0])): # Check the row
            if self.grid[position[0]][x] == n and position[1] != x:
                return False
            
        for x in range(len(self.grid)): # Check the column
            if self.grid[x][position[1]] == n and position[0] != x:
                return False
    
        x_cord_1 = (position[1] // 3) * 3 # the first row index
        y_cord_1 = (position[0] // 3) * 3 # the first column index
        for x in range(x_cord_1, x_cord_1 + 3): # Loop through the boxes
            for y in range(y_cord_1, y_cord_1 + 3):
                if self.grid[x][y] == n and (x, y) == position:
                    return False
        return True        
    
    # This method check for box index
    def get_box_index(self, row, col):
        box_index = []
        x_cord_2 = (row // 3) * 3 # the first row index
        y_cord_3 = (col // 3) * 3 # the first column index
        for i in range(x_cord, x_cord + 3): # Loop through the boxes
            for j in range(y_cord, y_cord + 3):
                box_index.append((i, j))
        return box_index  
                
    # Method to check the box
    def get_box(self, row, col):
        box = []
        # This for loop will check for the indexes: 
        # example: (2, 6), (2, 7), (2, 8) will return the third box on the top-right [0, 0, 0, 0, 0, 0, 6, 0]
        for x, y in self.get_box_index(row, col):                      
            box.append(self.grid[x][y])
        print(box)            
    
    def solve_sudoku(self):
        time1 = 0
        finder = self.empty_cells() # Find an empty cell
        if not finder:
            return True # We solved the puzzle!
        else:
            row, col = finder
        
        # We loop through the values 1 to 9 and put one of these number in the solution
        for i in range(1, 10):
            if self.solvable_grid(i, (row, col)):
                self.grid[row][col] = i
                if self.solve_sudoku():  
                    return True
                    
                self.grid[row][col] = 0
        print("Solved in %0.2fs!" % (time2-time1))
        return False      
    def find_row(self, num_row):
        print(self.grid[num_row])
        
    def find_col(self, num_col):
        col = []
        for x in range(len(self.grid)):
            col.append(self.grid[x][num_col])
        print(col)   
             
