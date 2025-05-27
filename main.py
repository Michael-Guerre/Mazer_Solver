from maze import Maze
from graphics import Window
from cell import Cell


def main():
    win = Window(800, 600)
    maze = Maze(
        x1=10,
        y1=10,
        num_rows=10,
        num_cols=10,
        cell_size_x=50,
        cell_size_y=50,
        win=win
    )
    win.wait_for_close()


main()
