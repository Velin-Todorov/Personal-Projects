from matplotlib import pyplot as plt


def graph(y):
    plt.plot(y)
    plt.title('Golden ratio')
    plt.show()


def fibo(n):

    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]

    a = 1
    b = 1
    series = [a, b]
    for i in range(n):
        c = a + b
        series.append(c)
        a = b
        b = c

    return series


def ratio(n):
    ratios = []

    result = fibo(n)
    for x in range(len(result) - 1):
        ratios.append(result[x + 1]/result[x])

    return ratios

num = 200
results = ratio(num)

graph(results)