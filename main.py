from gui.window import Window
from gui.point import Point
from maze.maze import Maze

def main():    
    win = Window(1000, 1000)
    maze = Maze(Point(10, 10), 9, 9, 100, 100, win)    
    maze.solve()
    win.wait_for_close()

main()