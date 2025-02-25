from gui.point import Point
from maze.cell import Cell
import time, random

class Maze:
    def __init__(
        self,
        origin,
        num_cols,
        num_rows,
        cell_size_x,
        cell_size_y,
        win = None,
        seed = None
    ):
        self.origin = origin
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.__win = win
        self._cells = []
        self._create_cells()
        if seed is not None:            
            random.seed(seed)
    
    def solve(self):
        self._solve_r(0, 0)

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
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        
    def _draw_all_cells(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)

    def _reset_cells_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._cells[i][j].visited = False

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()        

    def _animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.1)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].top_wall = False
        self._cells[0][0].draw()        
        self._cells[self.num_cols - 1][self.num_rows - 1].bottom_wall = False
        self._cells[self.num_cols - 1][self.num_rows - 1].draw()        

    def _break_walls_r(self, i, j):        
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            possible_next_cells = self._get_possible_next_cells(i, j)       
                
            if len(possible_next_cells) == 0:
                current_cell.draw()                
                return

            next_cell_index = random.randrange(0, len(possible_next_cells))
            next_cell = possible_next_cells[next_cell_index]
            match next_cell[3]:
                case "left":
                    current_cell.left_wall = False
                    next_cell[2].right_wall = False
                case "bottom":
                    current_cell.bottom_wall = False
                    next_cell[2].top_wall = False
                case "right":
                    current_cell.right_wall = False
                    next_cell[2].left_wall = False
                case "top":
                    current_cell.top_wall = False
                    next_cell[2].bottom_wall = False
            
            self._break_walls_r(next_cell[0], next_cell[1])
    
    def _get_possible_next_cells(self, i, j):
        adjacent_cells = []
        if i > 0:                
            adjacent_cells.append((i - 1, j, self._cells[i - 1][j], "left"))
        if j > 0:
            adjacent_cells.append((i, j - 1, self._cells[i][j - 1], "top"))
        if i < self.num_cols - 1:
            adjacent_cells.append((i + 1, j, self._cells[i + 1][j], "right"))
        if j < self.num_rows - 1:
            adjacent_cells.append((i, j + 1, self._cells[i][j + 1], "bottom"))
        
        possible_next_cells = []
        for adjacent_cell in adjacent_cells:                
            if not adjacent_cell[2].visited:
                possible_next_cells.append(adjacent_cell)            
        
        return possible_next_cells
        
    def _solve_r(self, i, j):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True

        possible_next_cells = self._get_possible_next_cells(i, j)
        for next_cell in possible_next_cells:
            can_visit = not next_cell[2].visited
            match next_cell[3]:
                case "left":
                    if current_cell.left_wall:
                        can_visit = False
                case "bottom":
                    if current_cell.bottom_wall:
                        can_visit = False
                case "right":
                    if current_cell.right_wall:
                        can_visit = False
                case "top":
                    if current_cell.top_wall:
                        can_visit = False

            if can_visit:
                current_cell.draw_move(next_cell[2])
                if self._solve_r(next_cell[0], next_cell[1]):
                    return True
                current_cell.draw_move(next_cell[2], undo=True)
        
        return False

        
