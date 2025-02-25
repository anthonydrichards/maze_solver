import unittest
from maze.maze import Maze
from gui.point import Point


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(Point(0, 0), num_cols, num_rows, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_cell_position(self):
        num_cols = 12
        num_rows = 10
        cell_width = 10
        cell_height = 15
        m1 = Maze(Point(0, 0), num_cols, num_rows, cell_width, cell_height)
        expected_x = (num_cols * cell_width) - (cell_width / 2)
        expected_y = (num_rows * cell_height) - (cell_height / 2)
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].center.x,
            expected_x,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].center.y,
            expected_y,
        )
    
    def test_maze_cell_origin(self):
        num_cols = 12
        num_rows = 10
        cell_width = 10
        cell_height = 15
        origin_x = 10
        origin_y = 20
        m1 = Maze(Point(origin_x, origin_y), num_cols, num_rows, cell_width, cell_height)
        expected_x = (num_cols * cell_width) - (cell_width / 2) + origin_x
        expected_y = (num_rows * cell_height) - (cell_height / 2) + origin_y
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].center.x,
            expected_x,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].center.y,
            expected_y,
        )
    
    def test_maze_entrance(self):
        num_cols = 12
        num_rows = 10
        cell_width = 10
        cell_height = 15
        origin_x = 10
        origin_y = 20
        m1 = Maze(Point(origin_x, origin_y), num_cols, num_rows, cell_width, cell_height)        
        self.assertEqual(
            m1._cells[0][0].top_wall,
            False,
        )        
    
    def test_maze_exit(self):
        num_cols = 12
        num_rows = 10
        cell_width = 10
        cell_height = 15
        origin_x = 10
        origin_y = 20
        m1 = Maze(Point(origin_x, origin_y), num_cols, num_rows, cell_width, cell_height)        
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].bottom_wall,
            False,
        )
    
    def test_maze_reset_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(Point(0, 0), num_cols, num_rows, 10, 10)
        m1._reset_cells_visited()
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertEqual(
                    m1._cells[i][j].visited,
                    False
                )

if __name__ == "__main__":
    unittest.main()