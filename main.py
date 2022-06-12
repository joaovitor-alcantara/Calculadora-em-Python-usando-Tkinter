from tkinter import *

root = Tk()
root.configure(background='#6495ED')
root.geometry('300x350')
root.title('CALCULADORA')
root.resizable(width=0, height=0)


janela = Frame(root)
janela.configure(background='#6495ED')
janela.grid()

lb1 = Label(janela, bg='#6495ED', fg='white')
lb1.grid(row=0, column=0, sticky='w')

display = Entry(janela)
display.grid(row=1, column=0, sticky='w', padx=15, ipadx=70, ipady=10)


# defining buttons functions


def button_click(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, str(current)+str(number))


def addition():
    global numberOne
    global operation
    operation = 'add'
    numberOne = display.get()
    display.delete(0, END)


def subtraction():
    global numberOne
    global operation
    operation = 'sub'
    numberOne = display.get()
    display.delete(0, END)


def multiplication():
    global numberOne
    global operation
    operation = 'mult'
    numberOne = display.get()
    display.delete(0, END)


def division():
    global numberOne
    global operation
    operation = 'div'
    numberOne = display.get()
    display.delete(0, END)


def equal():
    numberTwo = display.get()
    display.delete(0, END)

    if operation == 'add':
        display.insert(0, int(numberOne)+int(numberTwo))
    if operation == 'sub':
        display.insert(0, int(numberOne)-int(numberTwo))
    if operation == 'mult':
        display.insert(0, int(numberOne)*int(numberTwo))
    if operation == 'div':
        testing_num = int(numberOne) % int(numberTwo)
        if testing_num == 0:
            resp = int(numberOne) / int(numberTwo)
            answer = f'{resp:.0f}'
            answer = int(answer)
            display.insert(0, answer)
        else:
            resp = int(numberOne) / int(numberTwo)
            answer = f'{resp:.2f}'
            answer = float(answer)
            display.insert(0, answer)


def clear():
    display.delete(0, END)


# defining buttons
btn7 = Button(janela, text='7', bg='white', fg='black', command=lambda: button_click(7)).grid(
    row=2, column=0, ipadx=25, ipady=15, sticky='w', padx=10, pady=10)
btn8 = Button(janela, text='8', bg='white', fg='black', command=lambda: button_click(8)).grid(
    row=2, column=0, ipadx=25, ipady=15, sticky='w', padx=80)
btn9 = Button(janela, text='9', bg='white', fg='black', command=lambda: button_click(9)).grid(
    row=2, column=0, ipadx=25, ipady=15, sticky='w', padx=150)
btn_clear = Button(janela, text='c', bg='#FF7F50', fg='white', command=clear).grid(
    row=2, column=0, ipadx=25, ipady=15, sticky='w', padx=220)

btn_4 = Button(janela, text='4', bg='white', fg='black', command=lambda: button_click(4)).grid(
    row=3, column=0, ipadx=25, ipady=15, sticky='w', padx=10)
btn_5 = Button(janela, text='5', bg='white', fg='black', command=lambda: button_click(5)).grid(
    row=3, column=0, ipadx=25, ipady=15, sticky='w', padx=80)
btn_6 = Button(janela, text='6', bg='white', fg='black', command=lambda: button_click(6)).grid(
    row=3, column=0, ipadx=25, ipady=15, sticky='w', padx=150)
btn_division = Button(janela, text='/', bg='#FF7F50', fg='white', command=division).grid(
    row=3, column=0, ipadx=25, ipady=15, sticky='w', padx=220)

btn_1 = Button(janela, text='1', bg='white', fg='black', command=lambda: button_click(1)).grid(
    row=4, column=0, ipadx=25, ipady=15, sticky='w', padx=10, pady=10)
btn_2 = Button(janela, text='2', bg='white', fg='black', command=lambda: button_click(2)).grid(
    row=4, column=0, ipadx=25, ipady=15, sticky='w', padx=80)
btn_3 = Button(janela, text='3', bg='white', fg='black', command=lambda: button_click(3)).grid(
    row=4, column=0, ipadx=25, ipady=15, sticky='w', padx=150)
btn_multiply = Button(janela, text='x', bg='#FF7F50', fg='white', command=multiplication).grid(
    row=4, column=0, ipadx=25, ipady=15, sticky='w', padx=220)

btn_equal = Button(janela, text='=', bg='#FF7F50', fg='white', command=equal).grid(
    row=5, column=0, ipadx=25, ipady=15, sticky='w', padx=8)
btn_0 = Button(janela, text='0', bg='white', fg='black', command=lambda: button_click(0)).grid(
    row=5, column=0, ipadx=25, ipady=15, sticky='w', padx=80)
btn_minus = Button(janela, text='-', bg='#FF7F50', fg='white', command=subtraction).grid(
    row=5, column=0, ipadx=25, ipady=15, sticky='w', padx=151)
btn_add = Button(janela, text='+', bg='#FF7F50', fg='white', command=addition).grid(
    row=5, column=0, ipadx=25, ipady=15, sticky='w', padx=220)


root.mainloop()
