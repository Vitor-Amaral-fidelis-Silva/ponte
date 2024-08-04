import numpy as np
import scipy.linalg

def verificar_matriz(a):
    A = np.array(a)
    if np.linalg.matrix_rank(A) < len(A):
        print("A matriz A é singular ou mal formada.")
    else:
        print("A matriz A não é singular.")

def resolver_sistema_lu(a, b):
    A = np.array(a)
    B = np.array(b)

    try:
        P, L, U = scipy.linalg.lu(A)
        y = np.linalg.solve(L, np.dot(P, B))
        X = np.linalg.solve(U, y)
        print("Solução exata encontrada:")
    except np.linalg.LinAlgError as e:
        print(f"Erro ao resolver o sistema de equações: {e}")
        X = np.dot(np.linalg.pinv(A), B)
        print("Solução aproximada usando pseudo-inversa:")

    descricoes_forcas = [
        "a1", "a2", "a3", "a4", "b1", "b2", "b3", "b4", 
        "c1", "c2", "c3", "d1", "d2", "d3", "z1", "z2", 
        "z3", "z4", "w1", "w2", "w3", "w4", "v1", "v2", 
        "v3", "v4", "v5", "v6", "v7", "ni", "np", "fx"
    ]

    for i, valor in enumerate(X):
        descricao = descricoes_forcas[i]
        print(f"Força {descricao}: {valor}")

x = np.sqrt(2) / 2

a = [
    [0.0] * 32 for _ in range(32)
]

a1 = 0
a2 = 1
a3 = 2
a4 = 3
b1 = 4
b2 = 5
b3 = 6
b4 = 7
c1 = 8
c2 = 9
c3 = 10
d1 = 11
d2 = 12
d3 = 13
z1 = 14
z2 = 15
z3 = 16
z4 = 17
w1 = 18
w2 = 19
w3 = 20
w4 = 21
v1 = 22
v2 = 23
v3 = 24
v4 = 25
v5 = 26
v6 = 27
v7 = 28
ni = 29
nP = 30
fx = 31

#a
    #x
a[0][a4] = 1
a[0][b4] = 1
    #y
a[1][v4] = 1

#b
    #x
a[2][z4] = x
a[2][c3] = 1
a[2][d3] = 1
a[2][w4] = x
    #y
a[3][z4] = x
a[3][v4] = 1
a[3][w4] = x

#c
    #x
a[4][z4] = x
a[4][a4] = 1
a[4][a3] = 1
    #y
a[5][z4] = x
a[5][v3] = 1

#d
    #x
a[6][z3] = x
a[6][c3] = 1
a[6][c2] = 1
    #y
a[7][z3] = x
a[7][v3] = 1

#e
    #x
a[8][z3] = x
a[8][a3] = 1
a[8][a2] = 1
    #y
a[9][z3] = x
a[9][v2] = 1

#f
    #x
a[10][z2] = x
a[10][c2] = 1
a[10][c1] = 1
    #y
a[11][z2] = x
a[11][v2] = 1

#g
    #x
a[12][z2] = x
a[12][a1] = 1
a[12][a2] = 1
    #y
a[13][z2] = x
a[13][v1] = 1

#h
    #x    
a[14][z1] = x
a[14][c1] = 1
    #y
a[15][z1] = x
a[15][v1] = 1

#i
    #x
a[16][z1] = x
a[16][a1] = 1
a[16][fx] = 1
    #y
a[17][z1] = x
a[17][ni] = 1

#j
    #x
a[18][w4] = x
a[18][b4] = 1
a[18][b3] = 1
    #y
a[19][w4] = x
a[19][v5] = 1
#k
    #x
a[20][w3] = x
a[20][d3] = 1
a[20][d2] = 1
    #y
a[21][w3] = x
a[21][v5] = 1

#l
    #x
a[22][w3] = x
a[22][b3] = 1
a[22][b2] = 1
    #y
a[23][w3] = x
a[23][v6] = 1
#m
    #x
a[24][w2] = x
a[24][d2] = 1
a[24][d1] = 1
    #y
a[25][w2] = x
a[25][v6] = 1

#n
    #x
a[26][w2] = x
a[26][b2] = 1
a[26][b1] = 1
    #y
a[27][w2] = x
a[27][v7] = 1

#o
    #x
a[28][w1] = x
a[28][d1] = 1
    #y
a[29][w1] = x
a[29][v7] = 1

#p
    #x
a[30][w1] = x
a[30][b1] = 1
    #y
a[31][w1] = x
a[31][nP] = 1

b = [0.0]*32
peso = 900.0
b[1] = peso

verificar_matriz(a)
resolver_sistema_lu(a, b)
