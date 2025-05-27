import unittest
# assuming your `Maze` class is in a file called `maze.py`
from maze import Maze
class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )
    def test_maze_create_cells_empty(self):
        m1 = Maze(0, 0, 0, 0, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            0,
        )
    def test_maze_create_cells_one_cell(self):
        m1 = Maze(0, 0, 1, 1, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            1,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            1,
        )
    
    def test_maze_draw_path(self):
        m1 = Maze(0, 0, 5, 5, 10, 10)
        m1._Maze__cells[0][0].draw_move(m1._Maze__cells[1][1])
        m1._Maze__cells[1][1].draw_move(m1._Maze__cells[0][0], undo=True)
        # This test is just to ensure that the method can be called without error.
        self.assertTrue(True)
        
    def test_maze_break_entrance_and_exit(self):
        m1 = Maze(0, 0, 5, 5, 10, 10)
        m1._Maze__break_entrance_and_exit()
        # This test is just to ensure that the method can be called without error.
        self.assertTrue(True)
if __name__ == "__main__":
    unittest.main()