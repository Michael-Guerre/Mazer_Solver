from maze import Maze
from graphics import Window
from cell import Cell


def main():
    win = Window(800, 600)
    maze = Maze(
        x1=10,
        y1=10,
        num_rows=20,
        num_cols=20,
        cell_size_x=25,
        cell_size_y=25,
        win=win
    )
    maze.solve()
    win.wait_for_close()


main()
