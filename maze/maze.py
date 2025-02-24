from gui.point import Point
from maze.cell import Cell
import time

class Maze:
    def __init__(
        self,
        origin,
        num_cols,
        num_rows,
        cell_size_x,
        cell_size_y,
        win = None
    ):
        self.origin = origin
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.__win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        curr_x = self.origin.x
        for i in range(self.num_cols):
            cell_col = []
            curr_y = self.origin.y
            for j in range(self.num_rows):
                cell_col.append(Cell(Point(curr_x, curr_y), Point(curr_x + self.cell_size_x, curr_y + self.cell_size_y), self.__win))
                curr_y += self.cell_size_y
            self._cells.append(cell_col)
            curr_x += self.cell_size_x
        self._draw_all_cells()
        self._break_entrance_and_exit()
        
    def _draw_all_cells(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.1)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].top_wall = False
        self._cells[0][0].draw()
        self._animate()
        self._cells[self.num_cols - 1][self.num_rows - 1].bottom_wall = False
        self._cells[self.num_cols - 1][self.num_rows - 1].draw()
        self._animate()

        
