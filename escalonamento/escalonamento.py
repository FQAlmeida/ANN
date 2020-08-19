from pprint import pprint
a = [[4.0773, -2.4311, 3.29533, -1.3561, -1.439, 4.8437, -4.6728, -4.6556],
     [4.3016, -0.6597, -0.051, -1.232, 2.8784, -4.6575, -1.0685, -3.8988],
     [-3.9988, 4.0595, 3.2832, 1.2192, 1.5654, 1.3718, -2.5761, 3.2102],
     [-4.5069, 2.4142, 1.3464, -1.0711, 1.4539, -3.3201, -4.9439, 4.7887],
     [4.368, 0.9132, 1.0345, 2.1168, 2.9627, 2.8548, -2.5592, 2.7701],
     [-0.3954, -2.2655, -4.1126, -4.0911, 1.3996, -4.1031, -4.3896, -2.7001],
     [2.5599, -4.6319, -3.7891, 2.0063, -4.2503, 4.0969, -0.6511, 1.5592],
     [0.0049, -2.6163, 0.3524, -2.306, -4.4778, 1.2386, -3.0412, -0.18]]

b = [-3.575, 4.0053, -1.9704, 4.0497, -1.8963, 4.823, 3.0337, 2.5182]


def matriz_extendida(matriz_a: list, matriz_b: list):
    matriz_aux = matriz_a.copy()
    for i in range(len(matriz_a)):
        matriz_aux[i].append(matriz_b[i])
    return matriz_aux


def trocar_linha(matriz, linha_a, linha_b):
    matriz_aux = matriz.copy()
    matriz_aux[linha_a], matriz_aux[linha_b] = matriz[linha_b], matriz[linha_a]
    return matriz_aux


def multiplicar_por_escalar(matriz, escalar, linha):
    matriz_aux = matriz.copy()
    for index, item in enumerate(matriz[linha]):
        matriz_aux[linha][index] = item*escalar
    return matriz_aux


def trocar_linha_combinacao(matriz, linha_a, linha_b, escalar):
    matriz_aux = matriz.copy()
    # print(f"L1: {linha_a + 1} L2: {linha_b + 1} E: {escalar}")
    for index in range(len(matriz[linha_a])):
        matriz_aux[linha_b][index] = escalar * matriz[linha_a][index] + matriz[linha_b][index]
    return matriz_aux


def escalonar(matriz_est):
    matriz_aux = matriz_est.copy()
    for i in range(len(matriz_aux)):
        for j in range(i+1, len(matriz_aux)):
            matriz_aux = trocar_linha_combinacao(
                matriz_aux, i, j, -matriz_aux[j][i] / matriz_aux[i][i])
    return matriz_aux


def print_matriz(matriz):
    print('[')
    for index_linha, linha in enumerate(matriz):
        print('\t[', end="")
        for index, item in enumerate(linha):
            print(f"{item:.4f}", end=(", " if index+1 != len(linha) else ""))
        print('],' if index_linha+1 != len(matriz) else "]")
    print(']')


if __name__ == "__main__":
    print_matriz(escalonar(matriz_extendida(a, b)))
