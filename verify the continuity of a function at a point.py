from sympy import Symbol, Limit, S, solve, sympify
from sympy.core.sympify import SympifyError


def continuity_check(f, var, p):
    var = Symbol(var)
    l1 = Limit(f, var, p).doit().evalf()
    l2 = Limit(f, var, p).doit().evalf()
    expr = f.subs({var : p})
    if l1 == l2  and l1 == expr:
        print('{0} is continuous at {1}'.format(f, p))

    else:
        print('{0} is not continuous at {1}'.format(f, p))


if __name__ == '__main__':
    func = input('Enter a function in one variable: ')
    v = input('Enter the variable: ')
    val = float(input('Enter the point to check the continuity at: '))
    try:
        f = sympify(func)
    except SympifyError:
        print('Try again')

    else:
        continuity_check(f, v, val)

