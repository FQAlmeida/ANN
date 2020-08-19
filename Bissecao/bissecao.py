from math import cos, sin, log, e


funcs = [{
    "f": lambda x: x ** 5 - 8 * x - 2,
    "intervalo": [1, 2],
    "repeticoes": 5
},    {
    "f": lambda x: cos(x ** 2) - x,
    "intervalo": [-1, 2],
    "repeticoes": 5
},    {
    "f": lambda x: log(x) + x ** 2,
    "intervalo": [.5, 1],
    "repeticoes": 5
},    {
    "f": lambda x: log(x ** 2) + 2 * x,
    "intervalo": [.5, 1],
    "repeticoes": 5
},    {
    "f": lambda x: cos(sin(x ** 2)) + x ** 3 - 2,
    "intervalo": [1, 2],
    "repeticoes": 5
},    {
    "f": lambda x: (e ** (- x ** 2)) - x ** 2 + 5,
    "intervalo": [2, 2.5],
    "repeticoes": 5
},    {
    "f": lambda x: e ** cos(x) + log(x ** 2),
    "intervalo": [0.0001, 0.5],
    "repeticoes": 5
},    {
    "f": lambda x: x ** 2 * cos(x) + x - 1,
    "intervalo": [0, 1],
    "repeticoes": 5
},    {
    "f": lambda x: 2 * cos(e ** x) - x,
    "intervalo": [0, 1],
    "repeticoes": 5
},    {
    "f": lambda x: x ** 3 + x ** 2 + 0.001,
    "intervalo": [-1.5, 0],
    "repeticoes": 5
}
]


def funcao_1(x):
    return funcs[0](x)


intervalo = [0, 1]
repeticoes = 5


def bissecao(f, a, b, iteracoes):
    for i in range(iteracoes):
        n = (a + b) / 2
        resp_a = f(a)
        resp_b = f(b)
        resp_n = f(n)
        print(f"{i+1}) {n}")
        if resp_n == 0:
            print(f"A resposta é: {n}")
            break
        elif resp_a * resp_n < 0:
            b = n
        elif resp_b * resp_n < 0:
            a = n


for i in funcs:
    f = i["f"]
    a, b = i["intervalo"]
    n = i["repeticoes"]
    print("---------------------------------")
    bissecao(f, a, b, n)
