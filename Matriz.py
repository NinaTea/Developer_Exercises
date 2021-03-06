# -*- coding: utf-8 -*-
"""
@author: Camila Gallo García
"""

import numpy as np

matriz = np.around(np.random.random((5,5))*100)


h = []    
i = 0
j = 1
while True:
    #Sólo se fija en los primeros dos elementos porque debido al tamaño de la matriz
    #la secuencia, de izquierda a derecha, de números sólo puede empezar
    #en los primeros dos elementos
    if matriz[i][j-1] < matriz[i][j] < matriz[i][j+1] < matriz[i][j+2] :
        h.append((i,j-1))
        h.append((i,j+2))
    if matriz[i][j] < matriz[i][j+1] < matriz[i][j+2] < matriz[i][j+3] :
        h.append((i,j))
        h.append((i,j+3))
    i+=1
    if i > 4:
        break

    
a = 1
b = 0
v = []
while True:
    #Mismo razomiento que en la secuencia horizontal
    if matriz[a-1][b] < matriz[a][b] < matriz[a+1][b] < matriz[a+2][b] :
        v.append((a-1,b))
        v.append((a+2,b))
    if matriz[a][b] < matriz[a+1][b] < matriz[a+2][b] < matriz[a+3][b] :
        v.append((a,b))
        v.append((a+3,b))

    b+=1
    if b > 4:
        break

    
print("La matriz random resultante fue: ", matriz)
print("Las coordenadas de la secuencia horizontal encontrada son: ", h)
print("Las coordenadas de la secuencia vertical encontrada son: ", v)
print("Aclaración: Si una lista está vacía es porque no se encontró ninguna secuencia.")
