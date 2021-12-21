import tkinter as tk
from random import shuffle

# пишем свой собственный класс, который наследуется от класса Button из tkinter
class New_Button(tk.Button):
    def __init__(self, master, x, y, number=0, *args, **kwargs):
        super(New_Button, self).__init__(master, *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.is_mine = False
        self.count_bomb = 0

    def __repr__(self):
        return f'New_Button{self.x}{self.y} {self.number} {self.is_mine}'


class MS:

    window = tk.Tk()
    row = 6
    column = 5
    mines = 5

    def __init__(self):
        self.buttons = []
        for i in range(MS.row + 2):
            temp = []
            for j in range(MS.column + 2):
                btn = New_Button(MS.window, x=i, y=j, width=3)
                btn.config(command=lambda s=btn: self.click(s))
                temp.append(btn)
            self.buttons.append(temp)

# размещение кнопок при помощи метода grid:
    def create_buttons(self):
        for i in range(1, MS.row + 1):
            for j in range(1, MS.column + 1):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j)

# вывод кнопок
    def print_buttons(self):
        for row_btn in self.buttons:
            print(row_btn)

# расстановка мин:
    def insert_mines(self):
        indaxes = list(range(1, MS.row * MS.column + 1))
        shuffle(indaxes)
        index_mines = indaxes[:MS.mines]
        print(index_mines)
        count = 1
        for i in range(1, MS.row + 1):
            for j in range(1, MS.column + 1):
                btn = self.buttons[i][j]
                btn.number = count
                if btn.number in index_mines:
                    btn.is_mine = True
                count += 1

# считаем мины вокруг кнопки:
    def count_mines(self):
        for i in range(1, MS.row + 1):
            for j in range(1, MS.column + 1):
                btn = self.buttons[i][j]
                count_bomb = 0
                if not btn.is_mine:
                    for row_dx in [-1, 0, 1]:
                        for col_dy in [-1, 0, 1]:
                            neighbour = self.buttons[i + row_dx][j + col_dy]
                            if neighbour.is_mine:
                                count_bomb += 1
                btn.count_bomb = count_bomb

# что будет, когда нажимаешь на кнопку
    def click(self, clicked_button):
        # print(clicked_button)
        if clicked_button.is_mine:
            clicked_button.config(text='*', background='black', disabledforeground='white')
        else:
            clicked_button.config(text=clicked_button.count_bomb)
        clicked_button.config(state='disabled', relief=tk.SUNKEN)

# запуск
    def start(self):
        self.create_buttons()
        self.insert_mines()
        self.count_mines()
        self.print_buttons()
        MS.window.mainloop()


game = MS()
game.start()