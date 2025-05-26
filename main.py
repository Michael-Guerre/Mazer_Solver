from graphics import Window
from cell import Cell


def main():
    win = Window(800, 600)
    cell = Cell(win)
    cell.draw(100, 100, 200, 200)
    cell2 = Cell(win)
    cell2.draw(200, 100, 300, 200)
    cell.draw_move(cell2)
    win.wait_for_close()


main()
