# -*- coding: utf-8 -*-
"""
@author: Camila Gallo García
"""
from numpy import random

def lista_diccionarios():
    lista = []
    
    for i in range(10):
        lista.append({"id": i, "edad": round(random.random()*100)})
    
    return lista

def orden_mayor_a_menor(listaAOrdenar):
    
    """
    Dada una lista de diccionarios, la función debe devolver 
    la lista ordenada e imprimir en patalla el id de la persona más joven y más grande. 
    
    >>> orden_mayor_a_menor([{'id': 0, 'edad': 41},{'id': 1, 'edad': 44},{'id': 2, 'edad': 21},{'id': 3, 'edad': 4},{'id': 4, 'edad': 61},{'id': 5, 'edad': 14},{'id': 6, 'edad': 96},{'id': 7, 'edad': 92},{'id': 8, 'edad': 3},{'id': 9, 'edad': 67}])
    El id de la persona más jóven es: 8
    El id de la persona más mayor es: 6
    [{'id': 6, 'edad': 96}, {'id': 7, 'edad': 92}, {'id': 9, 'edad': 67}, {'id': 4, 'edad': 61}, {'id': 1, 'edad': 44}, {'id': 0, 'edad': 41}, {'id': 2, 'edad': 21}, {'id': 5, 'edad': 14}, {'id': 3, 'edad': 4}, {'id': 8, 'edad': 3}]
    """
    
    edades =  []
    ordenado = []
    
    for diccionario in listaAOrdenar:
        edades.append(diccionario["edad"]) #Guardo las edades en una lista 
    
    for i in range(len(edades)): #ordeno las edades de mayor a menor
        for j in range(len(edades)):
            if  edades[i] > edades[j]:
                n = edades[i]      
                edades[i] = edades[j]
                edades[j] = n
                

    for i in range(len(edades)): #Busco el diccionario que cumple con la mayor edad
        for j in range(len(edades)):
            if edades[i] == listaAOrdenar[j]["edad"]:
                ordenado.append(listaAOrdenar[j])
    
    print("El id de la persona más jóven es: " + str(ordenado[9]["id"]) + "\n"+
          "El id de la persona más mayor es: " + str(ordenado[0]["id"]))
    
    return ordenado
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
