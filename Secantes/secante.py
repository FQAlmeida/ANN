from math import cos, sin, log, e
funcs = [{
    "f": lambda x: x ** 5 - 8 * x - 2,
    "valores_iniciais": [1, 2],
    "repeticoes": 5
},    {
    "f": lambda x: cos(x ** 2) - x,
    "valores_iniciais": [-1, 2],
    "repeticoes": 5
},    {
    "f": lambda x: log(x) + x ** 2,
    "valores_iniciais": [.5, 1],
    "repeticoes": 5
},    {
    "f": lambda x: log(x ** 2) + 2 * x,
    "valores_iniciais": [.5, 1],
    "repeticoes": 5
},    {
    "f": lambda x: cos(sin(x ** 2)) + x ** 3 - 2,
    "valores_iniciais": [1, 2],
    "repeticoes": 5
},    {
    "f": lambda x: (e ** (- x ** 2)) - x ** 2 + 5,
    "valores_iniciais": [2, 2.5],
    "repeticoes": 5
},    {
    "f": lambda x: e ** cos(x) + log(x ** 2),
    "valores_iniciais": [0.0001, 0.5],
    "repeticoes": 5
},    {
    "f": lambda x: x ** 2 * cos(x) + x - 1,
    "valores_iniciais": [0, 1],
    "repeticoes": 5
},    {
    "f": lambda x: 2 * cos(e ** x) - x,
    "valores_iniciais": [0, 1],
    "repeticoes": 5
},    {
    "f": lambda x: x ** 3 + x ** 2 + 0.001,
    "valores_iniciais": [-1.5, 0],
    "repeticoes": 5
}
]



def funcao_secantes(f, a, b):
    return (a * f(b) - b * f(a)) / (f(b) - f(a))


for i in funcs:
    f = i["f"]
    a, b = i["valores_iniciais"]
    n = i["repeticoes"]
    print("---------------------------------")
    for k in range(n):
        b, a = funcao_secantes(f,   a, b), b
        print(f"{k}: {b}")
