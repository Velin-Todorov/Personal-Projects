from sympy import Symbol, factor, expand, pprint, init_printing, sympify, solve, plot
from sympy.core.sympify import SympifyError


def solver(expr11, expr22, x, y):
    sol = solve((expr11, expr22), dict=True)
    if sol:
        print('x: {0} y:{1}'.format(sol[0][x], sol[0][y]))
    else:
        print('No solution found')

    eq1 = solve(expr11, 'y')[0]
    eq2 = solve(expr22, 'y')[0]

    plot(eq1, eq2, legend=True)


if __name__ == '__main__':
    expr1 = input('Enter an expression in terms of x and y: ')
    expr2 = input('Enter an expression in terms of x and y: ')
    try:
        expr1 = sympify(expr1)
        expr2 = sympify(expr2)

    except SympifyError as e:
        print(e)

    else:
        x = Symbol('x')
        y = Symbol('y')

        eq1_syms = expr1.atoms(Symbol)
        eq2_syms = expr2.atoms(Symbol)

        solver(expr1, expr2, x, y)


