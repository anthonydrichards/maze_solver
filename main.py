from gui.window import Window
from gui.point import Point
from gui.line import Line
from maze.cell import Cell
from maze.maze import Maze

def main():
    
    win = Window(800, 600)
    maze = Maze(Point(10, 10), 5, 7, 100, 100, win)    
    win.wait_for_close()

main()