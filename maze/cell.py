from gui.point import Point
from gui.line import Line

class Cell:
    def __init__(self, top_left, bottom_right, win=None, left_wall=True, right_wall=True, top_wall=True, bottom_wall=True):
        self.__win = win
        self.left_wall = left_wall
        self.right_wall = right_wall
        self.top_wall = top_wall
        self.bottom_wall = bottom_wall
        self.__top_left = top_left
        self.__bottom_right = bottom_right
        self.__top_right = Point(bottom_right.x, top_left.y)
        self.__bottom_left = Point(top_left.x, bottom_right.y)
        self.center = Point((top_left.x + bottom_right.x) / 2, (top_left.y + bottom_right.y) / 2)
    
    def draw(self):
        if self.__win is None:
            return
        if self.left_wall:
            self.__win.draw_line(Line(self.__top_left, self.__bottom_left), "black")
        else:
            self.__win.draw_line(Line(self.__top_left, self.__bottom_left), "white")
        if self.right_wall:
            self.__win.draw_line(Line(self.__top_right, self.__bottom_right), "black")
        else:
            self.__win.draw_line(Line(self.__top_right, self.__bottom_right), "white")
        if self.top_wall:
            self.__win.draw_line(Line(self.__top_left, self.__top_right), "black")
        else:
            self.__win.draw_line(Line(self.__top_left, self.__top_right), "white")
        if self.bottom_wall:
            self.__win.draw_line(Line(self.__bottom_left, self.__bottom_right), "black")
        else:
            self.__win.draw_line(Line(self.__bottom_left, self.__bottom_right), "white")
    
    def draw_move(self, to_cell, undo=False):
        line_color = "red"
        if undo:
            line_color = "gray"
        
        self.__win.draw_line(Line(self.center, to_cell.center), line_color)
