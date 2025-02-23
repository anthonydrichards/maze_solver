from gui.point import Point
from maze.cell import Cell
import time

class Maze:
    def __init__(
        self,
        origin,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win
    ):
        self.origin = origin
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self._create_cells()

    def _create_cells(self):
        self.__cells = []
        curr_x = self.origin.x
        for i in range(self.num_cols):
            cell_col = []
            curr_y = self.origin.y
            for j in range(self.num_rows):
                cell_col.append(Cell(self.__win, Point(curr_x, curr_y), Point(curr_x + self.cell_size_x, curr_y + self.cell_size_y)))
                curr_y += self.cell_size_y
            self.__cells.append(cell_col)
            curr_x += self.cell_size_x
        self._draw_all_cells()
        
    def _draw_all_cells(self):
        for i in range(len(self.__cells)):
            for j in range(len(self.__cells[i])):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        self.__cells[i][j].draw()
        self._animate()

    def _animate(self):
        self.__win.redraw()
        time.sleep(0.1)
