

import random
from time import sleep
from cell import Cell


class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        if seed is not None:
            random.seed(seed)
        self.__create_cells()
        self.__break_entrance_and_exit()
        if self.__num_rows > 0 and self.__num_cols > 0:
            self.__break_calls_r(0, 0)
            self.__reset_cells_visited()

    def __create_cells(self):
        for col in range(self.__num_cols):
            cell_col = []
            self.__cells.append(cell_col)
            for row in range(self.__num_rows):
                cell = Cell(self.__win)
                cell_col.append(cell)
                self.__draw_cell(col, row)

    
    def __draw_cell(self,col,row):
        x1 = self.__x1 + col * self.__cell_size_x
        y1 = self.__y1 + row * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self.__cells[col][row].draw(x1, y1, x2, y2)
        self.animate()

    def animate(self):
        if self.__win is not None:
            self.__win.redraw()
        sleep(0.05)

    def __break_entrance_and_exit(self):
        if self.__num_rows > 0 and self.__num_cols > 0:
            # Break the top wall of the first cell
            self.__cells[0][0].has_top_wall = False
            self.__draw_cell(0, 0)
            # Break the bottom wall of the last cell
            self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
            self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)
    
    def __break_calls_r(self,i,j):
        self.__cells[i][j].visited = True
        while 1:
            directions = []
            if i > 0 and not self.__cells[i - 1][j].visited:
                directions.append((i-1,j))
            if i < self.__num_cols - 1 and not self.__cells[i + 1][j].visited:
                directions.append((i+1,j))
            if j > 0 and not self.__cells[i][j - 1].visited:
                directions.append((i,j-1))
            if j < self.__num_rows - 1 and not self.__cells[i][j + 1].visited:
                directions.append((i,j+1))
            if not directions:
                return
            i2, j2 = random.choice(directions)
            if i2 < i:
                self.__cells[i][j].has_left_wall = False
                self.__cells[i2][j2].has_right_wall = False
            elif i2 > i:
                self.__cells[i][j].has_right_wall = False
                self.__cells[i2][j2].has_left_wall = False
            elif j2 < j:
                self.__cells[i][j].has_top_wall = False
                self.__cells[i2][j2].has_bottom_wall = False
            elif j2 > j:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[i2][j2].has_top_wall = False
            self.__draw_cell(i, j)
            self.__draw_cell(i2, j2)
            self.animate()
            self.__break_calls_r(i2, j2)

    def __reset_cells_visited(self):
        for col in self.__cells:
            for cell in col:
                cell.visited = False


    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self, i, j):
        self.animate()
        self.__cells[i][j].visited = True
        if i == self.__num_cols - 1 and j == self.__num_rows - 1:
            return True
        if i > 0 and not self.__cells[i - 1][j].visited and not self.__cells[i][j].has_left_wall:
            self.__cells[i][j].draw_move(self.__cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else :
                self.__cells[i][j].draw_move(self.__cells[i - 1][j], undo=True)
        if i < self.__num_cols - 1 and not self.__cells[i + 1][j].visited and not self.__cells[i][j].has_right_wall:
            self.__cells[i][j].draw_move(self.__cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i + 1][j], undo=True)
        if j > 0 and not self.__cells[i][j - 1].visited and not self.__cells[i][j].has_top_wall:
            self.__cells[i][j].draw_move(self.__cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j - 1], undo=True)
        if j < self.__num_rows - 1 and not self.__cells[i][j + 1].visited and not self.__cells[i][j].has_bottom_wall:   
            self.__cells[i][j].draw_move(self.__cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j + 1], undo=True)
        return False
