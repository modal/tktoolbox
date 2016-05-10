import tkinter as tk
import random as rd


class Universe(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = dict()
        for i in range(0, height):
            for j in range(0, width):
                self.cells[(i, j)] = Cell((i, j), 0, width, height)

    def generate_random(self):
        for current_cell in self.cells:
            self.cells[current_cell].state = rd.randint(0, 3)

    def apply_rules(self):
        next_state = dict()
        for current_cell in self.cells:
            if self.cells[current_cell].state == 3:
                if self.cells[current_cell].count_electron_heads(self) == 1:
                    next_state[current_cell] = 1
                elif self.cells[current_cell].count_electron_heads(self) == 2:
                    next_state[current_cell] = 1
                else:
                    next_state[current_cell] = 3
            elif self.cells[current_cell].state == 2:
                next_state[current_cell] = 3
            elif self.cells[current_cell].state == 1:
                next_state[current_cell] = 2
            else:
                next_state[current_cell] = 0

        for current_cell in next_state:
            self.cells[current_cell].state = next_state[current_cell]

    def plain_text_display(self):
        for i in range(0, self.height):
            row = list()
            for j in range(0, self.width):
                row.append(self.cells[(i, j)].state)
            print(row)


class Cell(object):
    def __init__(self, coordinates, state, universe_width, universe_height):
        self.state = state
        self.coordinates = coordinates
        self.neighborhood = [[self.coordinates[0] - 1, self.coordinates[1] - 1],
                             [self.coordinates[0] - 1, self.coordinates[1]],
                             [self.coordinates[0] - 1, self.coordinates[1] + 1],
                             [self.coordinates[0], self.coordinates[1] - 1],
                             [self.coordinates[0], self.coordinates[1] + 1],
                             [self.coordinates[0] + 1, self.coordinates[1] - 1],
                             [self.coordinates[0] + 1, self.coordinates[1]],
                             [self.coordinates[0] + 1, self.coordinates[1] + 1]]

        for i in range(0, len(self.neighborhood)):
            if self.neighborhood[i][0] < 0:
                self.neighborhood[i][0] = universe_height - 1
            elif self.neighborhood[i][0] > universe_height - 1:
                self.neighborhood[i][0] = 0
            if self.neighborhood[i][1] < 0:
                self.neighborhood[i][1] = universe_width - 1
            elif self.neighborhood[i][1] > universe_width - 1:
                self.neighborhood[i][1] = 0

    def count_electron_heads(self, universe):
        electron_heads_count = 0
        for neighbor_cell_coordinates in self.neighborhood:
            if universe.cells[(neighbor_cell_coordinates[0], neighbor_cell_coordinates[1])].state == 1:
                electron_heads_count += 1
        return electron_heads_count


class GUI(tk.Tk):
    def __init__(self, universe):
        tk.Tk.__init__(self)
        self.cell_size = 12
        self.ui_frame = tk.Frame(self, width=self.cell_size*universe.width, height=60, bg="#282729")
        self.ui_frame.pack(fill="x", expand=True)
        self.cell_canvas = tk.Canvas(self, width=self.cell_size*universe.width, height=self.cell_size*universe.height,
                                     borderwidth=0, highlightthickness=0)
        self.cell_canvas.pack(fill="both", expand=True)
        self.cells = dict()
        for i in range(0, universe.height):
            for j in range(0, universe.width):
                if universe.cells[(i, j)].state == 1:
                    color = "#0099FF"
                elif universe.cells[(i, j)].state == 2:
                    color = "#CCFFFF"
                elif universe.cells[(i, j)].state == 3:
                    color = "#EDBE02"
                else:
                    color = "#0C1010"
                self.cells[(i, j)] = self.cell_canvas.create_rectangle(j*self.cell_size, i*self.cell_size,
                                                                       (j+1)*self.cell_size, (i+1)*self.cell_size,
                                                                       fill=color, tag=universe.cells[(i, j)])
        self.draw_button = tk.Button(self.ui_frame, text="Draw", command=lambda: self.draw(universe))
        self.draw_button.pack(side="left")

    def draw(self, universe):
        for i in range(0, universe.height):
            for j in range(0, universe.width):
                if universe.cells[(i, j)].state == 1:
                    color = "#0099FF"
                elif universe.cells[(i, j)].state == 2:
                    color = "#CCFFFF"
                elif universe.cells[(i, j)].state == 3:
                    color = "#EDBE02"
                else:
                    color = "#0C1010"
                self.cell_canvas.itemconfig(self.cells[(i, j)], fill=color)

        universe.apply_rules()
        self.after(200, lambda: self.draw(universe))




wireworld = Universe(20, 20)
wireworld.generate_random()
g = GUI(wireworld)

g.mainloop()
