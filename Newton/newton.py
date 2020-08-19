from math import cos, sin, log, e


funcs = [{
    "f": lambda x: x ** 5 - 8 * x - 2,
    "d": lambda x: 5 * x ** 4 - 8,
    "x": -1,
    "repeticoes": 5
},    {
    "f": lambda x: cos(x ** 2) - x,
    "d": lambda x: -sin(x * 2) * 2 * x - 1,
    "x": 1,
    "repeticoes": 5
},    {
    "f": lambda x: log(x) + x ** 2,
    "d": lambda x: 1/x + 2 * x,
    "x": 1,
    "repeticoes": 5
},    {
    "f": lambda x: log(x ** 2) + 2 * x,
    "d": lambda x: 2/x + 2,
    "x": 1,
    "repeticoes": 5
},    {
    "f": lambda x: cos(sin(x ** 2)) + x ** 3 - 2,
    "d": lambda x: 3 * x ** 2 - 2 * x * sin(sin(x ** 2)) * cos(x**2),
    "x": 1,
    "repeticoes": 5
},    {
    "f": lambda x: (e ** (- x ** 2)) - x ** 2 + 5,
    "d": lambda x: -2*e ** (- x ** 2) * x - 2 * x,
    "x": 2,
    "repeticoes": 5
},    {
    "f": lambda x: e ** cos(x) + log(x ** 2),
    "d": lambda x: -e ** cos(x) * sin(x) + 2/x,
    "x": 0.0001,
    "repeticoes": 5
},    {
    "f": lambda x: x ** 2 * cos(x) + x - 1,
    "d": lambda x: -x**2 * sin(x) + 2 * x * cos(x) + 1,
    "x": .5,
    "repeticoes": 5
},    {
    "f": lambda x: 2 * cos(e ** x) - x,
    "d": lambda x: -2 * e ** x * sin(e ** x) - 1,
    "x": .5,
    "repeticoes": 5
},    {
    "f": lambda x: x ** 3 + x ** 2 + 0.001,
    "d": lambda x: 3 * x ** 2 + 2 * x,
    "x": -1,
    "repeticoes": 5
}
]


def funcao_newton(xk, f, d):
    return xk - f(xk) / d(xk)


for i in funcs:
    n = i["repeticoes"]
    x = i["x"]
    d = i["d"]
    f = i["f"]
    xk = x
    print("--------------------------")
    for k in range(n):
        xk = funcao_newton(xk, f, d)
        print(f"{k}: {xk}")
