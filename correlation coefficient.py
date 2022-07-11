import math
from matplotlib import pyplot as plt


def check(x, y):
    if len(x) == len(y):
        return 1
    else:
        return 0


def find_corr_x_y(x, y):
    n = len(x)

    prod = []
    for xi, yi in zip(x, y):
        prod.append(xi * yi)

    sum_prod_x_y = sum(prod)
    sum_x = sum(x)
    sum_y = sum(y)
    squared_sum_x = sum_x ** 2
    squared_sum_y = sum_y ** 2

    x_squared = []
    for xi in x:
        x_squared.append(xi ** 2)

    x_squared_sum = sum(x_squared)

    y_squared = []

    for yi in y:
        y_squared.append(yi ** 2)

    y_squared_sum = sum(y_squared)

    numerator = n * sum_prod_x_y - sum_x * sum_y
    denominator = math.sqrt((n * squared_sum_x - sum_x) * (n * squared_sum_y - sum_y))

    correlation = numerator / denominator

    return correlation


if __name__ == '__main__':
    x = [90, 92, 95, 96, 87, 87, 90, 95, 98, 96]
    y = [85, 87, 86, 97, 96, 88, 89, 98, 98, 90]
   # result = check(x, y)

    try:
        corr = find_corr_x_y(x, y)
        plt.scatter(x, y)
        plt.show()
        print(corr)

    except ValueError as e:
        print(e)
        print('Correlation cannot be found!')
