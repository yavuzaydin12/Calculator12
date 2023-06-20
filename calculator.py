import tkinter as tk
from time import strftime
from tkinter.ttk import *


def clear_entry():
    calc.delete(0, tk.END)
    calc.insert(0, '0')

def add_digit(digit):
    value = calc.get()
    if value[0] == '0':
        value = value[1:]
        #print("HERE")
    calc.delete(0, tk.END)
    calc.insert(0, value+str(digit))

def add_operation(operation):
    value = calc.get()
    if value[-1] in '+-/*':
        value = value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, value+operation)

win = tk.Tk()
win.geometry(f"240x270+100+200")
win['bg'] = "black"
win.title("Calculator")

def make_clear_button(clear):
    return tk.Button(text=clear, bd=5, font=("Arial", 13), command=clear_entry)

def calculate():
    value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, eval(value))
win.resizable(0, 0)
def make_operation_button(operation):
    return tk.Button(text=operation, bd = 5, font=("Arial", 13), command = lambda:add_operation(operation))
win.resizable(True, True)
def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 13), command=calculate)
def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=("Arial", 13), command=lambda: add_digit(digit))
calc = tk.Entry(win, justify=tk.RIGHT, font=("Arial", 15), width=15) #метод justify показывает к какой стороне будет прижиматься текст
calc.insert(0,'0')
calc.grid(row = 0, column = 0, columnspan=4, stick = "we")    #row  - ряд column - колонка  #здесь grid работает как input #метод Grid является одним из трех менеджеров геометрии в Tkinter (другими являются уже рассмотренный ранее Pack, а также Place). У всех виджетов есть соответствующий данному менеджеру метод grid. "Grid" с английского переводится как "сетка", однако по смыслу правильнее говорить о таблице.
#метод columnspan объединяет все колонки в 1 которые будут находиться ровно под указаным grid
make_digit_button("1").grid(row = 1, column = 0, stick = "news", padx = 5, pady = 5) #метод stick расширяет объекты до краев в указанную сторону
make_digit_button("2").grid(row = 1, column = 1, stick = "news", padx = 5, pady = 5) # в данном случае мы расширили кнопки во все 4 стороны света
make_digit_button("3").grid(row = 1, column = 2, stick = "news", padx = 5, pady = 5)
make_digit_button("4").grid(row = 2, column = 0, stick = "news", padx = 5, pady = 5)
make_digit_button("5").grid(row = 2, column = 1, stick = "news", padx = 5, pady = 5)
make_digit_button("6").grid(row = 2, column = 2, stick = "news", padx = 5, pady = 5)
make_digit_button("7").grid(row = 3, column = 0, stick = "news", padx = 5, pady = 5)
make_digit_button("8").grid(row = 3, column = 1, stick = "news", padx = 5, pady = 5)
make_digit_button("9").grid(row = 3, column = 2, stick = "news", padx = 5, pady = 5)
make_digit_button("0").grid(row = 4, column = 0, stick = "news", padx = 5, pady = 5)



#есть атрибуты которые отвечают за расстояние между объектами они называются padx и pady
#bd создает толщину рамки у объектов
#command дает определенную команду для объектов, в данном случае она лишь добавляет цифру в строку ввода

make_operation_button('+').grid(row = 1, column = 3, stick = "news", padx = 5, pady = 5)
make_operation_button('-').grid(row = 2, column = 3, stick = "news", padx = 5, pady = 5)
make_operation_button('/').grid(row = 3, column = 3, stick = "news", padx = 5, pady = 5)
make_operation_button('*',).grid(row = 4, column = 3, stick = "news", padx = 5, pady = 5)

make_calc_button("=").grid(row = 4, column = 2, stick = "news", padx = 5, pady = 5)

make_clear_button("C").grid(row = 4, column = 1, stick = "news", padx = 5, pady = 5)



win.grid_columnconfigure(0,minsize=60)
win.grid_columnconfigure(1,minsize=60)
win.grid_columnconfigure(2,minsize=60)
win.grid_columnconfigure(3,minsize=60)

win.grid_rowconfigure(1,minsize=60)
win.grid_rowconfigure(2,minsize=60)
win.grid_rowconfigure(3,minsize=60)
win.grid_rowconfigure(4,minsize=60)


win.mainloop()

