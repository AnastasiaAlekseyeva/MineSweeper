import tkinter as tk
from random import shuffle
from tkinter.messagebox import showinfo

# пишем свой собственный класс, который наследуется от класса Button из tkinter.
class NewButton(tk.Button):
    def __init__(self, master, x, y, number=0, *args, **kwargs):
        super(NewButton, self).__init__(master, *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.is_mine = False
        self.count_bomb = 0

    def __repr__(self):
        return f'NewButton{self.x}{self.y} {self.number} {self.is_mine}'


class MS:
    window = tk.Tk()
    row = 6
    column = 5
    mines = 5
    game_over = False

    def __init__(self):
        self.buttons = []
        for i in range(MS.row + 2):
            temp = []
            for j in range(MS.column + 2):
                btn = NewButton(MS.window, x=i, y=j, width=3)
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

        # запрет нажатия на кнопки после проигрыша:
        if MS.game_over:
            return

        if clicked_button.is_mine:
            clicked_button.config(text='*', background='black', disabledforeground='white')
            MS.game_over = True
            showinfo('Game over', 'Вы проиграли!')
            for i in range(1, MS.row + 1):
                for j in range(1, MS.column + 1):
                    btn = self.buttons[i][j]
                    if btn.is_mine:
                        btn['text'] = '*'

        elif clicked_button.count_bomb == 1:
            clicked_button.config(text=clicked_button.count_bomb, disabledforeground='#1909f1')
        elif clicked_button.count_bomb == 2:
            clicked_button.config(text=clicked_button.count_bomb, disabledforeground='#046615')
        elif clicked_button.count_bomb == 3:
            clicked_button.config(text=clicked_button.count_bomb, disabledforeground='#f6e60f')
        elif clicked_button.count_bomb == 4:
            clicked_button.config(text=clicked_button.count_bomb, disabledforeground='#65036d')
        elif clicked_button.count_bomb == 5:
            clicked_button.config(text=clicked_button.count_bomb, disabledforeground='#6c0622')
        elif clicked_button.count_bomb == 6:
            clicked_button.config(text=clicked_button.count_bomb, disabledforeground='#f6e60f')
        elif clicked_button.count_bomb == 7:
            clicked_button.config(text=clicked_button.count_bomb, disabledforeground='#f5980e')
        elif clicked_button.count_bomb == 8:
            clicked_button.config(text=clicked_button.count_bomb, disabledforeground='#f50f0f')
        else:
            clicked_button.config(text='')
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
