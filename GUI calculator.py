import tkinter.messagebox
from tkinter import *


# the template for calculator
class Calculator:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def add(self, n1, n2):
        return self.n1 + self.n2

    def subtract(self, n1, n2):
        return self.n1 - self.n2

    def multiply(self, n1, n2):
        return self.n1 * self.n2

    def divide(self, n1, n2):
        return self.n1 / self.n2


# validation of input
def validating_input(n1, n2):

    if not n1.isdigit() or not n2.isdigit():
        tkinter.messagebox.showerror('Python Error', 'The input is incorrect. You have not provided an integer!')


# addition
def add():
    number1 = E1.get()
    number2 = E2.get()

    validating_input(number1, number2)

    calculator = Calculator(float(number1), float(number2))
    return displaying_result.insert(0, calculator.add(float(number1), float(number2)))


# subtraction
def subtract():
    number1 = E1.get()
    number2 = E2.get()

    validating_input(number1, number2)

    calculator = Calculator(float(number1), float(number2))
    return displaying_result.insert(0, calculator.subtract(float(number1), float(number2)))


# multiplication
def multiply():
    number1 = E1.get()
    number2 = E2.get()

    validating_input(number1, number2)

    calculator = Calculator(float(number1), float(number2))
    return displaying_result.insert(0, calculator.multiply(float(number1), float(number2)))


# division
def divide():
    number1 = E1.get()
    number2 = E2.get()

    validating_input(number1, number2)

    if int(number1) == 0 or int(number2) == 0:
        tkinter.messagebox.showerror('Python Error','You cannot divide by 0. Math Error!')

    calculator = Calculator(number1, number2)
    return displaying_result.insert(0, calculator.divide(number1, number2))


def clear():
    displaying_result.delete(0, END)


def clear_number1():
    E1.delete(0, END)


def clear_number2():
    E2.delete(0, END)


# numbers input
root = Tk()
root.title('V3l"s first project')
root.geometry('650x200')
root.configure(bg='red')


number1_label = Label(root, text='Please enter first number: ', bg='red', font='Helvetica 15', fg='white')
number2_label = Label(root, text='Please enter second number: ', bg='red', font='Helvetica 15', fg='white')

number1_label.grid(row=0, column=1)
number2_label.grid(row=2, column=1)

E1 = Entry(root, bd=5, font='Helvetica 15')
E2 = Entry(root, bd=5, font='Helvetica 15')

E1.grid(row=0, column=2)
E2.grid(row=2, column=2)

# displaying result
result = Label(root, text='Result: ', bg='red', font='Helvetica 15', fg='white')
result.grid(row=3, column=1)

displaying_result = Entry(root, bd=5, width=20, font='Helvetica 15')
displaying_result.grid(row=3, column=2)


# calculator buttons
plus_button = Button(root, text='+', padx=50, command=add ,font='Helvetica 16', width=5).grid(row=4, column=2)
minus_button = Button(root, text='-', padx=50, command= subtract, font='Helvetica 16', width=5).grid(row=4, column=3)
divide_button = Button(root, text='/', padx=50, command= divide,font='Helvetica 16', width=5 ).grid(row=5, column=2)
multiply_button = Button(root, text='*', padx=50, command= multiply,font='Helvetica 16', width=5).grid(row=5, column=3)
clear_result_button = Button(root, text='Clear', padx=50, command=clear, font='Helvetica 16', width=5).grid(row=3, column=3)
clear_number1_button = Button(root, text='Clear', padx=50, command=clear_number1, font='Helvetica 16', width=5).grid(row=0, column=3)
clear_number2_button = Button(root, text='Clear', padx=50, command=clear_number2, font='Helvetica 16', width=5).grid(row=2, column=3)

root.mainloop()
