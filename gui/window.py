from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root_widget = Tk()
        self.__root_widget.title = "Maze Solver"
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas_widget = Canvas(self.__root_widget, bg="white", height=height, width=width)
        self.__canvas_widget.pack(fill=BOTH, expand=1)
        self.__window_running = False
    
    def draw_line(self, line, fill_color):
        line.draw(self.__canvas_widget, fill_color)
    
    def draw_cell(self, cell):
        cell.draw()
    
    def redraw(self):
        self.__root_widget.update_idletasks()
        self.__root_widget.update()

    def wait_for_close(self):
        self.__window_running = True
        while self.__window_running:
            self.redraw()

    def close(self):
        self.__window_running = False