""""

Area between 2 curves
"""
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot
from sympy import Integral, Symbol, sympify
from sympy import SympifyError

s = Symbol('x')

upper_function = input('Please enter the upper function in terms of x: ')
lower_function = input('Please enter the lower function in terms of x: ')
a = input("Please enter the value for the lower bound: ")
b = input("Please enter the value for the upper bound: ")

try:
    u = sympify(upper_function)
    l = sympify(lower_function)

    integral_1 = Integral(upper_function, (s, int(a), int(b))).doit()
    integral_2 = Integral(lower_function, (s, int(a), int(b))).doit()

    area_under = integral_1 - integral_2

except SympifyError as e:
    print(e)

else:
    print(area_under)

